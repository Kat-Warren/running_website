from app import db
import hashlib 


#Bridge Table 
user_race = db.Table(
    'user_race',
    db.Column('user_id', db.Integer, db.ForeignKey('Login.id'), primary_key=True),
    db.Column('race_id', db.Integer, db.ForeignKey('race.id'), primary_key=True)
)



class Login(db.Model):
    __tablename__ = 'Login'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), nullable= False, unique= True)
    password = db.Column(db.String(120), nullable=False)

    saved_races = db.relationship('Races', secondary=user_race, back_populates='users')

        #Reference for the hash
        #Python (n.d.). hashlib — Secure hashes and message digests — Python 3.8.4rc1 documentation. [online] docs.python.org. Available at: https://docs.python.org/3/library/hashlib.html.
    def set_password(self, password):
        if not password:
            raise ValueError("Password cannot be empty.")
        # Hash the password and save it in the 'password' column
        hash = hashlib.sha256(password.encode('utf-8'))
        self.password = hash.hexdigest()  # Correct column name
        print("Hashed Password:", self.password)

    def check_password(self, password):
        # Hash the provided password and compare it to the stored hash
        hash = hashlib.sha256(password.encode('utf-8'))
        return self.password == hash.hexdigest()
    
    

class Races(db.Model):
    __tablename__ = 'race'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(500), index=True, unique=True)
    date = db.Column(db.DateTime)
    description = db.Column(db.String(500))
    competing = db.Column(db.Boolean)

    users = db.relationship('Login', secondary=user_race, back_populates='saved_races')


