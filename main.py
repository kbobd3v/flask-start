from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap

# to run a Flask application, export envs FLASK_APP, FLASK_DEBUG and FLASK_ENV

# The first declaration is the app which use the class Flask with its name
app = Flask(__name__)
# to use flask bootstrap templates first install it and run a instance of boostrap like this:
bootstrap = Bootstrap(app)



# create a variable to iterate through it
todos = ['Estudiar Flask', 'Terminar las garantias', 'Hacer ejercicio']


# Use the python decorator with the function route which defines the directory of our app
@app.route('/')
def index():
    # Here use remote_addr attribute request variable to know what's the ip address of the user who visits our app
    user_ip = request.remote_addr
    # Create our response with make_response from the app when the user makes a request and he'll be redirected to out hello function
    response = make_response(redirect('/hello'))
    # then we ask response to set a cookie with the 'user_ip' key and the user_ip variable
    response.set_cookie('user_ip', user_ip)
    # And return the response redirecting the user to our hello function
    return response


@app.route('/hello')
def hello():
    # We take the value of the key 'user_ip' from the cookie we just created and assign it to the user_ip variable
    user_ip = request.cookies.get('user_ip')
    # we can create a dictionary with the params we want to pass to the html render
    context = {
        'user_ip': user_ip,
        'todos': todos,
    }
    # Here we use render_template to render our html with the possibility of using python o flask variables within the html file
    # The function render_template takes html file as parameter and the variables you want to be within the render of the html file
    # Also we pass the dictionary as **kwargs, now the html render can expand our dictionary values
    # so you don't need to reference each value for instance 'context.todos'
    return render_template('hello.html', **context)

    # we can use this variable to return a string with the data
    # return f'Hello World Flask, you\'re visiting us from {user_ip}'

@app.route('/buenas')
def buenas():
    return 'Bueeeeenas!'

# Using the app decorator we can define how to manage error message
# In this case we use the '404 not found' error, we use it as parameter
# and render the html template with the error data we want to show
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)