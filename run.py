from flask import Flask
import textComp

app = Flask(__name__)
@app.route('/')
def hello_world():
    texto1 = "No te sientas obligado a realizarme una donación, pero cada aportación me ayuda a mantener el sitio en activo para que continúe existiendo y me motiva a continuar creando nuevo contenido."
    texto2 = "No te sientas obligado a realizarme una aportación, pero cada donación me ayuda a mantener el sitio online para que continúe existiendo y me motiva a seguir haciendo nuevo contenido."

    return 'La similitud es de ' + str(textComp.calcular_similitud(texto1, texto2))