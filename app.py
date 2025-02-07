from flask import Flask, request, render_template # type: ignore
from services.predict import predict
from models.person import Person
import os

app = Flask(__name__, template_folder='templates')
static_dir = os.path.join(app.root_path, 'static')

person = Person("","","","","")

@app.route('/')   # Decorator
def home():
    return render_template('index.html')

@app.route('/predict')
def prd():
    return predict()

@app.route('/form', methods=["GET","POST"])
def form():  
    if(request.method == "GET"):
        return render_template('diagnoses-form.html')
    else :
        person.fname = request.form.get("fname")
        person.lname = request.form.get("lname")
        person.email = request.form.get("email")
        person.address = request.form.get("address")
        person.phone = request.form.get("phone")
        print(person)
        return ""

@app.route('/form/form2',methods=["GET","POST"])
def form2():
    return render_template('diagnoses-form2.html')

@app.route('/base')
def base():
    name = "khalid edaoudi"
    return render_template('base.html',name=name)

@app.route('/index')
def index():
    return render_template('index2.html')

@app.template_filter("/reverse")
def reverse_string(str):
    return str[::-1]

@app.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files["file"]
    if file.content_type == "text/plain":
        file_path = os.path.join(static_dir, file.filename)
        file.save(file_path)
    return 'frf'


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)   # debug turns to False in production (deployment)
