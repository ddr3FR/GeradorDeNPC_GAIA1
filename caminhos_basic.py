import random

def sort_caminho_basic():
    lista_caminho_basico = ["Ladino", "Devoto", "Combatente", "Feiticeiro", "Andarilho"]
    basic_escolhida = random.choice(lista_caminho_basico)
    return basic_escolhida

def sort_graca(devoto_esc):
    lista_graca_devotoB = ["Graça de Dahaki", "Graça de Exatir", "Graça de Fif'nir", "Graça de Nívila", "Graça de Pris'ma", "Graça de Rakhantorr", "Graça de Setsuya"]
    lista_graca_devotoC = ["Graça de Aether", "Graça de Athranamad", "Graça de Gruneak", "Graça de Kalgoras", "Graça de Kyria", "Graça de Verkau", "Graça de Zalunea"]
    lista_graca_devotoO = ["Graça de Anatael", "Graça de Aysla", "Graça de Glimmera", "Graça de Koyona", "Graça de Laofeng", "Graça de Norduk", "Graça de Yachai"]

    if devoto_esc.lower() == "b":
        graca_escolido = random.choice(lista_graca_devotoB)
    elif devoto_esc.lower() == "c":
        graca_escolido = random.choice(lista_graca_devotoC)
    elif devoto_esc.lower() == "o":
        graca_escolido = random.choice(lista_graca_devotoO)
    return graca_escolido
