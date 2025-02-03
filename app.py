from flask import Flask, request, render_template
from services.predict import predict

app = Flask(__name__, template_folder='templates')

@app.route('/')   # Decorator
def home():
    return render_template('index.html')

@app.route('/predict')
def prd():
    return predict()

@app.route('/form')
def form():  
    name="said"
    liste = [10,20,30,40]
    return render_template('diagnoses-form.html',name=name,liste=liste)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)   # debug turns to False in production (deployment)
