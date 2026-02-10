from wtforms.fields import core
from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
import forms

app = Flask(__name__)
app.secret_key="clave secreta"
csrf=CSRFProtect()

@app.route('/index')
def index():
    titulo="IDGS803-Flask"
    lista=['Pedro','mario','juan']
    return render_template("index.html",titulo=titulo, lista=lista)

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/usuario",methods=["GET", "POST"])
def usuario():
    mat=0
    nom=""
    apa=""
    ama=""
    correo=""
    usuario_class=forms.UserForm(request.form)
    if request.method=='POST' and usuario_class.validate():
        mat=usuario_class.matricula.data
        nom=usuario_class.nombre.data
        apa=usuario_class.apaterno.data
        ama=usuario_class.amaterno.data
        correo=usuario_class.email.data

    return render_template("usuario.html",form=usuario_class,mat=mat,nom=nom,apa=apa,ama=ama,correo=correo)

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

@app.route("/operaBas", methods=["GET", "POST"])
def operas1():

    resultado=0
    if request.method == "POST":
        n1 = float(request.form.get("n1"))
        n2 = float(request.form.get("n2"))
        operacion = request.form.get("operacion")
        if operacion == "suma":
            resultado = n1 + n2
            op = "suma"
        
        elif operacion == "resta":
            resultado = n1 - n2
            op = "resta"
        
        elif operacion == "multiplicacion":
            resultado = n1 * n2
            op = "multiplicación"
        
        elif operacion == "division":
            if n2 == 0:
                return "<h1>Error: No se puede dividir entre 0</h1>"
            resultado = n1 / n2
            op = "división"

    return render_template("operaBas.html",resultado=resultado)

@app.route("/cinepolis", methods=["GET", "POST"])
def cinepolis():
    nombre = ""
    cantiCompradores = 0
    tarjCineco = ""
    cantiBoletos = 0
    Total = 0
    
    cinepolis_class = forms.CinepolisForm()
    
    if cinepolis_class.validate_on_submit():
        nombre = cinepolis_class.nombre.data
        cantiCompradores = cinepolis_class.compradores.data
        tarjCineco = cinepolis_class.cineco.data
        cantiBoletos = cinepolis_class.boletos.data
        limit = cantiCompradores * 7
        
        if cantiBoletos <= limit:
            Total = cantiBoletos * 12
            if 3 <= cantiBoletos <= 5:
                Total *= 0.90
            if cantiBoletos > 5:
                Total *= 0.85
            if tarjCineco == "si":
                Total *= 0.90
        else:
            Total = 0
            alert = "Solo se permiten 7 boletos por comprador"
            flash(alert)
    
    return render_template("ventas_boletos.html", form=cinepolis_class, nombre=nombre, cantiCompradores=cantiCompradores, tarjCineco=tarjCineco, cantiBoletos=cantiBoletos, Total=Total)


if __name__ == '__main__':
    csrf.init_app(app)
    app.run()