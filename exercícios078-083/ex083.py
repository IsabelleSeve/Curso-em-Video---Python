# Crie um programa onde o usuario digite uma expresssão matemática qualquer que use parênteses,
# Seu aplicativo deverá analisar se a expressão passada está com os parênsetes abertos ou fechados
# na ordem correta.
resp = "s".upper()
while "S" in resp:
    expressao = str(input("Digite uma expressão numérica: "))
    if "(" in expressao and ")" in expressao:
        print("Sua expressão possui parênteses, então vamos continuar analisando...")
        if expressao.index("(") < expressao.index(")"):
            print("Sua expressão está correta! Parabéns.")
        else:
            print("Erro! "*3)
            print("Os parentêses estão na ordem errada, sua expressão não está correta!")
    else:
        print("Erro! " * 3)
        print("Sua expressão não possui parentêses.")
    resp = input("Deseja continuar [s/n]? ").upper()
