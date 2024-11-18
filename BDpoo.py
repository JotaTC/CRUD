import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='bd_poo',

)

cursor = conexao.cursor()
#CRUD

        #CREATE

#Função para criar variavéis dentro do banco de dados

#nome_produto = "Açucar"
#valor = 5

#comando = f'INSERT INTO vendas(nome_produto, valor) VALUES ("{nome_produto}", {valor})'
#cursor.execute(comando)
#conexao.commit()
#resultado = cursor.fetchall()


#READ

#Função de leitura das informações dentro do banco de dados

#comando = f'SELECT * FROM vendas'
#cursor.execute(comando)
#conexao.commit()
#resultado = cursor.fetchall()
#print(resultado)

#UPDATE

#Função para atualizar dados existentes dentro do banco de dados

#nome_produto = "Peito de Frango"
#valor = 29
#comando = f'UPDATE vendas SET valor = {valor} where nome_produto= "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit()

#DELETE

#Função para deletar informações dentro do banco de dados

#nome_produto = "Peito de Frango"
#valor = 69
#comando = f'DELETE FROM vendas where nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit()

cursor.close()
conexao.close()