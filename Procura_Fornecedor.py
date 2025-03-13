#Importar as biblotecas
from tkinter import * #IMporta todos os modulos do tkinter
from tkinter import messagebox #importa o modulo de caixas de de mensagens do tkinter 
from tkinter import ttk #Importa a classe Database do modulo DataBase
from DataBase import Database

class Procura_Fornecedor():
    def __init__(self,root):
    


        tituloLabel = Label(text="FORNECEDORES PARA USUARIO:",bg="white") #Coloca um titulo para a janela
        tituloLabel.place(x=160,y=10)

        infoLabel = Label(text="Digite o ID do fornecedor para procurar:",bg="white") #Coloca um titulo para a janela
        infoLabel.place(x=40,y=40)

        alterarLabel = Label(text="Dados do forncedor procurado:",bg="white") #Coloca um label
        alterarLabel.place(x=40,y=110)

        idLabel = Label(text="ID do Fornecedor:",bg="White") #Cria label do ID
        idLabel.place(x=10,y=80)
        idEntry=ttk.Entry(width=30) #Cria um campo do ID
        idEntry.place(x=150,y=80)   

        FornecedorLabel = Label(text="Nome do Fornecedor:",bg="White") #Cria label do fornecedor
        FornecedorLabel.place(x=10,y=150)
        FornecedorEntry=ttk.Entry(width=30) #Cria um campo do forncedor
        FornecedorEntry.place(x=150,y=150)   

        CpfFornecedorLabel = Label(text="CPF do Fornecedor:",bg="White") #Cria label do Cpf
        CpfFornecedorLabel.place(x=10,y=190)
        CpfFornecedorEntry = ttk.Entry(width=30) #Cria um campo do cpf
        CpfFornecedorEntry.place(x=150,y=190)

        TelefoneFornecedorLabel = Label(text="Telefone do fornecedor:",bg="White") #Cria label do Telefone
        TelefoneFornecedorLabel.place(x=10,y=230)
        TelefoneFornecedorEntry = ttk.Entry(width=30) #Cria um campo do telefone
        TelefoneFornecedorEntry.place(x=150,y=230)

        EmailFornecedorLabel = Label(text="Email do Fornecedor:",bg="White") #Cria label do email
        EmailFornecedorLabel.place(x=10,y=270)
        EmailFornecedorEntry = ttk.Entry(width=30) #Cria um campo do email
        EmailFornecedorEntry.place(x=150,y=270)

        EnderecoFornecedorLabel = Label(text="Endereço do Fornecedor:",bg="White") #Cria label do endereço
        EnderecoFornecedorLabel.place(x=10,y=310)
        EnderecoFornecedorEntry = ttk.Entry(width=30) #Cria um campo do endereço
        EnderecoFornecedorEntry.place(x=150,y=310)

        ProdutoFornecedorLabel = Label(text="Produto Fornecido:",bg="White") #Cria label do produto
        ProdutoFornecedorLabel.place(x=10,y=350)
        ProdutoFornecedorEntry = ttk.Entry(width=30) #Cria um campo do produto
        ProdutoFornecedorEntry.place(x=150,y=350)

        QuantidadeFornecedorLabel = Label(text="Quantia de Produto:",bg="White") #Cria label da quantidade de produto fornecido 
        QuantidadeFornecedorLabel.place(x=10,y=390)
        QuantidadeFornecedorEntry = ttk.Entry(width=30) #Cria um campo para colocar a quantidade de produto fornecido
        QuantidadeFornecedorEntry.place(x=150,y=390)
        
        def LimparCampos():
                    FornecedorEntry.delete(0,END) #Limpa o campo de entrada do fornecedor
                    CpfFornecedorEntry.delete(0,END) #Limpa o campo de entrada do cpf
                    TelefoneFornecedorEntry.delete(0,END) #Limpa o campo de entrada do telefone
                    EmailFornecedorEntry.delete(0,END) #Limpa o campo de entrada do email
                    EnderecoFornecedorEntry.delete(0,END) #Limpa o campo de entrada do endereço
                    ProdutoFornecedorEntry.delete(0,END) #Limpa o campo de entrada do produto
                    QuantidadeFornecedorEntry.delete(0,END) #Limpa o campo de entrada da quantidade de produto
                    idEntry.delete(0,END)
        
        def buscaFornecedor():
            idfornecedor=idEntry.get()
            if idfornecedor =="":
                messagebox.showerror(title="Erro de Busca", message="PREENCHA O CAMPO DE ID") #Exibe a mensagem de erro
            else:
                db = Database()
                db.buscarFornecedor(idfornecedor)
                usuario=buscaFornecedor()
                if usuario:
                    FornecedorEntry.insert(0, usuario[1])
                    CpfFornecedorEntry.insert(0, usuario[2])
                    TelefoneFornecedorEntry.insert(0, usuario[3])
                    EmailFornecedorEntry.insert(0, usuario[4])
                    EnderecoFornecedorEntry.insert(0, usuario[5])
                    ProdutoFornecedorEntry.insert(0, usuario[6])
                    QuantidadeFornecedorEntry.insert(0, usuario[7])
                else:
                    messagebox.showerror(title="Erro de Busca", message="FORNECEDOR NÂO EXISTE") #Exibe a mensagem de erro


        pesquisaButton =  ttk.Button(text="BUSCAR",width=15,command=buscaFornecedor) #Cria o botão de alterar
        pesquisaButton.place(x=370,y=80)
        limparButton =  ttk.Button(text="LIMPAR",width=15,command=LimparCampos) #Cria o botão de alterar
        limparButton.place(x=470,y=80)





if __name__=="__main__":
    jan=Tk() # Cria uma instancia da janela principal
    jan.title("ADM - Leitor Fornecedor") #Define o titulo da janela
    jan .geometry("900x700") #Define o tamanho da janela
    jan.configure(background="white") #Configura a cor de fundo da janela
    jan.resizable(width=False,height=False) #Impede que a janela seja redimensionad
    app=Procura_Fornecedor(jan)
    jan.mainloop()