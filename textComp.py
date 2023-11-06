from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import sys

def calcular_similitud(texto1, texto2):
    # Preprocesamiento de los textos
    
    stop_words = set(stopwords.words("spanish"))
    lemmatizer = WordNetLemmatizer()
    tokens1 = [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(texto1) if word.isalnum() and word.lower() not in stop_words]
    tokens2 = [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(texto2) if word.isalnum() and word.lower() not in stop_words]

    # Unión de los tokens preprocesados en textos nuevamente
    texto_preprocesado1 = ' '.join(tokens1)
    texto_preprocesado2 = ' '.join(tokens2)

    # Creación del vectorizador TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([texto_preprocesado1, texto_preprocesado2])

    # Cálculo de la similitud de coseno entre los vectores TF-IDF
    similitud = (tfidf_matrix * tfidf_matrix.T).toarray()[0, 1]

    return similitud


