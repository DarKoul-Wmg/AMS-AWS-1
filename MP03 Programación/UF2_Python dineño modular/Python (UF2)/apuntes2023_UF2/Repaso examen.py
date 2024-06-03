# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# —————————————————————————————————————————— FUNCIONS: PARÀMETRES ARBITRARIS ———————————————————————————————————————————
# —————————————————————————————————————————————————————————————————————————————————————————————— PARÀMETRES PER OMISSIÓ.
"""
def saludar(nom, missatge="Benvingut,"):
    print(missatge, nom)


saludar("Pöl.")
"""

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ——————————————————————————————————————————————————————————————————————————————————————————— KEYWORDS COM A PARÀMETRES.
"""
def saludar(nom, missatge="Benvingut,"):
    print(missatge, nom)


saludar(nom="Pöl.", missatge="Hola,")


def saludar(nom, missatge="Benvingut,"):
    print(missatge, nom)


saludar(missatge="Hola,", nom="Pöl.")
"""

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# ——————————————————————————————————————————————————————————————————————————————————————————————— PARÀMETRES ARBITRARIS.
"""
def recorrer_parametres_arbitraris(parametre_fixe, *arbitraris):
    print(parametre_fixe)
    for argument in arbitraris:
        print(argument)


recorrer_parametres_arbitraris("Valor 1", "Valor 2", "Valor 3", "Valor 4")
"""

""" En Python, el uso de asteriscos (* y **) se utiliza para manejar parámetros variables en funciones.
Un solo asterisco (*) se utiliza para recoger argumentos posicionales adicionales en una tupla.
Dos asteriscos (**) se utilizan para recoger argumentos de palabra clave adicionales en un diccionario.
    *arbitraris recoge cualquier número de argumentos posicionales adicionales después del parámetro fijo parametre_fixe
    en una tupla llamada arbitraris.
    
    **kwords recoge cualquier número de argumentos de palabra clave adicionales en un diccionario llamado kwords.

Por lo tanto, cuando llamas a la función recorrer_parametres_arbitraris con los argumentos "arbitrari 1", "arbitrari 2",
"arbitrari 3", estos se recogen en la tupla arbitraris. Y como no hay argumentos de palabra clave adicionales, el
diccionario kwords estará vacío."""


def recorrer_parametres_arbitraris(parametre_fixe, *arbitraris, **kwords):
    print(parametre_fixe)
    for argument in arbitraris:
        print(argument)
    for clau in kwords:
        print("El valor de", clau, "es", kwords[clau])


recorrer_parametres_arbitraris("Fixed", "arbitrari 1", "arbitrari 2", "arbitrari 3")
