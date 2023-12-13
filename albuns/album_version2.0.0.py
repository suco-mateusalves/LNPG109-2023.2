import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def cadastrar_album():
    try:
        nome = entry_nome.get()
        ano = entry_ano.get()
        artista = entry_artista.get()
        lancamento = "Sim" if var_lancamento.get() == 1 else "Não"

        with open("albuns.txt", "a") as file:
            file.write(f"{nome},{ano},{artista},{lancamento}\n")
        limpar_campos()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar álbum: {e}")

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_ano.delete(0, tk.END)
    entry_artista.delete(0, tk.END)
    var_lancamento.set(0)

def listar_albuns():
    lista.delete(0, tk.END)
    try:
        with open("albuns.txt", "r") as file:
            for line in file:
                album_info = line.strip().split(",")
                lista.insert(tk.END, f"Nome: {album_info[0]} - Ano: {album_info[1]} - Artista: {album_info[2]} - Lançamento: {album_info[3]}")
    except FileNotFoundError:
        messagebox.showinfo("Info", "Nenhum álbum cadastrado ainda!")

def buscar_por_artista():
    try:
        lista.delete(0, tk.END)
        busca = entry_busca_artista.get().upper()
        with open("albuns.txt", "r") as file:
            for line in file:
                album_info = line.strip().split(",")
                if busca in album_info[2].upper():
                    lista.insert(tk.END, f"Nome: {album_info[0]} - Ano: {album_info[1]} - Artista: {album_info[2]} - Lançamento: {album_info[3]}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao buscar por artista: {e}")

def buscar_por_ano():
    try:
        lista.delete(0, tk.END)
        busca_ano = int(combobox_ano.get())
        opcao = var_radio.get()

        with open("albuns.txt", "r") as file:
            for line in file:
                album_info = line.strip().split(",")
                ano_album = int(album_info[1])

                if (opcao == 1 and ano_album < busca_ano) or (opcao == 2 and ano_album > busca_ano) or (opcao == 3 and ano_album == busca_ano):
                    lista.insert(tk.END, f"Nome: {album_info[0]} - Ano: {album_info[1]} - Artista: {album_info[2]} - Lançamento: {album_info[3]}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, selecione um ano válido.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao buscar por ano: {e}")

# Criar a janela principal
root = tk.Tk()
root.title("Cadastro e Busca de Álbuns")
root.resizable(1, 0)



# Campos de entrada para cadastro
label_nome = tk.Label(root, text="Nome do Álbum:")
label_nome.pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

label_ano = tk.Label(root, text="Ano de Lançamento:")
label_ano.pack()
entry_ano = tk.Entry(root)
entry_ano.pack()

label_artista = tk.Label(root, text="Nome do Artista/Banda:")
label_artista.pack()
entry_artista = tk.Entry(root)
entry_artista.pack()

var_lancamento = tk.IntVar()
check_lancamento = tk.Checkbutton(root, text="Álbum Lançamento do Artista", variable=var_lancamento)
check_lancamento.pack()

btn_cadastrar = tk.Button(root, text="Cadastrar Álbum", command=cadastrar_album)
btn_cadastrar.pack()

btn_listar = tk.Button(root, text="Listar Álbuns", command=listar_albuns)
btn_listar.pack()

# Buscar por nome do Artista
label_busca_artista = tk.Label(root, text="Buscar por nome de Artista:")
label_busca_artista.pack()
entry_busca_artista = tk.Entry(root)
entry_busca_artista.pack()

btn_buscar_artista = tk.Button(root, text="Buscar por Artista", command=buscar_por_artista)
btn_buscar_artista.pack()

# Buscar por ano do Álbum
label_busca_ano = tk.Label(root, text="Buscar por ano do Álbum:")
label_busca_ano.pack()

var_radio = tk.IntVar()
radio_antes = tk.Radiobutton(root, text="Anterior a", variable=var_radio, value=1)
radio_antes.pack()
radio_depois = tk.Radiobutton(root, text="Posterior a", variable=var_radio, value=2)
radio_depois.pack()
radio_igual = tk.Radiobutton(root, text="Igual a", variable=var_radio, value=3)
radio_igual.pack()

anos = [str(i) for i in range(1950, 2031)]
combobox_ano = ttk.Combobox(root, values=anos)
combobox_ano.pack()

btn_buscar_ano = tk.Button(root, text="Buscar por Ano", command=buscar_por_ano)
btn_buscar_ano.pack()

# Lista de álbuns cadastrados
label_lista = tk.Label(root, text="Álbuns Cadastrados:")
label_lista.pack()
lista = tk.Listbox(root, width=50)
lista.pack()

root.mainloop()
