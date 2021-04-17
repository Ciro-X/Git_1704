//Cálculo de IMC
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))
imc = peso/(altura**2)
print("Seu IMC é {:.3}".format(imc))

//Mudança de temperatua de Fahrenheit para Celsius
tf = float(input("Digite a temperatura em Fahrenheit: "))
tc = (tf-32)*5/9
print("T em C: {:.2f}".format(tc))

//Cálculo da área
base = float(input("Digite o valor da base (m): "))
altura = float(input("Digite o valor da altura (m): "))
area = base*altura
print("O valor da área é: {} m^2".format(area))

//Número de eleitores
brancos = int(input("Digite a quantidade de votos brancos: "))
nulos = int(input ("Digite a quantidade de votos nulos: "))
validos = int(input ("Digite a quantidade de votos válidos: "))

eleitores = brancos + nulos + validos

pb = float((brancos/eleitores)*100)
pn = float((nulos/eleitores)*100)
pv = float((validos/eleitores)*100)

print ("O número total de eleitores foi de: ", eleitores)
print ("Com {:.2f}% de votos brancos".format(pb))
print ("Com {:.2f}% de votos nulos".format(pn))
print ("Com {:.2f}% de votos válidos".format(pv))

//Alteração de valores tilizando variáveis

a=10
b=20
aux = a
a = b
b = aux

print("A: ", a)
print ("B: ", b)

//necessário corrigir alteração
valfab = float(input("Digite o valor de fábrica: "))
valdist = float((valfab + (valfab*0,28))
valimp = float(valfab + (valfab*0,45))

valfinal = valfab+valimp+valdist

print("Valor final", valfinal)
