from semantic_text_similarity.models import WebBertSimilarity
from semantic_text_similarity.models import ClinicalBertSimilarity

#Maps batches of sentence pairs to real-valued scores in the range [0,5]

def predictionComparision(text1, text2):
    web_model = WebBertSimilarity(device='cpu', batch_size=10) #defaults to GPU prediction
    clinical_model = ClinicalBertSimilarity(device='cpu', batch_size=10) #defaults to GPU prediction
    response  = {}
    response["WEB_MODEL"] = float(str(web_model.predict([(text1,text2)]))[1:-1])
    response["CLINICAL_MODEL"] = float(str(clinical_model.predict([(text1,text2)]))[1:-1])
    return response

