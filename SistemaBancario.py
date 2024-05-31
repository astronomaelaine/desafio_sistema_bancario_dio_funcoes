def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):

    if (saldo < valor_saque):
        print(f""" Você não possui saldo suficente para esta operação. 
                    Saldo em conta: R$ {saldo:.2f}
                    Valor retirada: R$ {valor_saque:.2f}
                    """)

    elif (valor_saque > limite):
        print(f""" Operação Inválida! 
                        O valor limite para saque é de R${limite}.
                        """)

    elif (numero_saques >= limite_saques):
        print(f""" Operação Inválida! 
                        Você já  realizou os {limite_saques} saques permitidos hoje.
                        """)

    elif (valor_saque > 0):
        saldo -= valor_saque
        extrato += f"- Saque no valor de R$ {valor_saque:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    return saldo, extrato, numero_saques


def depositar(saldo, valor_deposito, extrato,/):
    if (valor_deposito > 0):
        saldo += valor_deposito
        extrato += f"+ Depósito no valor de R$ {valor_deposito:.2f}\n"

    else:
        print("""Operação Inválida!
                    Não é possível realizar depósitos de valores negativos.
                """)
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n ------------------- Extrato ------------------- \n")
    #        if(extrato == ""):
    #            print("\n Não foram realizadas movimentações na conta." if not extrato else extrato)
    print("\n Não foram realizadas movimentações na conta.\n" if not extrato else extrato)
    print(f"\n Saldo em conta: R$ {saldo:.2f}")
    print("\n ----------------------------------------------- \n")

def criar_usuario(usuarios):

    print("\n ------------------- CADASTRO DE USUARIO ------------------- \n")
    cpf = input("Digite o cpf do usuario: ")

    for usuario in usuarios:
        if(cpf == usuario["cpf"]):
            print(f"\nOps! Já existe usuário com o CPF {cpf}!")
            print(f"\nRetornando ao menu inicial...")
            return

    nome = input("Digite o nome do usuario: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    return {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}


def listar_usuarios(lista_usuarios):

    print("\n Lista de usuarios do sistema!")
    print("*********************************************************")
    for usuario in lista_usuarios:
        print(f"""Nome: {usuario["nome"]}
            CPF: {usuario["cpf"]}
            Data de nascimento: {usuario["data_nascimento"]}
            Endereço: {usuario["endereco"]}
        """)
        print("*********************************************************")


def criar_conta(agencia, numero, lista_usuarios):

    print("\n ------------------- CADASTRO DE CONTA ------------------- \n")

    cliente = input("\nDigite o CPF do cliente: ")
    for usuario in lista_usuarios:
        if(cliente == usuario["cpf"]):
            print("Cliente localizado")
            return {"agencia":agencia,"numero_conta":numero,"cliente":cliente}

        else:
            print("Não foi possível localizar um cliente com essa conta.")
            print("\nPor favor, tente novamente.")
            return

def listar_contas(lista_contas):

    print("\n Lista de contas do sistema!")
    print("*********************************************************")
    for conta in lista_contas:
        print(f"""Agencia: {conta["agencia"]}
            Numero da Conta: {conta["numero_conta"]}
            Cliente: {conta["cliente"]}
        """)
        print("*********************************************************")
def menu():
    menu = """
    ***************** MENU *****************
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    
    [u]  Novo Usuario
    [lu] Lista Usuarios
    
    [c]  Nova Conta
    [lc] Lista Contas
    
    [q]  Sair
    
    ::> """

    return menu

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    lista_usuario = []
    lista_contas = []

    AGENCIA = "0001"

    while True:
        opcao = input(menu())

        if (opcao == "d"):
            print("Deposito")

            valor_deposito = float(input("Insira o valor que deseja depositar: "))
            saldo, extrato = depositar(saldo,valor_deposito,extrato)


        elif (opcao == "s"):
            print("Saque")

            if (saldo <= 0):
                print("Você não possui saldo para realizar saque.")

            else:
                valor_saque = float(input("Insira o valor que deseja retirar: "))

                saldo, extrato,numero_saques = sacar(saldo=saldo, valor_saque=valor_saque,
                                       extrato=extrato,limite_saques=LIMITE_SAQUES,
                                       numero_saques=numero_saques,limite=limite)


        elif (opcao == "e"):
            exibir_extrato(saldo, extrato=extrato)

        elif (opcao == "u"):
            usuario = criar_usuario(lista_usuario)
            if(usuario):
                lista_usuario.append(usuario)
                print("\n Usuário cadastrado com sucesso!")
                print("\n -------------------*****------------------- \n")

        elif (opcao == "lu"):
            if not lista_usuario:
                print("Não há usuários cadastrados.")
                print("Retornando ao menu")
            else:
                listar_usuarios(lista_usuario)

        elif (opcao == "c"):
            num_conta= len(lista_contas)+1
            nova_conta = criar_conta(AGENCIA, num_conta, lista_usuario)
            if(nova_conta):
                lista_contas.append(nova_conta)
                print("\n Nova conta criada com sucesso!")
                print("\n -------------------*****------------------- \n")

        elif (opcao == "lc"):
            if not lista_contas:
                print("Não há contas cadastrados.")
                print("Retornando ao menu")
            else:
                listar_contas(lista_contas)

        elif (opcao == "q"):
            print("SAIR")
            exit()

        else:
            print("Opcao invalida.")

main();