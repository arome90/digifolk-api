from flask import Flask, render_template, request, redirect, url_for
import textComp 
import LevenshteinDistances
import hermetricsMed
import SemanticTextSimilarity
import TopicModelingGensim2

app = Flask(__name__)
@app.route('/api/textos/', methods=["GET", "POST"])
def getInformationAndProcess():

    if request.method == 'GET':
        return 'Esto es la api de Digifolk! Por favor, elige la opción y manda la información correcta'
    if request.method == 'POST':
        contentJson = request.json
        titulo1 = str(contentJson[0]["Obra"])
        titulo2 = str(contentJson[1]["Obra"])
        response = {}
        response["1-comparacion"] = titulo1 + "-" + titulo2
        response["TextSimilarity"] = textComp.calcular_similitud(contentJson[0]['Letra concatenada'], contentJson[1]['Letra concatenada'])
        response["levenshteinCustom"] = LevenshteinDistances.levenshteinDistanceDP(contentJson[0]['Letra concatenada'], contentJson[1]['Letra concatenada'])
        response["levenshteinHermetrics"] = hermetricsMed.hermetricsLevenstein(contentJson[0]['Letra concatenada'], contentJson[1]['Letra concatenada'])
        response["comparativaHermetrics"] = hermetricsMed.hermetricsComp(contentJson[0]['Letra concatenada'], contentJson[1]['Letra concatenada'])
        response["SemanticTextSimilarity"] = SemanticTextSimilarity.predictionComparision(contentJson[0]['Letra concatenada'], contentJson[1]['Letra concatenada'])
        #response["SimilarityCheck"] = SimilarityCheckMed.similarityChecker(contentJson[0]['Letra concatenada'], contentJson[1]['Letra concatenada'])
        #response["JensenShanon2"] = TopicModelingGensim2.calcularGensim(contentJson, contentJson[0]['Letra concatenada'])
        return response    

@app.route('/')
def getBasicInformation():

    if request.method == 'GET':
        return 'Esto es el servidor de Digifolk!'