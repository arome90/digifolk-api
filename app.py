from flask import Flask, render_template, request, redirect, url_for
import textComp

app = Flask(__name__)
@app.route('/api/textos/', methods=["GET", "POST"])
def getInformationAndProcess():
    contentJson = request.json
    titulo1 = str(contentJson['Mexico'][0])
    response = ''
    #for field_dict in contentJson['Mexico']:
    #    str(textComp.calcular_similitud(field_dict, field_dict))
    #return str(titulo1)
    return 'Numero de elementos ' + str(len(contentJson['Mexico'])) + ' La similitud entre ' + str(contentJson['Mexico'][0]['titulo']) + ' y ' +str(contentJson['Mexico'][1]['titulo']) + ' es de ' + str(textComp.calcular_similitud(contentJson['Mexico'][0]['letra'], contentJson['Mexico'][1]['letra']))