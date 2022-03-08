from flask import Flask, render_template, request
from forms import BookForm
from forms import TeacherFeedbackForm
from forms import NewBookForm
import json
import psycopg2




app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'


@app.route("/")
def index_page():
    return render_template("home_page.html")



file_connection = open("C:\Git\evania\comment_app\summaries.json", 'r')
summary = json.load(file_connection) #to  load the json file
file_connection.close()

summary=[]
@app.route("/school/book_summary", methods = ["GET", "POST"])
def book_summary():
    print("THIAGO")

    #establishing the connection
    conn = psycopg2.connect(
        database="postgres", 
        user='digitalboost', 
        password='digitalboost', 
        host='127.0.0.1', 
        port= '5432')
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # cursor.execute("select version()")
    # db_version = cursor.fetchone()
    # print(db_version)
    
    book_form = BookForm(csrf_enabled=False)
    if book_form.validate_on_submit(): #validators make sure that the fields are not left blank
        sql_command = f"insert into summary(book_title, book_summary) values ('{book_form.book_title.data}','{book_form.book_summary.data}')"
        cursor.execute(sql_command)
        conn.commit()
        cursor.close()
        conn.close()

    return render_template("book_summary.html",
    template_form = book_form, summary = summary)


# feedback=[]
# file_connection = open("C:/Git/evania/comment_app/feedback.json", 'r')
# feedback = json.load(file_connection)
# file_connection.close()
#
#
# @app.route("/school/teacher_feedback", methods = ["GET", "POST"])
# def teacher_feedback():
#     teacher_feedback_form = TeacherFeedbackForm(csrf_enabled=False)
#     if teacher_feedback_form.validate_on_submit():
#         id = len(feedback) + 1
#         feedback.append({
#       "student_name": teacher_feedback_form.student_name.data,
#       "class_chosen":teacher_feedback_form.class_chosen.data,
#       "teacher_feedback": teacher_feedback_form.teacher_feedback.data
#     })
#     file_connection = open("C:/code/comment_app/feedback.json", 'w')
#     json.dump(feedback, file_connection)
#     file_connection.close()
#     return render_template("teacher_feedback.html",
#     template_form = teacher_feedback_form, feedback = feedback)
#
# book=[]


# @app.route("/school/new_book", methods = ["GET", "POST"])
# def new_book():
#     new_book_form = NewBookForm(csrf_enabled=False)
#     if new_book_form.validate_on_submit():
#         id = len(book) + 1
#         book.append({
#       "student_name": new_book_form.student_name.data,
#       "book_chosen":new_book_form.book_chosen.data
#     })
#     return render_template("new_book.html",
#     template_form = new_book_form, book = book)
#
#     #.book-summary-body {
#     #background-image: url("/static/main/childrensbook.jpg");
#     #background-size: cover;
#     #background-position: -245px -55px;
#     #background-repeat: no-repeat;



