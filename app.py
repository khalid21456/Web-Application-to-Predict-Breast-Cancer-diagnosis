from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')
# from jinja2 import Environment, FileSystemLoader

# # Specify the templates directory
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)

# # Load a template
# template = env.get_template('index.html')

# # Define the context
# context = {
#     'title': 'My Website',
#     'header': 'Welcome to My Website',
#     'content': 'This is a sample content rendered by Jinja2.'
# }
@app.route('/')   # Decorator
def home():
    return render_template('index.html')

@app.route('/greet/<name>',methods=['GET'])
def greeting(name):
    return f"{request.method}"

#Url Parameters
@app.route('/add/<int:number1>/<int:number2>')
def add(number1,number2):
    return f'{number1} + {number2} = {number1+number2}'

@app.route("/params")
def handle_params():
    greeting = request.args["greeting"]
    name = request.args.get("name")
    return f'{greeting} {name}'


@app.route("/employ")
def employees():
    name = request.args["name"]
    

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=1111,debug=True)   # debug turns to False in production (deployment)

# I can also specify the port number by adding port=5000 in app.run() method