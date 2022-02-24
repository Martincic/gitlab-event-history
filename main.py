from tokenize import Token
from flask import Flask, render_template, request
from bin.Events import Event
import webbrowser
from bin.Token import Token
# import request
# import webview

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
  
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    event = Event()
    try:
        data = event.getData()
    except:
        return "You most likely did not set GitLab Personal access token! Please add token first. (todo: add some html/css here)"
    return render_template('index.html', events=data)

@app.route('/token', methods = ['POST', 'DELETE'])
def token():
    # Save token
    if request.method == 'POST':
        print('Received!!!')
        print(request.form['token'])
        Token.saveToken(request.form['token'])
        return 'Saved!'
        # data = request.form # a multidict containing POST data

    # Delete token
    if request.method == 'DELETE':
        Token.deleteToken()
        return 'Deleted!'

    
# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.

    # webview.create_window('Git History', 'http://127.0.0.1:5000/')
    # webview.start()
    webbrowser.open('http://127.0.0.1:5000/', new=2)
    app.run(debug=True)