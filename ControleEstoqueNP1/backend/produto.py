#CRUD Produto
from conexao import conexao
import pyodbc

def cadastrar_produto(nome, localizacao, id_categoria, id_fornecedor):
    try:
        cursor=conexao.cursor()
        cursor.execute("INSERT INTO Produto (NomeProduto, Localizacao, IdCategoria, IdFornecedor) VALUES (?, ?, ?, ?)",
                           nome,
                           localizacao,
                           id_categoria,
                           id_fornecedor
                           )
        conexao.commit()
        return "Produto cadastrado com sucesso"
    except pyodbc.IntegrityError:
        conexao.rollback()
        return "Não foi possível cadastrar o produto"

def listar_produtos():
    try:
        cursor=conexao.cursor()
        cursor.execute("SELECT * FROM Produto WHERE Ativo = 1 ORDER BY IdProduto ASC")
        produtos=cursor.fetchall()
        return produtos
    except:
        return None

def atualizar_produto(id_produto, nome, localizacao, id_categoria, id_fornecedor):
    try:
        cursor=conexao.cursor()
        cursor.execute("UPDATE Produto SET NomeProduto = ?, Localizacao = ?, IdCategoria = ?, IdFornecedor = ? WHERE IdProduto = ?",
                       nome,
                       localizacao,
                       id_categoria,
                       id_fornecedor,
                       id_produto
                       )
        if cursor.rowcount>0:
            conexao.commit()
            return "Cadastro atualizado com sucesso"
        else:
            return "Produto não encontrado"
    except pyodbc.IntegrityError:
        return "Não foi possível atualizar o produto"

def excluir_produto(id_produto):
    try:
        cursor=conexao.cursor()
        cursor.execute("UPDATE Produto SET Ativo = 0 WHERE IdProduto = ? AND Ativo = 1",
                       id_produto
                       )
        if cursor.rowcount>0:
            conexao.commit()
            return "Produto excluído com sucesso"
        else:
            return "Produto não encontrado"
    except pyodbc.IntegrityError:
        return "Não foi possível excluir o produto"