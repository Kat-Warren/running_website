from flask import Flask, session, jsonify, request, redirect, url_for, flash, render_template
from app import app, db
from .models import Login, Races
from datetime import datetime
from sqlalchemy import select
import json

#Register Page
@app.route('/register', methods=['GET'])
def register_page():
  return render_template('register.html')

#Register the user
@app.route('/register', methods=['POST'])
def register():
    if request.is_json:
        user_data = request.get_json()
    else:
        user_data = request.form.to_dict()
    username = user_data.get('username')
    password = user_data.get('password')

    if not username or not password:
        return jsonify({'status': 'error', 'message': 'Username and password are required'}), 400


    #Check if register before
    exists_user = Login.query.filter_by(username=username).first()
    if exists_user:
        #REFERNCE: jsonify knowalge and use used
        #GeeksforGeeks. (2023). Use jsonify() instead of json.dumps() in Flask. [online] Available at: https://www.geeksforgeeks.org/use-jsonify-instead-of-json-dumps-in-flask/.
        return jsonify({'status': 'error', 'message': 'Username already exists'}), 409
    new_user = Login(username=username)
    new_user.set_password(password)  # Use the set_password method to hash the password
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Account created successfully'}), 201

#Login Page
@app.route('/login', methods=['GET'])
def login_page():
  return render_template('login.html')

#Login Page
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({'status': 'error', 'message': 'Request must be in JSON format'}), 400

    try:
        # Parse JSON data
        user_data = request.get_json()
        username = user_data.get('username')
        password = user_data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({'status': 'error', 'message': 'Username and password are required'}), 400

        # Query the database for the user
        user = Login.query.filter_by(username=username).first()

        # Check if the user exists and password matches
        if user and user.check_password(password):
            session['user_id'] = user.id
            return jsonify({'status': 'success', 'message': 'Login Successful'}), 200
        else:
            return jsonify({'status': 'error', 'message': 'Invalid username or password'}), 401

    except Exception as e:
        # Log the error and return a generic error response
        app.logger.error(f"Login error: {e}")
        return jsonify({'status': 'error', 'message': 'An unexpected error occurred'}), 500



@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if request.method == 'GET':
        # Render the change password page
        return render_template('change_password.html')

    # Handle the POST request for changing the password
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"message": "Unauthorized access. Please log in."}), 401

    data = request.get_json()
    new_password = data.get("new_password")
    if not new_password:
        return jsonify({"message": "New password is required."}), 400

    try:
        user = Login.query.get(user_id)
        if not user:
            return jsonify({"message": "User not found."}), 404

        user.set_password(new_password)
        db.session.commit()
        return jsonify({"message": "Password updated successfully!"}), 200
    except Exception as e:
        app.logger.error(f"Password change error: {e}")
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500
@app.route('/display_races')
def display_races():
    races = Races.query.all()
    return render_template('display_races.html', races=races)

@app.route('/save_race/<int:race_id>', methods=['POST'])
def save_race(race_id):
    user_id = session.get('user_id')  # Get the logged-in user from the session
    if not user_id:
        flash('You must be logged in to save a race!', 'danger')
        return redirect(url_for('login'))

    # Fetch user and race objects
    user = Login.query.get(user_id)
    race = Races.query.get(race_id)

    if not race:
        flash('Race not found!', 'danger')
        return redirect(url_for('home'))

    # Add the race to the user's saved races if not already saved
    if race not in user.saved_races:
        user.saved_races.append(race)
        db.session.commit()
        flash(f'Race "{race.name}" saved successfully!', 'success')
    else:
        flash(f'Race "{race.name}" is already in your saved races.', 'info')

    return redirect(url_for('home'))

@app.route('/saved_races')
def saved_races():
    user_id = session.get('user_id')  # Get the logged-in user
    if not user_id:
        flash('You must be logged in to view saved races!', 'danger')
        return redirect(url_for('login'))

    user = Login.query.get(user_id)
    return render_template('saved_races.html', races=user.saved_races)

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove user ID from session
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))



                    
#Home page   
@app.route('/', methods=['GET', 'POST'])
def home():
    username = session.get('username')  # Retrieve username from session
    return render_template('home.html', username=username)

@app.context_processor
def inject_user():
    return {'username': session.get('username')}



if __name__ == '__main__':
    app.run(debug=True)







