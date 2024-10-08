#2 em python: lista de tupla, cada tupla representa uma cidade com o nome da cidade e uma lista de temperaturas registradas ao
 # longo de uma semana (7 dias).Escreva uma funcao que calcule a temperatura media para cada cidade e retorne uma lista de
 #tuplas com o nome da cidade e a temperatura media.
 
 
def calcular_temperatura_media(cidades_temperaturas):
    medias = []
    for cidades, temperaturas in cidades_temperaturas:
        media = sum(temperaturas)/len(temperaturas)
        medias.append((cidades, media))
        return medias
    
    
cidades_temperaturas = [
    
        ("Sao Paulo", [22, 24, 27, 20, 25, 22, 26,]),
        ("Belo Horizonte", [24, 26, 27, 31, 32, 28, 27]),
        ("Salvador", [32, 33, 30, 29, 33, 30, 28])
]
    
resultado = calcular_temperatura_media(cidades_temperaturas)
print(resultado)
        