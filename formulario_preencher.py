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

        # Salvando as informações no arquivo
        with open('informacoes.txt', 'a') as arquivo:
            arquivo.write(f"{nome}|{idade}|{sexo}|{telefone}\n")

preencher_formulario()
