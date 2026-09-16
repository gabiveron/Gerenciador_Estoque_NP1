#CRUD Movimentacoes
from conexao import conexao
import pyodbc

def calcular_estoque(estoque_atual, quantidade, tipo):
    if tipo=="ENTRADA":
        estoque_atual= estoque_atual + quantidade
        return estoque_atual
    elif tipo=="SAIDA":
        estoque_atual= estoque_atual - quantidade
        return estoque_atual

def  cadastrar_movimentacao(id_produto, quantidade, tipo):
    try:
        cursor=conexao.cursor()
        cursor.execute("SELECT QuantidadeProduto FROM Produto WHERE IdProduto = ? AND Ativo = 1",
                    id_produto
                    )
        if quantidade <= 0:
            return "A quantidade deve ser maior que zero"

        resultado=cursor.fetchone()

        if resultado is None:
            return "Produto não encontrado"
        
        estoque_atual=resultado[0]

        if quantidade>estoque_atual and tipo=="SAIDA":
            return "Não temos a quantidade solicitada"

        novo_estoque= calcular_estoque(estoque_atual, quantidade, tipo)

        cursor.execute("UPDATE Produto SET QuantidadeProduto = ? WHERE IdProduto = ?",
                    novo_estoque,
                    id_produto
                    )

        cursor.execute("INSERT INTO Movimentacao(IdProduto, QntdMovimentacao, TipoMovimentacao) VALUES (?, ?, ?)",
                    id_produto,
                    quantidade,
                    tipo
                    )
        conexao.commit()
        return "Movimentação cadastrada com sucesso"
    except pyodbc.IntegrityError:
        conexao.rollback()
        return "A movimentação não foi cadastrada"

def listar_movimentacoes():
    try:
        cursor=conexao.cursor()
        cursor.execute("""SELECT IdMovimentacao, NomeProduto, QntdMovimentacao, TipoMovimentacao, DataMovimentacao 
        FROM Movimentacao 
        INNER JOIN Produto
        ON Movimentacao.IdProduto = Produto.IdProduto
        ORDER BY DataMovimentacao DESC
        """)
        movimentacoes=cursor.fetchall()
        return movimentacoes
    except:
        return None
