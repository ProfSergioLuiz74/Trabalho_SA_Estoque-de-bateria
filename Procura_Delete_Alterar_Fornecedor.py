#Importar as biblotecas
from tkinter import * #IMporta todos os modulos do tkinter
from tkinter import messagebox #importa o modulo de caixas de de mensagens do tkinter 
from tkinter import ttk #Importa a classe Database do modulo DataBase
from DataBase import Database
import tkinter as tk
class Procura_DeleteEAlterarFornecedor():
    def __init__(self,root):
    


        tituloLabel = Label(text="FORNECEDORES:",bg="white") #Coloca um titulo para a janela
        tituloLabel.place(x=160,y=10)

        alterarLabel = Label(text="Alterar forncedor:",bg="white") #Coloca um label
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

        def alterarFornecedor():

            #Transforma os campos de textos em variaveis
            idfornecedor=idEntry.get()
            fornecedores=FornecedorEntry.get()
            cpf=CpfFornecedorEntry.get()
            telefone=TelefoneFornecedorEntry.get()
            email=EmailFornecedorEntry.get()
            endereco=EnderecoFornecedorEntry.get()
            produto=ProdutoFornecedorEntry.get()
            quantidade=QuantidadeFornecedorEntry.get()


            if idfornecedor =="" or fornecedores == "" or cpf == "" or telefone == "" or email == "" or endereco == "" or produto == "" or quantidade == "": #Verifica se os campos de textos estão vazios
                messagebox.showerror(title="Erro de Atulização", message="PREENCHA TODOS OS CAMPOS") #Exibe a mensagem de erro
            else:
                db = Database() #Cria uma instancia da classe Database
                db.alterarFornecedor(idfornecedor,fornecedores,cpf,telefone,email,endereco,produto,quantidade) #Chama o metodo para registrar no banco de dados 
                messagebox.showinfo("Sucesso","Fornecedor atualizado com sucesso!") #Exibe a mensagem de sucesso

        def buscaFornecedor(): #Busca fornecedor de acordo com o id
            idfornecedor=idEntry.get()
            if idfornecedor =="": #Verifica se a caixa de texto do id está vazia
                messagebox.showerror(title="Erro de Busca", message="PREENCHA O CAMPO DE ID") #Exibe a mensagem de erro
            else:
                db = Database() #Cria uma instancia da classe Database
                db.buscarFornecedor(idfornecedor)
                usuario=buscaFornecedor()
                if usuario:
                    #Coloca as informações no campo de dados
                    FornecedorEntry.insert(0, usuario[1])
                    CpfFornecedorEntry.insert(0, usuario[2])
                    TelefoneFornecedorEntry.insert(0, usuario[3])
                    EmailFornecedorEntry.insert(0, usuario[4])
                    EnderecoFornecedorEntry.insert(0, usuario[5])
                    ProdutoFornecedorEntry.insert(0, usuario[6])
                    QuantidadeFornecedorEntry.insert(0, usuario[7])
                else:
                    messagebox.showerror(title="Erro de Busca", message="FORNECEDOR NÂO EXISTE") #Exibe a mensagem de erro

                
        def excluirFornecedor():
            idfornecedor=idEntry.get()
            if idfornecedor =="": #Verifica se a caixa de texto do id está vazia
                messagebox.showerror(title="Erro de Busca", message="PREENCHA O CAMPO DE ID") #Exibe a mensagem de erro
            else:
                db = Database() #Cria uma instancia da classe Database
                db.removerFornecedor(idfornecedor)
                messagebox.showinfo("Sucesso","Fornecedor atualizado com sucesso!") #Exibe a mensagem de sucesso

        def LimparCampos():
            FornecedorEntry.delete(0,END) #Limpa o campo de entrada do fornecedor
            CpfFornecedorEntry.delete(0,END) #Limpa o campo de entrada do cpf
            TelefoneFornecedorEntry.delete(0,END) #Limpa o campo de entrada do telefone
            EmailFornecedorEntry.delete(0,END) #Limpa o campo de entrada do email
            EnderecoFornecedorEntry.delete(0,END) #Limpa o campo de entrada do endereço
            ProdutoFornecedorEntry.delete(0,END) #Limpa o campo de entrada do produto
            QuantidadeFornecedorEntry.delete(0,END) #Limpa o campo de entrada da quantidade de produto
            idEntry.delete(0,END)

        alterarButton =  ttk.Button(text="ALTERAR",width=15,command=alterarFornecedor) #Cria o botão de alterar
        alterarButton.place(x=470,y=80)

        pesquisaButton =  ttk.Button(text="BUSCAR",width=15,command=buscaFornecedor) #Cria o botão de buscar
        pesquisaButton.place(x=370,y=80)

        excluirButton =  ttk.Button(text="EXCLUIR",width=15,command=excluirFornecedor) #Cria o botão de excluir
        excluirButton.place(x=570,y=80)

        limparButton =  ttk.Button(text="LIMPAR",width=15,command=LimparCampos) #Cria o botão de limpar
        limparButton.place(x=670,y=80)

if __name__=="__main__":
    jan=Tk() # Cria uma instancia da janela principal
    jan.title("ADM - Leitor Fornecedor") #Define o titulo da janela
    jan .geometry("900x700") #Define o tamanho da janela
    jan.configure(background="white") #Configura a cor de fundo da janela
    jan.resizable(width=False,height=False) #Impede que a janela seja redimensionad
    app=Procura_DeleteEAlterarFornecedor(jan)
    jan.mainloop()