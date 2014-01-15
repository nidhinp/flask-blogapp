from flask.ext.sqlalchemy import SQLAlchemy
from flask import *
from time import *
import psycopg2
import os


app = Flask(__name__)


USERNAME = 'admin'
PASSWORD = 'password'


@app.route('/comments', methods = ['GET', 'POST'])
def comments():
    conn = psycopg2.connect(database="d600bqomrbg8er", user = "mxwgzzfpkciuuh", password = "tVKQ_Quhpk1m2yejMakND1MEAn", host = "ec2-184-73-194-196.compute-1.amazonaws.com" , port = "5432")
    cur = conn.cursor()
    cur.execute("INSERT INTO newcomments(title, name, comment) VALUES(%s, %s, %s)",[request.form['title'], request.form['name'], request.form['comment']])
    conn.commit()
    cur.execute("SELECT title, body, day, time FROM newblogposts ORDER BY id DESC")
    entries = cur.fetchall()
    cur.execute("SELECT title, name, comment FROM newcomments ORDER BY id DESC")
    comments = cur.fetchall()
    conn.close()
    return render_template('posts.html', title = 'posts', entries = entries, comments = comments)

@app.route('/posts', methods = ['GET', 'POST'])
def posts():
    conn = psycopg2.connect(database="d600bqomrbg8er", user = "mxwgzzfpkciuuh", password = "tVKQ_Quhpk1m2yejMakND1MEAn", host = "ec2-184-73-194-196.compute-1.amazonaws.com" , port = "5432")
    cur = conn.cursor()
    cur.execute("SELECT title, body, day, time FROM newblogposts ORDER BY id DESC")
    entries = cur.fetchall()
    cur.execute("SELECT title, name, comment FROM newcomments ORDER BY id DESC")
    comments = cur.fetchall()
    conn.close()
    return render_template('posts.html', title = 'posts', entries = entries, comments = comments)


@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != USERNAME:
            error = 'Invalid Username'
        if request.form['password'] != PASSWORD:
            error = 'Invalid Password'
        else:
            return redirect(url_for('posts'))
    return render_template('login.html', error = error)

@app.route('/newpost', methods = ['GET', 'POST'])
def newpost():
    if request.method == 'POST':
        conn = psycopg2.connect(database="d600bqomrbg8er", user = "mxwgzzfpkciuuh", password = "tVKQ_Quhpk1m2yejMakND1MEAn", host = "ec2-184-73-194-196.compute-1.amazonaws.com" , port = "5432")
        cur = conn.cursor()
        cur.execute("INSERT INTO newblogposts (title, body, day, time) VALUES (%s,%s,%s,%s)", [request.form['title'], request.form['body'], strftime("%d %b %Y ", gmtime()), strftime("%H:%M:%S ", gmtime())])
        conn.commit()
        conn.close()
        return redirect(url_for('posts'))
    else:
        return render_template('newposts.html', title = 'New Post')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port, debug = True)
