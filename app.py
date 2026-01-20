from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/hola')
def hola():
    return "Hello, Hola"

@app.route("/user/<string:user>")
def user(user):
    return f"Hello, {user}!"

@app.route("/numero/<int:n>")
def numero(n):
    return f"El numero es: {n}"

@app.route("/user/<int:n>/<string:username>")
def username(id,username):
    return f"<h1>!Hola, {username}! Tu ID es: {id}</h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"<h1>La suma es: {n1+n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:parm>")
def fun(param="juan"):
    return f"<h1>¡Hola, {param}!</h1>"

@app.route("/operas")
def operas():
    return '''
        <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="name">apaterno:</label>
        <input type="text" id="name" name="name" required>
        </form>
    '''

if __name__ == '__main__':
    app.run()