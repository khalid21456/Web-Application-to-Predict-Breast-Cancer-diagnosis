from flask import Flask, request, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')   # Decorator
def home():
    return render_template('index.html')
 

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)   # debug turns to False in production (deployment)
