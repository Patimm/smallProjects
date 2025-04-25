from flask import Flask,render_template
from datetime import datetime  # import datetime module
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index")
def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # get current time
    return render_template('index.html', current_time=current_time)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__=="__main__":
    app.run(debug=True)