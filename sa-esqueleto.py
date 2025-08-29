pessoas = []

def validar_email(email):
    return '@' in email and '.' in email.split('@')[-1]

def validar_cep(cep):
    return cep.isdigit() and len(cep) == 8

def cadastrar_pessoa():
    print("\n--- Cadastro de Pessoa ---")
    
    nome = input("Nome: ").strip()
    if nome == "":
        print("Nome não pode ser vazio.")
        return

    cpf = input("CPF (apenas números): ").strip()
    if not (cpf.isdigit() and len(cpf) == 11):
        print("CPF inválido. Deve conter exatamente 11 dígitos.")
        return

    idade = input("Idade: ").strip()
    if not idade.isdigit() or int(idade) <= 0:
        print("Idade inválida. Deve ser um número positivo.")
        return
    idade = int(idade)

    email = input("E-mail: ").strip()
    if not validar_email(email):
        print("E-mail inválido. Deve conter '@' e '.'.")
        return

    cep = input("CEP (apenas números): ").strip()
    if not validar_cep(cep):
        print("CEP inválido. Deve conter exatamente 8 dígitos.")
        return

    telefone = input("Telefone (com DDD, apenas números): ").strip()
    if not telefone.isdigit() or len(telefone) < 10 or len(telefone) > 11:
        print("Telefone inválido. Deve conter 10 ou 11 dígitos (com DDD).")
        return

    genero = input("Gênero (M/F/Outro): ").strip().upper()
    if genero not in ['M', 'F', 'OUTRO']:
        print("Gênero inválido. Opções válidas: M, F ou Outro.")
        return

    pessoa = {
        "nome": nome,
        "cpf": cpf,
        "idade": idade,
        "email": email,
        "cep": cep,
        "telefone": telefone,
        "genero": genero
    }
    
    pessoas.append(pessoa)
    print("Pessoa cadastrada com sucesso!")

def listar_pessoas():
    print("\n--- Lista de Pessoas ---")
    if not pessoas:
        print("Nenhuma pessoa cadastrada.")
        return
    
    for i, pessoa in enumerate(pessoas, 1):
        print(f"\nPessoa {i}:")
        print(f"Nome: {pessoa['nome']}")
        print(f"CPF: {pessoa['cpf']}")
        print(f"Idade: {pessoa['idade']}")
        print(f"E-mail: {pessoa['email']}")
        print(f"CEP: {pessoa['cep']}")
        print(f"Telefone: {pessoa['telefone']}")
        print(f"Gênero: {pessoa['genero']}")

def editar_pessoa():
    if not pessoas:
        print("Não há pessoas cadastradas para editar.")
        return
    
    listar_pessoas()
    try:
        indice = int(input("\nDigite o número da pessoa para editar: ")) - 1
        if indice < 0 or indice >= len(pessoas):
            print("Número inválido.")
            return
    except ValueError:
        print("Digite um número válido.")
        return

    pessoa = pessoas[indice]
    print(f"\nEditando pessoa: {pessoa['nome']}")
    
    novo_nome = input(f"Nome ({pessoa['nome']}): ").strip()
    if novo_nome != "":
        pessoa['nome'] = novo_nome
    
    nova_idade = input(f"Idade ({pessoa['idade']}): ").strip()
    if nova_idade != "":
        if not nova_idade.isdigit() or int(nova_idade) <= 0:
            print("Idade inválida. Mantendo a idade anterior.")
        else:
            pessoa['idade'] = int(nova_idade)
    
    novo_email = input(f"E-mail ({pessoa['email']}): ").strip()
    if novo_email != "":
        if not validar_email(novo_email):
            print("E-mail inválido. Mantendo o e-mail anterior.")
        else:
            pessoa['email'] = novo_email
    
    novo_cep = input(f"CEP ({pessoa['cep']}): ").strip()
    if novo_cep != "":
        if not validar_cep(novo_cep):
            print("CEP inválido. Mantendo o CEP anterior.")
        else:
            pessoa['cep'] = novo_cep
    
    novo_telefone = input(f"Telefone ({pessoa['telefone']}): ").strip()
    if novo_telefone != "":
        if not novo_telefone.isdigit() or len(novo_telefone) < 10 or len(novo_telefone) > 11:
            print("Telefone inválido. Mantendo o telefone anterior.")
        else:
            pessoa['telefone'] = novo_telefone
    
    novo_genero = input(f"Gênero ({pessoa['genero']}): ").strip().upper()
    if novo_genero != "":
        if novo_genero not in ['M', 'F', 'OUTRO']:
            print("Gênero inválido. Mantendo o gênero anterior.")
        else:
            pessoa['genero'] = novo_genero
    
    print("Dados atualizados com sucesso!")

def excluir_pessoa():
    if not pessoas:
        print("Não há pessoas cadastradas para excluir.")
        return
    
    listar_pessoas()
    try:
        indice = int(input("\nDigite o número da pessoa para excluir: ")) - 1
        if indice < 0 or indice >= len(pessoas):
            print("Número inválido.")
            return
    except ValueError:
        print("Digite um número válido.")
        return
    
    pessoa_removida = pessoas.pop(indice)
    print(f"Pessoa {pessoa_removida['nome']} removida com sucesso!")

def menu():
    while True:
        print("\n====== MENU PRINCIPAL ======")
        print("1. Cadastrar Pessoa")
        print("2. Listar Pessoas")
        print("3. Editar Pessoa")
        print("4. Excluir Pessoa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_pessoa()
        elif opcao == '2':
            listar_pessoas()
        elif opcao == '3':
            editar_pessoa()
        elif opcao == '4':
            excluir_pessoa()
        elif opcao == '5':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()