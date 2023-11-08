from flask import Flask, render_template, request, redirect, url_for
import textComp 
import LevenshteinDistances
import hermetricsMed
import json

app = Flask(__name__)
@app.route('/api/textos/', methods=["GET", "POST"])
def getInformationAndProcess():

    if request.method == 'GET':
        return 'Esto es la api de Digifolk! Por favor, elige la opción y manda la información correcta'
    if request.method == 'POST':
        contentJson = request.json
        titulo1 = str(contentJson['Mexico'][0])
        response = {}

        response["TextSimilarity"] = textComp.calcular_similitud(contentJson['Mexico'][0]['letra'], contentJson['Mexico'][1]['letra'])
        response["levenshteinCustom"] = LevenshteinDistances.levenshteinDistanceDP(contentJson['Mexico'][0]['letra'], contentJson['Mexico'][1]['letra'])
        response["levenshteinHermetrics"] = hermetricsMed.hermetricsLevenstein(contentJson['Mexico'][0]['letra'], contentJson['Mexico'][1]['letra'])
        response["comparativaHermetrics"] = hermetricsMed.hermetricsComp(contentJson['Mexico'][0]['letra'], contentJson['Mexico'][1]['letra'])

        
        return response    

@app.route('/')
def getBasicInformation():

    if request.method == 'GET':
        return 'Esto es el servidor de Digifolk!'