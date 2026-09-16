from http.server import HTTPServer, BaseHTTPRequestHandler
from produto import listar_produtos, cadastrar_produto, atualizar_produto, excluir_produto
from categoria import listar_categorias, cadastrar_categoria, atualizar_categoria, excluir_categoria
from fornecedor import listar_fornecedores, cadastrar_fornecedor, atualizar_fornecedor, excluir_fornecedor
from movimentacoes import listar_movimentacoes, cadastrar_movimentacao
import json

class Servidor(BaseHTTPRequestHandler):
    
    def do_OPTIONS(self): #libera as requisições vindas do navegador
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):   #mandar informaçoes pro front
#--------------------GET PRODUTO----------------------
        if self.path=="/produtos":
            produtos = listar_produtos() #pega return da funçao e salva na variavel
            if produtos is None:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
            else:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                produtos_formatados=[] #cria uma lista para guardar os produtos passados no dicionario
                for produto in produtos: # pega produto por produto e passa no dicionario
                    produto_dicionario={
                        "id_produto": produto[0],
                        "nome": produto[1],
                        "quantidade": produto[2],
                        "localizacao": produto[3],
                        "id_categoria": produto[4],
                        "id_fornecedor": produto[5]
                        }
                    produtos_formatados.append(produto_dicionario) # adicionando os produtos passados
                produto_json=json.dumps(produtos_formatados) #transforma o formato de produtos em formato json
                self.wfile.write(produto_json.encode()) #transforma a informação em bytes e envia de volta

#--------------------GET CATEGORIA----------------------
        if self.path=="/categorias":
            categorias = listar_categorias()
            if categorias is None:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
            else:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                categorias_formatadas=[]
                for categoria in categorias:
                    categoria_dicionario={
                        "id_categoria": categoria[0],
                        "nome": categoria[1],
                        }
                    categorias_formatadas.append(categoria_dicionario)
                categoria_json=json.dumps(categorias_formatadas)
                self.wfile.write(categoria_json.encode())

#--------------------GET FORNECEDOR----------------------
        if self.path=="/fornecedores":
            fornecedores = listar_fornecedores() 
            if fornecedores is None:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
            else:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                fornecedores_formatados=[] 
                for fornecedor in fornecedores:
                    fornecedor_dicionario={
                        "id_fornecedor": fornecedor[0],
                        "nome": fornecedor[1],
                        "documento": fornecedor[2],
                        "telefone": fornecedor[3],
                        "localidade": fornecedor[4]
                        }
                    fornecedores_formatados.append(fornecedor_dicionario)
                fornecedor_json=json.dumps(fornecedores_formatados)
                self.wfile.write(fornecedor_json.encode())

#--------------------GET MOVIMENTACAO----------------------
        if self.path=="/movimentacoes":
            movimentacoes = listar_movimentacoes()
            if movimentacoes is None:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
            else:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                movimentacoes_formatadas=[]
                for movimentacao in movimentacoes:
                    movimentacao_dicionario={
                        "id_movimentacao": movimentacao[0],
                        "nome_produto": movimentacao[1],
                        "quantidade": movimentacao[2],
                        "tipo": movimentacao[3],
                        "data": movimentacao[4].isoformat(),
                        }
                    movimentacoes_formatadas.append(movimentacao_dicionario)
                movimentacao_json=json.dumps(movimentacoes_formatadas)
                self.wfile.write(movimentacao_json.encode())


    def do_POST(self):  #inserir informaçoes no banco
#--------------------POST PRODUTO----------------------
        if self.path=="/produtos":
            tamanho=int(self.headers["Content-Length"]) #tamanho da requisição
            dados=self.rfile.read(tamanho) #pega a quantidade de bytes enviados
            dados=dados.decode("utf-8") #transforma bytes em string
            dados=json.loads(dados) #pega o formato que esta em json e devolve em dicionario
            resultado=cadastrar_produto(
                dados["nome"],
                dados["localizacao"],
                dados["id_categoria"],
                dados["id_fornecedor"]
            )
            if resultado== "Produto cadastrado com sucesso":
                self.send_response(200)
            else:
                self.send_response(400)

            resultado=json.dumps(resultado)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(resultado.encode())

#--------------------POST CATEGORIA----------------------
        if self.path=="/categorias":
            tamanho=int(self.headers["Content-Length"])
            dados=self.rfile.read(tamanho)
            dados=dados.decode("utf-8")
            dados=json.loads(dados)
            resultado=cadastrar_categoria(
                dados["nome"]
            )
            if resultado== "Categoria cadastrada com sucesso":
                self.send_response(200)
            else:
                self.send_response(400)

            resultado=json.dumps(resultado)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(resultado.encode())

#--------------------POST FORNECEDOR----------------------
        if self.path=="/fornecedores":
            tamanho=int(self.headers["Content-Length"])
            dados=self.rfile.read(tamanho)
            dados=dados.decode("utf-8")
            dados=json.loads(dados)
            resultado=cadastrar_fornecedor(
                dados["nome"],
                dados["documento"],
                dados["telefone"],
                dados["localidade"]
            )
            if resultado== "Fornecedor cadastrado com sucesso":
                self.send_response(200)
            else:
                self.send_response(400)

            resultado=json.dumps(resultado)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(resultado.encode())

#--------------------POST MOVIMENTACAO----------------------
        if self.path=="/movimentacoes":
            tamanho=int(self.headers["Content-Length"])
            dados=self.rfile.read(tamanho)
            dados=dados.decode("utf-8")
            dados=json.loads(dados)
            resultado=cadastrar_movimentacao(
                dados["id_produto"],
                dados["quantidade"],
                dados["tipo"]
            )
            if resultado== "Movimentação cadastrada com sucesso":
                self.send_response(200)
            else:
                self.send_response(400)

            resultado=json.dumps(resultado)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(resultado.encode())


    def do_PUT(self):
#--------------------PUT PRODUTO----------------------
        if self.path.startswith("/produtos/"):
            id_produto=int(self.path.split("/")[2])
            tamanho=int(self.headers["Content-Length"])
            dados=self.rfile.read(tamanho)
            dados = dados.decode("utf-8")
            dados = json.loads(dados)
            
            resultado = atualizar_produto(
                id_produto,
                dados["nome"],
                dados["localizacao"],
                dados["id_categoria"],
                dados["id_fornecedor"]
            )
            
            if resultado == "Cadastro atualizado com sucesso":
                self.send_response(200)
            else:
                self.send_response(400)

            resultado = json.dumps(resultado)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(resultado.encode())

#--------------------PUT CATEGORIA----------------------
        if self.path.startswith("/categorias/"):
            id_categoria = int(self.path.split("/")[2])
            tamanho = int(self.headers["Content-Length"])
            dados = self.rfile.read(tamanho)
            dados = dados.decode("utf-8")
            dados = json.loads(dados)
            
            resultado = atualizar_categoria(id_categoria, dados["nome"])
            
            if resultado == "Categoria atualizada com sucesso":
                self.send_response(200)
            else:
                self.send_response(400)

            resultado = json.dumps(resultado)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(resultado.encode())

#--------------------PUT FORNECEDOR----------------------
        if self.path.startswith("/fornecedores/"):
            id_fornecedor = int(self.path.split("/")[2])
            tamanho = int(self.headers["Content-Length"])
            dados = self.rfile.read(tamanho)
            dados = dados.decode("utf-8")
            dados = json.loads(dados)
            
            resultado = atualizar_fornecedor(
                id_fornecedor,
                dados["nome"],
                dados["documento"],
                dados["telefone"],
                dados["localidade"]
            )
            
            if resultado == "Fornecedor atualizado com sucesso":
                self.send_response(200)
            else:
                self.send_response(400)

            resultado = json.dumps(resultado)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(resultado.encode())


    def do_DELETE(self):
#--------------------DELETE PRODUTO----------------------
        if self.path.startswith("/produtos/"):
            id_produto = int(self.path.split("/")[2])
            resultado = excluir_produto(id_produto)
            
            if resultado == "Produto excluído com sucesso":
                self.send_response(200)
            else:
                self.send_response(400)

            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            resultado = json.dumps(resultado)
            self.wfile.write(resultado.encode())

#--------------------DELETE CATEGORIA----------------------
        if self.path.startswith("/categorias/"):
            id_categoria = int(self.path.split("/")[2])
            resultado = excluir_categoria(id_categoria)
            
            if resultado == "Categoria excluída com sucesso":
                self.send_response(200)
            else:
                self.send_response(400)

            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            resultado = json.dumps(resultado)
            self.wfile.write(resultado.encode())

#--------------------DELETE FORNECEDOR----------------------
        if self.path.startswith("/fornecedores/"):
            id_fornecedor = int(self.path.split("/")[2])
            resultado = excluir_fornecedor(id_fornecedor)
            
            if resultado == "Fornecedor excluído com sucesso":
                self.send_response(200)
            else:
                self.send_response(400)

            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            resultado = json.dumps(resultado)
            self.wfile.write(resultado.encode())


# Inicialização do Servidor
servidor = HTTPServer(("localhost", 8000), Servidor)
servidor.serve_forever()