#CRUD Fornecedor
from conexao import conexao
import pyodbc

def cadastrar_fornecedor(nome, documento, telefone, localidade):
    try:
        cursor=conexao.cursor()
        cursor.execute("INSERT INTO Fornecedor(Nomefornecedor, Documento, Telefone, Localidade) VALUES(?, ?, ?, ?) ", 
                       nome,
                       documento,
                       telefone,
                       localidade
                       )
        conexao.commit()
        return "Fornecedor cadastrado com sucesso"
    except pyodbc.IntegrityError:
        return "Já existe um cadastro com esse documento"

def listar_fornecedores():
    try:
        cursor=conexao.cursor()
        cursor.execute("SELECT * FROM Fornecedor WHERE Ativo = 1 ORDER BY IdFornecedor ASC")
        fornecedores= cursor.fetchall()
        return fornecedores
    except:
        return None

def atualizar_fornecedor(id_fornecedor, nome, documento, telefone, localidade):
    try:
        cursor=conexao.cursor()
        cursor.execute("UPDATE Fornecedor SET NomeFornecedor = ?, Documento = ?, Telefone = ?, Localidade = ? WHERE IdFornecedor = ?",
                       nome,
                       documento,
                       telefone,
                       localidade,
                       id_fornecedor
                       )
        if cursor.rowcount>0:
            conexao.commit()
            return "Fornecedor atualizado com sucesso"
        else:
            return "Fornecedor não encontrado"
    except pyodbc.IntegrityError:
        return "Já existe um cadastro com esse documento"

def excluir_fornecedor(id_fornecedor):
    try:
        cursor=conexao.cursor()
        cursor.execute("UPDATE Fornecedor SET Ativo = 0 WHERE IdFornecedor = ? AND Ativo = 1",
                       id_fornecedor
                       )
        if cursor.rowcount>0:
                conexao.commit()
                return "Fornecedor excluído com sucesso"
        else:
            return "Fornecedor não encontrado"   
    except pyodbc.IntegrityError:
        return "Não é possível excluir o fornecedor porque ele está vinculado a um produto"
