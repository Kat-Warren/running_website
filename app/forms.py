from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, BooleanField, SubmitField, DateTimeField
from wtforms.validators import DataRequired

class AssessmentForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    deadline = DateTimeField('Deadline', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    complete = BooleanField('Complete')
    submit = SubmitField('Add Assessment')

