#CRUD Categoria
from conexao import conexao
import pyodbc

def cadastrar_categoria(nome):
    try:
        cursor=conexao.cursor()
        cursor.execute("INSERT INTO Categoria(Nome) VALUES (?)",
                       nome
                       )
        conexao.commit()
        return "Categoria cadastrada com sucesso"
    except pyodbc.IntegrityError:
        return "Não foi possível cadastrar a categoria"

def listar_categorias():
    try:
        cursor=conexao.cursor()
        cursor.execute("SELECT * FROM Categoria WHERE Ativo = 1 ORDER BY IdCategoria ASC")
        categorias=cursor.fetchall()
        return categorias
    except:
        return None

def atualizar_categoria(id_categoria, nome):
    try:
        cursor=conexao.cursor()
        cursor.execute("UPDATE Categoria SET Nome = ? WHERE IdCategoria = ?",
                    nome,
                    id_categoria
                    )
        if cursor.rowcount>0:
            conexao.commit()
            return "Categoria atualizada com sucesso"
        else:
             return "Categoria não encontrada"
    except pyodbc.IntegrityError:
         return "Já existe uma categoria com esse nome"

def excluir_categoria(id_categoria):
    try:
        cursor=conexao.cursor()
        cursor.execute("UPDATE Categoria SET Ativo = 0 WHERE IdCategoria = ? AND Ativo = 1",
                       id_categoria
                       )
        if cursor.rowcount>0:
                conexao.commit()
                return "Categoria excluída com sucesso"
        else:
             return "Categoria não encontrada"
                
    except pyodbc.IntegrityError:
        return "Não é possível excluir a categoria porque ela está vinculada a um produto"
