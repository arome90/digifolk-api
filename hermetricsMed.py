from hermetrics import *

def hermetricsLevenstein(texto1, texto2):
    lev = Levenshtein()
    return lev.distance(texto1, texto2)


def hermetricsComp(texto1, texto2):
    mc = MetricComparator()
    return mc.similarity(texto1, texto2)