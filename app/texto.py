import re
import unicodedata

def removerCarateres(texto):
    texto = str(texto).lower()
    texto = unicodedata.normalize('NFKD',texto)
    return re.sub('[^a-z]','',texto)