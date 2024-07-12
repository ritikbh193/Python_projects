from flask import Flask,render_template

app = Flask(__name__)

# @app.route('/')
# def run():
#     return 'Hello Ritik How are you where are you working currently ? is there anay why to connect you'

@app.route('/')
def run():
    return render_template('mylearn.html')


app.run(debug=True)