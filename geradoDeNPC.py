import random
import os
from legados import legado, habil_legado
from caminhos_basic import sort_caminho_basic, sort_graca
from pda_gaia import sort_pda
from param_e_conhec import distrib_andarilho, distrib_combatente, distrib_devoto, distrib_feiticeiro, distrib_ladino
from life_Energi import qts_energi, qts_life
from habilits_caminho import escolhaCam


npc_play = {
    'nome_play': [],
    'raça': [],
    # 'habilidade_raça': [],
    'Caminho_basico': [],
    'graça':[],
    'PDA': [],
    'Precisao':[],
    'brutalidade':[],
    'destreza':[],
    'agilidade':[],
    'canalizacao':[],
    'arcanismo':[],
    'espirito':[], 
    'vigor':[],
    'Pontos de Energia': [],
    'Vida': []


}

print("Gerador de personagens do RPG: Gaia o preludio")

nome = str(input("Insira o nome do personagem: "))
pda_Npc = str(input(f'Escolha o nivél de PDA: Novato = N, Aventureiro = A, Herói = H, Lenda = L, Semi-Deus = S ou T para qualquer nivél:'))
while pda_Npc.lower() not in ["n", "a", "h", "l", "s", "t"]:
    pda_Npc = str(input("Digite um valor válido: "))
    if pda_Npc.lower() == "n" or pda_Npc.lower() == "a" or pda_Npc.lower() == "h" or pda_Npc.lower() == "l" or pda_Npc.lower() == "s" or pda_Npc.lower() == "t": 
        break
esc_nvl = sort_pda(pda_Npc)
caminho_basic = sort_caminho_basic()
pE = qts_energi(esc_nvl)

npc_play["nome_play"].append(nome)
npc_play["raça"].append(legado) 
npc_play["Caminho_basico"].append(caminho_basic)
npc_play["PDA"].append(esc_nvl)
npc_play["Pontos de Energia"].append(pE)

ale_ord = str(input(f'Vc deseja que a distribuição de PDA sejá feita direcinado para seu caminho Sim/s ou Não/n? ')).lower()
if ale_ord == "s" or ale_ord == "S":
    if caminho_basic == "Andarilho":
        precisao, canalizacao, arcanismo, espirito, vigor = distrib_andarilho(esc_nvl)
        # Atualizar o dicionário com os valores distribuídos
        npc_play["Precisao"].append(precisao)
        npc_play["canalizacao"].append(canalizacao)
        npc_play["arcanismo"].append(arcanismo)
        npc_play["espirito"].append(espirito)
        npc_play["vigor"].append(vigor)
        npc_play["brutalidade"].append(0)
        npc_play["agilidade"].append(0)
        npc_play["destreza"].append(0)
    elif caminho_basic == "Combatente":
        precisao, brutalidade, arcanismo, destreza, vigor, agilidade = distrib_combatente(esc_nvl)
        # Atualizar o dicionário com os valores distribuídos
        npc_play["Precisao"].append(precisao)
        npc_play["canalizacao"].append(0)
        npc_play["arcanismo"].append(arcanismo)
        npc_play["espirito"].append(0)
        npc_play["vigor"].append(vigor)
        npc_play["brutalidade"].append(brutalidade)
        npc_play["agilidade"].append(agilidade)
        npc_play["destreza"].append(destreza)
    elif caminho_basic == "Devoto":
        precisao, canalizacao, espirito, vigor = distrib_devoto(esc_nvl)
        npc_play["Precisao"].append(precisao)
        npc_play["canalizacao"].append(canalizacao)
        npc_play["arcanismo"].append(0)
        npc_play["espirito"].append(espirito)
        npc_play["vigor"].append(vigor)
        npc_play["brutalidade"].append(0)
        npc_play["agilidade"].append(0)
        npc_play["destreza"].append(0)
    elif caminho_basic == "Feiticeiro":
        canalizacao, vigor, arcanismo = distrib_feiticeiro(esc_nvl)
        npc_play["Precisao"].append(0)
        npc_play["canalizacao"].append(canalizacao)
        npc_play["arcanismo"].append(arcanismo)
        npc_play["espirito"].append(0)
        npc_play["vigor"].append(vigor)
        npc_play["brutalidade"].append(0)
        npc_play["agilidade"].append(0)
        npc_play["destreza"].append(0)
    elif caminho_basic == "Ladino":
        precisao, agilidade, destreza, vigor = distrib_ladino(esc_nvl)
        npc_play["Precisao"].append(precisao)
        npc_play["canalizacao"].append(0)
        npc_play["arcanismo"].append(0)
        npc_play["espirito"].append(0)
        npc_play["vigor"].append(vigor)
        npc_play["brutalidade"].append(0)
        npc_play["agilidade"].append(agilidade)
        npc_play["destreza"].append(destreza)

else:
    # Atribua valores padrão
    npc_play["Precisao"].append(0)
    npc_play["canalizacao"].append(0)
    npc_play["arcanismo"].append(0)
    npc_play["espirito"].append(0)
    npc_play["vigor"].append(0)
    npc_play["brutalidade"].append(0)
    npc_play["destreza"].append(0)
    npc_play["agilidade"].append(0)

vidaNPC = qts_life(esc_nvl, vigor)
npc_play['Vida'].append(vidaNPC)
print(legado)
print(caminho_basic)
print(esc_nvl)
print(pE)
print(vidaNPC)

# npc_play["habilidade_raça"].append(desc_hab_legado)


graca_escolhida = None
if caminho_basic == "Devoto":
    devoto_esco = str(input("Que deseja receber graça de qual plano: b-Balança, c-Caos, o-Ordem ou qualquer outra coisa pra ser aleatoria: "))
    while devoto_esco.lower() not in ["b", "c", "o"]:
        devoto_esco = str(input("Digite um valor válido: "))
        if devoto_esco.lower() == "b" or devoto_esco.lower() == "c" or devoto_esco.lower() == "o": 
            break
    graca_escolhida = sort_graca(devoto_esco)
    npc_play["graça"].append(graca_escolhida)
    print(f'A graça escolhida é: {graca_escolhida}')
else:
    npc_play["graça"].append('vazio')

if esc_nvl > 1:
    escolhaCam(caminho_basic)


print(f'{"N°":<4}{"Nome":<10}{"Legado":<15}{"Caminho(s)":<25}{"Graça":<20}{"PDA":<15}{"Precisão":<10}{"Brutalidade":<15}{"Destreza":<10}{"Agilidade":<10}{"Canalização":<15}{"Arcanismo":<10}{"Espírito":<10}{"Vigor":<10}{"PE":<10}{"Vida":<10}')
for idx, nome in enumerate(npc_play["nome_play"], start=1):
    print(f'{idx:<4}{nome:<10}{npc_play["raça"][idx-1]:<15}{npc_play["Caminho_basico"][idx-1]:<25}{npc_play["graça"][idx-1]:<20}{npc_play["PDA"][idx-1]:<15}'
          f'{npc_play["Precisao"][idx-1]:<10}{npc_play["brutalidade"][idx-1]:<15}{npc_play["destreza"][idx-1]:<10}{npc_play["agilidade"][idx-1]:<10}'
          f'{npc_play["canalizacao"][idx-1]:<15}{npc_play["arcanismo"][idx-1]:<10}{npc_play["espirito"][idx-1]:<10}{npc_play["vigor"][idx-1]:<10}{npc_play["Pontos de Energia"][idx-1]:<10}{npc_play["Vida"][idx-1]:<10}')


