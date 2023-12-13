import tkinter as tk

def cadastrar_album():
    nome = entrada_nome.get()
    ano = entrada_ano.get()
    artista = entrada_artista.get()
    lancamento = "Sim" if var_lancamento.get() == 1 else "Não"

    # Verifica se o ano é um número inteiro
    if ano.isdigit():
        with open("albuns.txt", "a") as arquivo:
            arquivo.write(f"{nome},{ano},{artista},{lancamento}\n")
        limpar_campos()
    else:
        # Se o ano não for um número, exibe uma mensagem de erro
        label_erro.config(text="Por favor, insira um ano válido.")

def limpar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_ano.delete(0, tk.END)
    entrada_artista.delete(0, tk.END)
    var_lancamento.set(0)
    label_erro.config(text="")  # Limpa a mensagem de erro

def listar_albuns():
    lista.delete(0, tk.END)

    try:
        with open("albuns.txt", "r") as arquivo:
            for linha in arquivo:
                album_info = linha.strip().split(",")
                lista.insert(tk.END, f"Nome: {album_info[0]} - Ano: {album_info[1]} - Artista: {album_info[2]} - Lançamento: {album_info[3]}")
    except FileNotFoundError:
        lista.insert(tk.END, "Nenhum álbum cadastrado ainda.")

# Criar a janela principal
root = tk.Tk()
root.title("Cadastro de Álbuns")

# Campos de entrada
label_nome = tk.Label(root, text="Nome do Álbum:")
label_nome.pack()
entrada_nome = tk.Entry(root)
entrada_nome.pack()

label_ano = tk.Label(root, text="Ano de Lançamento:")
label_ano.pack()
entrada_ano = tk.Entry(root)
entrada_ano.pack()

label_artista = tk.Label(root, text="Nome do Artista/Banda:")
label_artista.pack()
entrada_artista = tk.Entry(root)
entrada_artista.pack()

var_lancamento = tk.IntVar()
check_lancamento = tk.Checkbutton(root, text="Álbum Lançamento do Artista", variable=var_lancamento)
check_lancamento.pack()

btn_cadastrar = tk.Button(root, text="Cadastrar Álbum", command=cadastrar_album)
btn_cadastrar.pack()

btn_listar = tk.Button(root, text="Listar Álbuns", command=listar_albuns)
btn_listar.pack()

# Lista de álbuns cadastrados
label_lista = tk.Label(root, text="Álbuns Cadastrados:")
label_lista.pack()
lista = tk.Listbox(root, width=50)
lista.pack()

# Label para exibir mensagens de erro
label_erro = tk.Label(root, fg="red")
label_erro.pack()

root.mainloop()
