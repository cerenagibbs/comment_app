from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    book_title = StringField("Book Title", validators=[DataRequired()])
    book_summary = TextAreaField("Book Summary", validators=[DataRequired()])
    submit = SubmitField("Submit")

class TeacherFeedbackForm(FlaskForm):
    class_options = [("Math","Math"), ("English","English"), ("Science","Science")]
    class_chosen = RadioField("Classes", choices=class_options)
    student_name = StringField("Student Name", validators=[DataRequired()])
    teacher_feedback = TextAreaField("Feedback", validators=[DataRequired()])
    add_feedback  = SubmitField("Add Feedback")

class NewBookForm(FlaskForm):
    student_name = StringField("Student Name", validators=[DataRequired()])
    choose_this_book = SubmitField("Choose This Book")
    book_options = [("Harry Potter and the Chamber of Secrets","Harry Potter and the Chamber of Secrets"), ("Ghost","Ghost"), ("Running Out Of Time","Running Out Of Time")]
    book_chosen = RadioField("Classes", choices=book_options)
