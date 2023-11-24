import json, re
import pandas as pd 
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import ToktokTokenizer
from gensim.corpora import Dictionary
from gensim.models import LdaModel
import random
import numpy as np
import matplotlib.pyplot as plt
from gensim.matutils import jensen_shannon


def limpiar_texto(texto):
    """
    Función para realizar una limpieza de un texto dado.
    """
    # Eliminamos los caracteres especiales
    texto = re.sub(r'\W', ' ', str(texto))
    # Eliminado las palabras que tengo un solo caracter
    texto = re.sub(r'\s+[a-zA-Z]\s+', ' ', texto)
    # Sustituir los espacios en blanco en uno solo
    texto = re.sub(r'\s+', ' ', texto, flags=re.I)
    # Convertimos textos a minusculas
    texto = texto.lower()
    return texto


def filtrar_stopword_digitos(tokens):
    STOPWORDS = set(stopwords.words("spanish"))
    """
    Filtra stopwords y digitos de una lista de tokens.
    """
    return [token for token in tokens if token not in STOPWORDS and not token.isdigit()]


def stem_palabras(tokens):
    stemmer = SnowballStemmer("spanish")
    """
    Reduce cada palabra de una lista dada a su raíz.
    """
    return [stemmer.stem(token) for token in tokens]

def calcular_jensen_shannon_sim_doc_doc(doc_dist1, doc_dist2):
    """Calcula la distancia Jensen Shannon entre dos documentos.
    """
    return jensen_shannon(doc_dist1, doc_dist2)

def calcularGensim(jsonDatos, texto1):

    tuplas = list(zip([noticia.get("titulo") for noticia in jsonDatos],[noticia.get("letra") for noticia in jsonDatos]))
    df = pd.DataFrame(tuplas, columns =['titulo', 'letra'])
    print(df.shape)
    df.head()

    df["Tokens"] = df.letra.apply(limpiar_texto)
    print(df.Tokens[0])
    df.head()

    tokenizer = ToktokTokenizer() 
    df["Tokens"] = df.Tokens.apply(tokenizer.tokenize)
    print(df.Tokens[0])
    df.head()


    df["Tokens"] = df.Tokens.apply(filtrar_stopword_digitos)
    df.head()

    df["Tokens"] = df.Tokens.apply(stem_palabras)


    diccionario = Dictionary(df.Tokens)
    print(f'Número de tokens: {len(diccionario)}')

    #diccionario.filter_extremes(no_below=2, no_above = 0.8)
    #print(f'Número de tokens: {len(diccionario)}')

    corpus = [diccionario.doc2bow(noticia) for noticia in df.Tokens]

    print(corpus)

    lda = LdaModel(corpus=corpus, id2word=diccionario, num_topics=50, random_state=42, 
               chunksize=1000, passes=10, alpha='auto')

    topicos = lda.print_topics(num_words=5, num_topics=20)
    for topico in topicos:
        print(topico)

    #for i in range(1, 5):
    #    plt.figure()
    #    plt.imshow(WordCloud(background_color='white', prefer_horizontal=1.0).fit_words(dict(lda.show_topic(i, 20))))
    #    plt.axis("off")
    #    plt.title("Tópico " + str(i))
    #    plt.show()

    articulo_nuevo = texto1
    articulo_nuevo = limpiar_texto(articulo_nuevo)
    articulo_nuevo = tokenizer.tokenize(articulo_nuevo)
    articulo_nuevo = filtrar_stopword_digitos(articulo_nuevo)
    articulo_nuevo = stem_palabras(articulo_nuevo)

    bow_articulo_nuevo = diccionario.doc2bow(articulo_nuevo)

    # Indices de los topicos mas significativos
    dist_indices = [topico[0] for topico in lda[bow_articulo_nuevo]]
    # Contribucion de los topicos mas significativos
    dist_contrib = [topico[1] for topico in lda[bow_articulo_nuevo]]

    #distribucion_topicos = pd.DataFrame({'Topico':dist_indices,'Contribucion':dist_contrib })
    #distribucion_topicos.sort_values('Contribucion', ascending=False, inplace=True)
    #ax = distribucion_topicos.plot.bar(y='Contribucion',x='Topico', rot=0, color="green",
    #                                title = "Tópicos más importantes para documento nuevo")

    #for ind, topico in distribucion_topicos.iterrows():
    #    print("*** Tópico: " + str(int(topico.Topico)) + " ***")
    #    palabras = [palabra[0] for palabra in lda.show_topic(topicid=int(topico.Topico))]
    #    palabras = ', '.join(palabras)
    #    print(palabras, "\n")

    lda.save("articulos.model")
    diccionario.save("articulos.dictionary")

    distribucion_noticia = lda.get_document_topics(bow_articulo_nuevo, 
                                               minimum_probability=0)



    """Muestra las n noticias mas similares a partir 
       de una distribucion de tópicos.
    """
    distancias = [calcular_jensen_shannon_sim_doc_doc(
        distribucion_noticia, lda[noticia]) for noticia in corpus]
    mas_similares = np.argsort(distancias)

    resultado = {}
    for i in range(0,2):
        titular = df.iloc[int(mas_similares[i])].titulo
        print(f'{i + 1}: {titular} ({distancias[mas_similares[i]]})')
        resultado[i] = f'{titular} ({distancias[mas_similares[i]]})'

    return resultado

    
