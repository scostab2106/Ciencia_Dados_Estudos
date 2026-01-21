#CALCULADORA

#Interface
while True:
    operacao = int(input(
"\n   1 - SOMA \n" \
"   2 - SUBTRAÇÃO\n" \
"   3 - MULTIPLICAÇÃO\n" \
"   4 - DIVISÃO\n" \
"   0 - SAIR\n"
"\n"
))
    
    #Interrupção
    if operacao == 0:
        break

    #Leitura dos números
    num1 = float(input("Digite o Primeiro Número: "))
    num2 = float(input("Digite o Segundo Número: "))

    resultado = 0

    #Operações e decisão
    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 4:
        resultado = num1 / num2
    

    print("RESULTADO: ", resultado,"\n")