from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

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


texto1 = "No te sientas obligado a realizarme una donación, pero cada aportación me ayuda a mantener el sitio en activo para que continúe existiendo y me motiva a continuar creando nuevo contenido."
texto2 = "No te sientas obligado a realizarme una aportación, pero cada donación me ayuda a mantener el sitio online para que continúe existiendo y me motiva a seguir haciendo nuevo contenido."

similitud = calcular_similitud(texto1, texto2)
print("La similitud entre los textos es:", similitud)