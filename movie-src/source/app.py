# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') 
def index():
  return render_template('index.html')

@app.route('/index.html')
def index2():
  return render_template('index.html')

@app.route('/about.html')
def index3():
  return render_template('about.html')

@app.route('/upload.html')
def index4():
  return render_template('upload.html')

if __name__=="__main__":
  app.run(host="0.0.0.0", port="5000", debug=True)
