import mysql.connector #Importa o modulo mysql.connector para conectar ao banco de dados MySQL
class Database:
    def __init__(self):
        #Conecta ao banco de dados MySQL com as credenciais forncedas
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'trabalho_sa'
        )

        self.cursor = self.conn.cursor() #Cria um cursor para executar comandos MySQL
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `fornecedor` (
                        `idfornecedor` int(11) NOT NULL,
                        `fornecedores` text DEFAULT NULL,
                        `cpf` text DEFAULT NULL,
                        `telefone` text DEFAULT NULL,
                        `email` text DEFAULT NULL,
                        `endereco` text DEFAULT NULL,
                        `produto` text DEFAULT NULL, 
                        `quantidade` int(11) DEFAULT NULL

        );''')
    #DataBase Fornecedor
        self.conn.commit() #Confirma a criação da tabela
    def RegistrarNoBancoFornecedor(self,fornecedores,cpf,telefone,email,endereco,produto,quantidade):
        self.cursor.execute("INSERT INTO fornecedor(fornecedores, cpf, telefone, email, endereco, produto, quantidade) VALUES(%s, %s, %s, %s, %s, %s, %s)",(fornecedores, cpf, telefone, email, endereco, produto, quantidade)) #Insere os dados do usuario na tabela
        self.conn.commit() #Confirma a inserção dos dados
        self.conn.close()

    def alterarFornecedor(self,idfornecedor,fornecedores,cpf,telefone,email,endereco,produto,quantidade):
        self.cursor.execute("UPDATE fornecedor SET fornecedores=%s, cpf=%s, telefone=%s, email=%s, endereco=%s, produto=%s,quantidade=%s WHERE idfornecedor=%s",
                            (fornecedores,cpf,telefone,email,endereco,produto,quantidade,idfornecedor)) #Atualiza os dados do usuario com id oferecido
        self.conn.commit() #Confirma a atualização do dados 
        self.conn.close()
    def buscarFornecedor(self,idfornecedor):
        self.cursor.execute("SELECT * FROM fornecedor WHERE idfornecedor=%s",(idfornecedor,)) #Seleciona os dados do usuario com o id fornecido
        usuario = self.cursor.fetchone() #Retorna oos dados do usuario encontrado
        self.conn.commit()
        self.conn.close()
        return usuario
    def removerFornecedor(self,idfornecedor):
        self.cursor.execute("DELETE FROM fornecedor WHERE idfornecedor=%s", (idfornecedor,))
        self.conn.commit()
    
    def RegistrarNoBancofuncionario(self, cpf, nome, telefone, email, dataDeContratacao, cargo, salario, endereco):
        # Insere um novo funcionário no banco de dados
        self.cursor.execute("INSERT INTO funcionario(cpf, nome, telefone, email, dataDeContratacao, cargo, salario, endereco) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
                            (cpf, nome, telefone, email, dataDeContratacao, cargo, salario, endereco))
        self.conn.commit()  # Confirma a inserção dos dados

    def removerfuncionario(self,idfuncionario):
        self.cursor.execute("DELETE FROM funcionario WHERE idfuncionario=%s",(idfuncionario))
        self.conn.commit()

    def alterarfuncionario(self, idfuncionario, cpf, nome, telefone, email, dataDeContratacao, cargo, salario, endereco):
        self.cursor.execute("UPDATE funcionario SET cpf=%s, nome=%s, telefone=%s, email=%s, dataDeContratacao=%s, cargo=%s,salario=%s, endereco=%s WHERE idfuncionario=%s",
                            (cpf, nome, telefone, email, dataDeContratacao, cargo, salario, endereco, idfuncionario)) #Atualiza os dados do usuario com id oferecido
        self.conn.commit() #Confirma a atualização do dados 
        self.conn.close()

    def buscar_funcionario(self, id_funcionario):
        query = "SELECT * FROM funcionario WHERE id = %s"
        self.cursor.execute(query, (id_funcionario,))
        return self.cursor.fetchone() 
    

        # Metódo para registrar um novo usuario no banco de dados
    def RegistrarNoBanco_Produto(self, tipo, voltagem, marca, quantidade, preco, data):
        self.cursor.execute("INSERT INTO produto (tipo, voltagem, marca, quantidade, preco, data) VALUES (%s ,%s ,%s ,%s, %s, %s)",(tipo, voltagem, marca, quantidade, preco, data)) # Insere os dados do usuario na tabela
        self.conn.commit() # Confirma a inseção dos dados

    # Metodo para buscar os dados de um usuario no banco de dados
    def buscar_produto(self, idproduto):
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT* FROM produto WHERE idproduto = %s"
        self.cursor.execute(query, (idproduto,))
        conn.close()
        cursor.close()
        return buscar_produto()
    
