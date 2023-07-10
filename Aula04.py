import sys

def instructions():
    "Imprime as instrucoes para o usuario"
    print("Entre com uma opcao:\n", \
          "  1 para inserir inicio da lista\n", \
          "  2 para inserir no final da lista\n", \
          "  3 para deletar no comeco da lista\n", \
          "  4 para deletar no final da lista\n", \
          "  5 para finalizar programa\n")


listObject = list()  # instacia uma lista
instructions()
choice = str(input("? "))

while choice != "5":
    if choice == "1":
        listObject.insertAtBegin(input("Entre com o valor para a cabeca:"))
        print("Lista: ", listObject.getAsText())
    elif choice == "2":
        listObject.insertAtEnd(input("Entre com o valor para a cauda:"))
        print("Lista: ", listObject.getAsText())
    elif choice == "3":
        try:
            value = listObject.removeFromBegin()
        except(IndexError):
            print("Falha na Operacao: lista vazia")
        else:
            print(value, "removido da cabeca da lista")
            print("Lista: ", listObject.getAsText())
    elif choice == "4":
        try:
            value = listObject.removeFromEnd()
        except(IndexError):
            print("Falha na Operacao: lista vazia")
        else:
            print("Lista: ", value, "removido da cauda da lista")
            print(listObject.getAsText())
    else:
        print("Opcao invalida:", choice)
        instructions()
    choice = str(input("\n? "))
print("Fim do programa")