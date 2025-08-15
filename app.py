from flask import Flask, render_template, url_for, request
import sqlite3
import os
from VIDEO import Recognition
from LIVE import LiveRecognition

connection = sqlite3.connect('user_data.db')
cursor = connection.cursor()

command = """CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, mobile TEXT, email TEXT)"""
cursor.execute(command)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('Video.html')

@app.route('/userlog', methods=['GET', 'POST'])
def userlog():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']

        query = "SELECT name, password FROM user WHERE name = '"+name+"' AND password= '"+password+"'"
        cursor.execute(query)

        result = cursor.fetchall()

        if len(result) == 0:
            return render_template('index.html', msg='Sorry, Incorrect Credentials Provided,  Try Again')
        else:
            return render_template('Video.html')

    return render_template('index.html')


@app.route('/userreg', methods=['GET', 'POST'])
def userreg():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']
        mobile = request.form['phone']
        email = request.form['email']
        
        print(name, mobile, email, password)

        command = """CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, mobile TEXT, email TEXT)"""
        cursor.execute(command)

        cursor.execute("INSERT INTO user VALUES ('"+name+"', '"+password+"', '"+mobile+"', '"+email+"')")
        connection.commit()

        return render_template('index.html', msg='Successfully Registered')
    
    return render_template('index.html')

@app.route('/detectvideo', methods=['GET', 'POST'])
def detectvideo():
    if request.method == 'POST':
        source = request.form['src']
        query = request.form['query']
        Recognition(source, query)

        return render_template('Video.html', query=query, inputvideo='static/inputvideo/'+source, outputvideo='static/outputvideo/'+source)
    return render_template('Video.html')

@app.route('/detectlive', methods=['GET', 'POST'])
def detectlive():
    if request.method == 'POST':
        query = request.form['query']
        LiveRecognition(query)

        return render_template('Live.html', query=query, outputvideo='static/outputvideo/1.mp4')
    return render_template('Live.html')


@app.route('/viewframes')
def viewframes():
    unique_frames = []
    for img in os.listdir('static/unique'):
        unique_frames.append('http://127.0.0.1:5000/static/unique/'+img)
    common_frames = []
    for img in os.listdir('static/common'):
        common_frames.append('http://127.0.0.1:5000/static/unique/'+img)
    return render_template('viewframes.html', common_frames=common_frames, unique_frames=unique_frames)

@app.route('/logout')
def logout():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
