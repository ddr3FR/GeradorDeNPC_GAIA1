import random

def escolhaCam(opc):
    lista_caminho_basico = ["Ladino", "Devoto", "Combatente", "Feiticeiro", "Andarilho"]
    if opc == "Ladino":
        especializa = str("Qual especialização de Ladino vc deseja seguir(Digite a letra antes da especialização para escolhe): A - Assasino, B - Atirador, C - Duelista, D - Sombra, E - Trapaceiro ").lower()
        while especializa not in ["a", "b", "c", "d", "e"]:
            especializa = str(input("Digite uma Especialização Validar:  A - Assasino, B - Atirador, C - Duelista, D - Sombra, E - Trapaceiro  ")).lower()
            if especializa == "a" or especializa == "c" or especializa == "b" or especializa == "d" or especializa == "e": 
                break
        match especializa:
            case "a":
                


def hab_Andarilho():
    habilits_andarilho = ["COMPANHEIRO FERAL", "DESCENDENTE DOS FILHOS DA FLORESTA", "CONVOCAR AS CALAMIDADES", "FORÇAS DO CICLO", "ENFEITIÇAR", "GRILHÕES PRIMAIS", "EXPLORADOR DE AURORIA", "INVÓLUCRO CINZENTO","DECRETO LUNAR", "TÉCNICA MUSICAL"]
    habilits_andarilhoultilit = ["COMPANHEIRO FERAL", "DESCENDENTE DOS FILHOS DA FLORESTA", "CONVOCAR AS CALAMIDADES",]
    habilits_andarilhoEsp = ["ENFEITIÇAR", "EXPLORADOR DE AURORIA", "INVÓLUCRO CINZENTO", "DECRETO LUNAR", "TÉCNICA MUSICAL"]
    habilits_andarilhoVig = ["GRILHÕES PRIMAIS", "EXPLORADOR DE AURORIA"]
    habilits_andarilhoCan = ["FORÇAS DO CICLO"] 

    habilits_andarilhoParaBardo = ["TÉCNICA MUSICAL", "ENFEITIÇAR"]
    habilits_andarilhoParacacador = ["COMPANHEIRO FERAL", "EXPLORADOR DE AURORIA"]
    habilits_andarilhoParaDruida = ["DESCENDENTE DOS FILHOS DA FLORESTA", "DECRETO LUNAR"]
    habilits_andarilhoParaEmissario = ["FORÇAS DO CICLO", "GRILHÕES PRIMAIS"]
    habilits_andarilhoParaRitualista = ["CONVOCAR AS CALAMIDADES", "INVÓLUCRO CINZENTO"]


def hab_Combatente():
    habilits_Combatente = ["ATAQUE ENERGIZADO", "CALOR DA BATALHA", "DISCÍPULO DO CORPO E MENTE", "ENSINAMENTOS DO TEMPLO CINZENTO", "PERITO COM ARMAMENTOS CORPO A CORPO", "PERSEGUIDOR DO VÉU", "PUNIÇÃO ESCARLATE", "TÉCNICAS MARCIAIS", "DESCANSO", "PERITO COM EQUIPAMENTOS DEFENSIVOS"]
    habilits_CombatenteParaArtMarcial = ["DISCÍPULO DO CORPO E MENTE", "TÉCNICAS MARCIAIS"]
    habilits_CombatenteParaGuardiao = ["DESCANSO", "PERITO COM EQUIPAMENTOS DEFENSIVOS"]
    habilits_CombatenteParaInquisidor = ["PERSEGUIDOR DO VÉU", "PUNIÇÃO ESCARLATE"]
    habilits_CombatenteParaLegioMistico = ["ATAQUE ENERGIZADO", "ENSINAMENTOS DO TEMPLO CINZENTO"]
    habilits_CombatenteParaSoberano = ["CALOR DA BATALHA", "PERITO COM ARMAMENTOS CORPO A CORPO"]

def hab_Devoto():
    habilits_Devoto = ["FRAGMENTO ABISSAL", "LAMPEJO CELESTIAL", "BARREIRA DE LUZ", "ASPECTO DA GRANDEZA", "CENTELHAS DE ÉDONA", "CONSAGRAR", "REVITALIZAR", "ELO ESPIRITUAL", "PODER SOMBRIO", "SANTUÁRIO"]
    habilits_DevotoParaAvata = ["CENTELHAS DE ÉDONA", "SANTUÁRIO"]
    habilits_DevotoParaEspiritualista = ["ASPECTO DA GRANDEZA", "ELO ESPIRITUAL"]
    habilits_DevotoParaOculto = ["FRAGMENTO ABISSAL", "PODER SOMBRIO"]
    habilits_DevotoParaPaladino = ["LAMPEJO CELESTIAL", "BARREIRA DE LUZ"]
    habilits_DevotoParaSacerdote = ["CONSAGRAR", "REVITALIZAR"]

def hab_Feiticeiro():
    habilit_Feiticeiro = ["DESPERTAR ARCANO", "ABERRAÇÃO DE SANGUE", "MOLDAR ELEMENTO", "ESFERA ESPIRAL SOBERANA", "PERITO COM ARMAMENTOS MÁGICOS", "ARMADURA ARCANA", "FEITIÇARIA", "MANIPULAR A FENDA", "VELOCIDADE MÍSTICA", "RITUAIS SANGRENTOS", "TOQUE DO VÉU"]
    habilit_FeiticeiroParaArcanista = ["ARMADURA ARCANA", "FEITIÇARIA"]
    habilit_FeiticeiroParaArtifice = ["PERITO COM ARMAMENTOS MÁGICOS", "TOQUE DO VÉU"]
    habilit_FeiticeiroParaElementalista = ["ESFERA ESPIRAL SOBERANA", "MOLDAR ELEMENTO"]
    habilit_FeiticeiroParaFianDeSangue = ["ABERRAÇÃO DE SANGUE", "RITUAIS SANGRENTOS"]
    habilit_FeiticeiroParaRegulador = ["MANIPULAR A FENDA", "VELOCIDADE MÍSTICA"]

def hab_Ladino():
    habilit_Ladino = ["ARMADILHAS MÍSTICAS", "DISPARO DEBILITANTE", "EMBOSCADA", "ESTILO HÍBRIDO", "LADINAGEM", "PERITO COM ARMAMENTOS À DISTÂNCIA", "REVIDAR", "MANTO DAS SOMBRAS", "REFLEXO ENGANADOR", "MARCA SOMBRIA"]
    habilit_LadinoParaAssassino = ["EMBOSCADA", "LADINAGEM"]
    habilit_LadinoParaAtirador = ["DISPARO DEBILITANTE", "PERITO COM ARMAMENTOS À DISTÂNCIA"]
    habilit_LadinoParaDuelista = ["REVIDAR", "ESTILO HÍBRIDO"]
    habilit_LadinoParaSombra = ["MANTO DAS SOMBRAS", "MARCA SOMBRIA"]
    habilit_LadinoParaTrapaceiro = ["ARMADILHAS MÍSTICAS", "REFLEXO ENGANADOR"]
