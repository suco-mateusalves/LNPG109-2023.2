def preencher_formulario():
    while True:
        nome = input("Digite o nome (ou '0' para encerrar): ")
        if nome == '0':
            break
        
        while True:
            idade = input("Digite a idade: ")
            if idade.isdigit():
                break
            else:
                print("Por favor, digite uma idade válida (número inteiro).")

        while True:
            sexo = input("Digite o sexo (M ou F): ").upper()
            if sexo in ['M', 'F']:
                break
            else:
                print("Por favor, digite 'M' para masculino ou 'F' para feminino.")

        telefone = input("Digite o telefone: ")

        with open('informacoes.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f"{nome}|{idade}|{sexo}|{telefone}\n")

def ler_dados():
    try:
        with open('informacoes.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split('|')
                nome = dados[0]
                idade = dados[1]
                if dados[2] == 'M':
                    sexo = 'Masculino'
                else: 
                    sexo = 'Feminino'
                telefone = dados[3]

                print(f"Nome: {nome}")
                print(f"Idade: {idade} anos")
                print(f"Sexo: {sexo}")
                print(f"Telefone: {telefone}")
                print("")
    except FileNotFoundError:
        print("Ainda não existem dados para exibir.")

def busca_usuario_pelo_sexo(sexo):
    resultados = []
    try:
        with open('informacoes.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split('|')
                if dados[2].upper() == sexo.upper():
                    resultados.append({
                        'Nome': dados[0],
                        'Idade': dados[1],
                        'Sexo': 'Masculino' if dados[2] == 'M' else 'Feminino',
                        'Telefone': dados[3]
                    })
    except FileNotFoundError:
        print("Ainda não existem dados para buscar.")

    return resultados

def main():
    while True:
        print("Selecione uma opção:")
        print("1. Preencher formulário")
        print("2. Ler dados")
        print("3. Buscar usuários por sexo")
        print("4. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            preencher_formulario()
        elif opcao == '2':
            ler_dados()
        elif opcao == '3':
            sexo = input("Digite o sexo para buscar (M ou F): ")
            resultados = busca_usuario_pelo_sexo(sexo)
            for usuario in resultados:
                print(f"Nome: {usuario['Nome']}")
                print(f"Idade: {usuario['Idade']} anos")
                print(f"Sexo: {usuario['Sexo']}")
                print(f"Telefone: {usuario['Telefone']}")
                print("")
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
