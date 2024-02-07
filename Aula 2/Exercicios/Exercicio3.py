listaDeCores = ["Azul", "Amarelo", "Vermelho"]

corDigitada1 = input("Digite uma cor: ")
if corDigitada1 == "Azul" or corDigitada1 == "Amarelo" or corDigitada1 == "Vermelho":
    corDigitada1 =  input("Digite novamente! OBS:não escolha a cor azul, amarelo e vermelho") 

corDigitada2 = input("Digite outra cor: ")
if corDigitada2 == "Azul" or corDigitada2 == "Amarelo" or corDigitada2 == "Vermelho" or corDigitada2 == corDigitada1:
    corDigitada2 =  input("Digite novamente! OBS:não escolha a cor azul, amarelo, vermelho e "+str(corDigitada1))

listaDeCores.append(str(corDigitada1))
listaDeCores.append(str(corDigitada2))

print("A lista final de cores ficou:")
print(listaDeCores)
print("---------------x----------------")



latitude = input("Digite uma latitude: ")
longitude = input("Digite uma longitude: ")

coordenadas= (float(latitude), float(longitude))

print("As coordenadas ficaram: Latitude: "+str(coordenadas[0])+" Longitude: "+str(coordenadas[1]))