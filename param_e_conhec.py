import random

def distrib_andarilho(pts_pda):
    # Inicializar todos os atributos com 0
    precisao = 0
    canalizacao = 0
    arcanismo = 0
    espirito = 0
    vigor = 0
    pts_total = 7
    # Lista dos atributos para distribuição
    melhorParaAnda = ["Precisao", "Canalizacao", "Arcanismo", "Espirito", "Vigor"]
    # Inicializar o limite máximo de pontos que podem ser distribuídos para cada atributo
    max_pontos_por_atributo = 2
    
    # Ajustar a quantidade de pontos iniciais
    if pts_pda == (1,2):
        pts_total = 7
        while pts_total > 0:
            l = random.choice(melhorParaAnda)
            if l == "Precisao" and precisao < max_pontos_por_atributo:
                precisao += 1
            elif l == "Canalizacao" and canalizacao < max_pontos_por_atributo:
                canalizacao += 1
            elif l == "Arcanismo" and arcanismo < max_pontos_por_atributo:
                arcanismo += 1
            elif l == "Espirito" and espirito < max_pontos_por_atributo:
                espirito += 1
            elif l == "Vigor" and vigor < max_pontos_por_atributo:
                vigor += 1
            else:
                continue  # Repetir a escolha se o atributo já atingiu o máximo permitido

        pts_total -= 1
    else:
        # Calcular pontos extras baseados na quantidade de pontos
        if pts_pda >= 3 and pts_pda <= 5:
            pontos_adicionais = 1
        elif pts_pda >= 6 and pts_pda <= 8:
            pontos_adicionais = 2
        elif pts_pda == 9:
            pontos_adicionais = 3
        else:
            pontos_adicionais = 0
        
        if pts_pda > 9:
            pontos_adicionais += (((pts_pda - 9) / 2 ) * 2) + 4
        
        pts_total += pontos_adicionais
    
        while pts_total > 0:
            l = random.choice(melhorParaAnda)
            if l == "Precisao":
                precisao += 1
            elif l == "Canalizacao":
                canalizacao += 1
            elif l == "Arcanismo":
                arcanismo += 1
            elif l == "Espirito":
                espirito += 1
            elif l == "Vigor":
                vigor += 1
            else:
                continue  # Repetir a escolha se o atributo já atingiu o máximo permitido

            pts_total -= 1

        return precisao, canalizacao, arcanismo, espirito, vigor
    
def distrib_combatente(pts_pda):
    # Inicializar todos os atributos com 0
    precisao = 0
    brutalidade = 0
    destreza = 0
    vigor = 0
    agilidade = 0
    arcanismo = 0
    pts_total = 7
    # Lista dos atributos para distribuição
    melhorParaComtb = ["Precisao", "Brutalidade", "Arcanismo", "Destreza", "Vigor", "Agilidade"]
    # Inicializar o limite máximo de pontos que podem ser distribuídos para cada atributo
    max_pontos_por_atributo = 2
    
    # Ajustar a quantidade de pontos iniciais
    if pts_pda == (1,2):
        pts_total = 7
        while pts_total > 0:
            l = random.choice(melhorParaComtb)
            if l == "Precisao" and precisao < max_pontos_por_atributo:
                precisao += 1
            elif l == "Brutalidade" and brutalidade < max_pontos_por_atributo:
                brutalidade += 1
            elif l == "Arcanismo" and arcanismo < max_pontos_por_atributo:
                arcanismo += 1
            elif l == "Destreza" and destreza < max_pontos_por_atributo:
                espirito += 1
            elif l == "Vigor" and vigor < max_pontos_por_atributo:
                vigor += 1
            elif l == "Agilidade" and agilidade < max_pontos_por_atributo:
                agilidade +=1
            else:
                continue  # Repetir a escolha se o atributo já atingiu o máximo permitido

        pts_total -= 1
    else:
        # Calcular pontos extras baseados na quantidade de pontos
        if pts_pda >= 3 and pts_pda <= 5:
            pontos_adicionais = 1
        elif pts_pda >= 6 and pts_pda <= 8:
            pontos_adicionais = 2
        elif pts_pda == 9:
            pontos_adicionais = 3
        else:
            pontos_adicionais = 0
        
        if pts_pda > 9:
            pontos_adicionais += (((pts_pda - 9) / 2 ) * 2) + 4
        
        pts_total += pontos_adicionais
    
        while pts_total > 0:
            l = random.choice(melhorParaComtb)
            if l == "Precisao":
                precisao += 1
            elif l == "Brutalidade":
                brutalidade += 1
            elif l == "Arcanismo":
                arcanismo += 1
            elif l == "Destreza":
                destreza += 1
            elif l == "Vigor":
                vigor += 1
            elif l == "Agilidade":
                agilidade +=1
            else:
                continue  # Repetir a escolha se o atributo já atingiu o máximo permitido

            pts_total -= 1

        return precisao, brutalidade, arcanismo, destreza, vigor, agilidade
def distrib_devoto(pts_pda):
    # Inicializar todos os atributos com 0
   
    canalizacao = 0
    espirito = 0
    vigor = 0
    precisao = 0
    pts_total = 7
    # Lista dos atributos para distribuição
    melhorParaDevoto = ["Precisao", "Canalizacao", "Espirito", "Vigor"]
    # Inicializar o limite máximo de pontos que podem ser distribuídos para cada atributo
    max_pontos_por_atributo = 2
    
    # Ajustar a quantidade de pontos iniciais
    if pts_pda == (1,2):
        pts_total = 7
        while pts_total > 0:
            l = random.choice(melhorParaDevoto)
            if l == "Precisao" and precisao < max_pontos_por_atributo:
                precisao += 1
            elif l == "Canalizacao" and canalizacao < max_pontos_por_atributo:
                canalizacao += 1
            elif l == "Espirito" and espirito < max_pontos_por_atributo:
                espirito += 1
            elif l == "Vigor" and vigor < max_pontos_por_atributo:
                vigor += 1
            else:
                continue  # Repetir a escolha se o atributo já atingiu o máximo permitido

        pts_total -= 1
    else:
        # Calcular pontos extras baseados na quantidade de pontos
        if pts_pda >= 3 and pts_pda <= 5:
            pontos_adicionais = 1
        elif pts_pda >= 6 and pts_pda <= 8:
            pontos_adicionais = 2
        elif pts_pda == 9:
            pontos_adicionais = 3
        else:
            pontos_adicionais = 0
        
        if pts_pda > 9:
            pontos_adicionais += (((pts_pda - 9) / 2 ) * 2) + 4
        
        pts_total += pontos_adicionais
    
        while pts_total > 0:
            l = random.choice(melhorParaDevoto)
            if l == "Precisao":
                precisao += 1
            elif l == "Canalizacao":
                canalizacao += 1
            elif l == "Espirito":
                espirito += 1
            elif l == "Vigor":
                vigor += 1
            else:
                continue  # Repetir a escolha se o atributo já atingiu o máximo permitido

            pts_total -= 1

        return precisao, canalizacao, espirito, vigor

def distrib_feiticeiro(pts_pda):
    # Inicializar todos os atributos com 0
    arcanismo = 0
    canalizacao = 0
    vigor = 0
    pts_total = 7
    # Lista dos atributos para distribuição
    melhorParaFeitc = ["Canalizacao", "Arcanismo", "Vigor"]
    # Inicializar o limite máximo de pontos que podem ser distribuídos para cada atributo
    max_pontos_por_atributo = 2
    
    # Ajustar a quantidade de pontos iniciais
    if pts_pda == (1,2):
        pts_total = 7
        while pts_total > 0:
            l = random.choice(melhorParaFeitc)
            if l == "Canalizacao" and canalizacao < max_pontos_por_atributo:
                canalizacao += 1
            elif l == "Arcanismo" and arcanismo < max_pontos_por_atributo:
                arcanismo += 1
            elif l == "Vigor" and vigor < max_pontos_por_atributo:
                vigor += 1
            else:
                continue  # Repetir a escolha se o atributo já atingiu o máximo permitido

        pts_total -= 1
    else:
        # Calcular pontos extras baseados na quantidade de pontos
        if pts_pda >= 3 and pts_pda <= 5:
            pontos_adicionais = 1
        elif pts_pda >= 6 and pts_pda <= 8:
            pontos_adicionais = 2
        elif pts_pda == 9:
            pontos_adicionais = 3
        else:
            pontos_adicionais = 0
        
        if pts_pda > 9:
            pontos_adicionais += (((pts_pda - 9) / 2 ) * 2) + 4
        
        pts_total += pontos_adicionais
    
        while pts_total > 0:
            l = random.choice(melhorParaFeitc)
            if l == "Canalizacao":
                canalizacao += 1
            elif l == "Arcanismo":
                arcanismo += 1
            elif l == "Vigor":
                vigor += 1
            else:
                continue  # Repetir a escolha se o atributo já atingiu o máximo permitido

            pts_total -= 1

        return canalizacao, arcanismo, vigor
    
def distrib_ladino(pts_pda):
    # Inicializar todos os atributos com 0
    precisao = 0
    destreza = 0
    vigor = 0
    agilidade = 0
    pts_total = 7
    # Lista dos atributos para distribuição
    melhorParaladino = ["Precisao", "Destreza", "Vigor", "Agilidade"]
    # Inicializar o limite máximo de pontos que podem ser distribuídos para cada atributo
    max_pontos_por_atributo = 2
    
    # Ajustar a quantidade de pontos iniciais
    if pts_pda == (1,2):
        pts_total = 7
        while pts_total > 0:
            l = random.choice(melhorParaladino)
            if l == "Precisao" and precisao < max_pontos_por_atributo:
                precisao += 1
            elif l == "Destreza" and destreza < max_pontos_por_atributo:
                espirito += 1
            elif l == "Vigor" and vigor < max_pontos_por_atributo:
                vigor += 1
            elif l == "Agilidade" and agilidade < max_pontos_por_atributo:
                agilidade +=1
            else:
                continue  # Repetir a escolha se o atributo já atingiu o máximo permitido

        pts_total -= 1
    else:
        # Calcular pontos extras baseados na quantidade de pontos
        if pts_pda >= 3 and pts_pda <= 5:
            pontos_adicionais = 1
        elif pts_pda >= 6 and pts_pda <= 8:
            pontos_adicionais = 2
        elif pts_pda == 9:
            pontos_adicionais = 3
        else:
            pontos_adicionais = 0
        
        if pts_pda > 9:
            pontos_adicionais += (((pts_pda - 9) / 2 ) * 2) + 4
        
        pts_total += pontos_adicionais
    
        while pts_total > 0:
            l = random.choice(melhorParaladino)
            if l == "Precisao":
                precisao += 1
            elif l == "Destreza":
                destreza += 1
            elif l == "Vigor":
                vigor += 1
            elif l == "Agilidade":
                agilidade +=1
            else:
                continue  # Repetir a escolha se o atributo já atingiu o máximo permitido

            pts_total -= 1

        return precisao, destreza, vigor, agilidade