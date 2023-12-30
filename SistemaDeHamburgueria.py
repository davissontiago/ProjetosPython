import os
cardapio=[
    { 
    "codigo":0,
    "nome":"Cheese Salada",
    "descricao":"Pão, carne de 80g, queijo, alface, tomate e molho",
    "valor":19.99
    },
    { 
    "codigo":1,
    "nome":"Cheese Bacon",
    "descricao":"Pão, carne de 180g, 5x fatias bacon, queijo, cebola e molho",
    "valor":24.99
    },
    { 
    "codigo":2,
    "nome":"Cheese Supremo",
    "descricao":"Pão, 3x carne de 80g, 3x quejo, cebola e molho",
    "valor":28.99
    },
    { 
    "codigo":3,
    "nome":"Cheese Vegan",
    "descricao":"Pão Vegano, blend de lentilhas, cebola, tomate, alface e molho",
    "valor":24.99
    }
]

pedidos=[]

def ExibirMenu():
    print("""----------------------------MENU----------------------------
1 - Cardápio
2 - Realizar pedido
3 - Listar pedidos
0 - Sair
------------------------------------------------------------""")
    entrada=int(input("Digite a opção:"))
    return entrada

def ExibirCardapio():
    print("===============Cardápio===============")
    for i in range(len(cardapio)):
        print(f"""------------------------------------------------------------
codigo: {cardapio[i]['codigo']}
nome = {cardapio[i]['nome']}
descrica = {cardapio[i]['descricao']}
valor = {cardapio[i]['valor']}""")
    print("------------------------------------------------------------")

def RealizarPedido():
    cod = int(input("Digite o código do produto (-1 para voltar para o menu): "))
    if cod == -1:
        return
    elif 0 <= cod < len(cardapio):
        pedidos.append({"nome": cardapio[cod]['nome'], "valor": cardapio[cod]['valor']})
        print(f"{cardapio[cod]['nome']} adicionado à Lista.")
    else:
        print("Código Inválido. Tente Novamente.")

def SomaPedidos():
    soma=0
    for i in pedidos:
        soma=soma+i['valor']
    return soma
    
def ExibirLista():
    print("===============Pedidos===============")
    for i in range(len(pedidos)):
        print(f"{pedidos[i]['nome']} - {pedidos[i]['valor']}")
    total=SomaPedidos()
    print(f"------------------------Total: {total}------------------------")
    
op=1
while(op!=0):
    op=ExibirMenu()
    if(op==1):
        os.system("cls")
        ExibirCardapio()
    if(op==2):
        os.system("cls")
        RealizarPedido()
    if(op==3):
        os.system("cls")
        ExibirLista()
    input("Aperte ENTER para retornar ao menu.")
    os.system("cls")