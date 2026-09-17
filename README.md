# Sistema de Controle de Estoque

## 1. Identificação Institucional
* *Curso:* Ciência da Computação
* *Turma:* CC4P17
  * Gabriel Zaneti Veronezzi - RA: H4235G6
  * Gustavo Ayres de Meira - RA: R601GJ3



## 2. Descrição do Projeto
O presente projeto consiste em um Sistema de Gerenciamento de Estoque construído para controlar de forma eficiente o fluxo de mercadorias. A arquitetura foi desenvolvida respeitando estritamente as restrições da NP1:
* *Lógica de Negócio e Back-end:* Desenvolvido em Python puro utilizando bibliotecas nativas (http.server), sem o uso de frameworks. A comunicação com o banco de dados é feita de forma direta via pyodbc.
* *Front-end:* Interface estruturada exclusivamente com HTML5, CSS3, Bootstrap 5 para responsividade e Vanilla JavaScript para o consumo da API via Fetch. Não foram utilizadas bibliotecas SPA.

### Regras de Negócio e Escopo Funcional

## Regras de Negócio

- Produtos devem possuir nome, localização, categoria e fornecedor.
- A quantidade inicial de um produto é 0.
- O nome do produto e o documento do fornecedor devem ser únicos.
- O estoque não pode possuir quantidade negativa.
- Entradas aumentam e saídas diminuem a quantidade em estoque.
- Não é permitida uma saída maior que o estoque disponível.
- Movimentações devem possuir quantidade maior que 0 e tipo `ENTRADA` ou `SAIDA`.
- A exclusão de produtos, categorias e fornecedores é realizada de forma lógica, mantendo os registros no banco de dados.

## Funcionalidades

### 📊 Painel de Controle
* **Resumo do Sistema:** Indicadores numéricos em tempo real exibindo o Total de Produtos e o total de Categorias Ativas.
* **Métricas do Dia:** Monitoramento do volume de Entradas Hoje e Saídas Hoje.
* **Acesso Rápido:** Links diretos para os módulos de Catálogo de Produtos, Movimentações e Fornecedores.

### 📦 Catálogo de Produtos
* **Gerenciamento Completo:** Cadastro, consulta, edição e exclusão lógica de produtos (identificados por nome e localização).

### 🔄 Movimentações de Estoque
* **Fluxo de Caixa:** Registro de novas entradas e saídas com validação de saldo para impedir estoque negativo.
* **Histórico:** Consulta ao histórico completo de movimentações do sistema.

### 🚚 Cadastros Auxiliares
* **Fornecedores:** Gerenciamento de empresas e parceiros integrados ao catálogo.
* **Categorias:** Organização estruturada para a classificação dos itens.

## 3. Modelagem de Dados

### Diagrama Entidade-Relacionamento (DER)
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/6b3e2b99-40e0-42ae-9ea5-6735f4484e9a" />


### Scripts DDL (Criação do Banco de Dados - SQL Server)
```sql
CREATE DATABASE Gerenciador_Estoque;
GO
USE Gerenciador_Estoque;
GO
CREATE TABLE Categoria(
	IdCategoria int IDENTITY(1,1) NOT NULL,
	Nome varchar(50) NOT NULL,
	Ativo bit NULL,
	CONSTRAINT PK_Categoria PRIMARY KEY (IdCategoria),
	CONSTRAINT UQ_Categoria_Nome UNIQUE (Nome),
	CONSTRAINT DF_Categoria_Ativo DEFAULT 1 FOR Ativo
);

CREATE TABLE Fornecedor(
	IdFornecedor int IDENTITY(1,1) NOT NULL,
	NomeFornecedor varchar(50) NOT NULL,
	Documento varchar(14) NOT NULL,
	Telefone varchar(11) NOT NULL,
	Localidade varchar(50) NOT NULL,
	Ativo bit NULL,
	CONSTRAINT PK_Fornecedor PRIMARY KEY (IdFornecedor),
	CONSTRAINT UQ_Fornecedor_Documento UNIQUE (Documento),
	CONSTRAINT DF_Fornecedor_Ativo DEFAULT 1 FOR Ativo
);

CREATE TABLE Produto(
	IdProduto int IDENTITY(1,1) NOT NULL,
	NomeProduto varchar(50) NOT NULL,
	QuantidadeProduto int NOT NULL,
	Localizacao varchar(50) NOT NULL,
	IdCategoria int NOT NULL,
	IdFornecedor int NOT NULL,
	Ativo bit NULL,
	CONSTRAINT PK_Produto PRIMARY KEY (IdProduto),
	CONSTRAINT UQ_Produto_Nome UNIQUE (NomeProduto),
	CONSTRAINT FK_Produto_Categoria FOREIGN KEY (IdCategoria) REFERENCES Categoria(IdCategoria),
	CONSTRAINT FK_Produto_Fornecedor FOREIGN KEY (IdFornecedor) REFERENCES Fornecedor(IdFornecedor),
	CONSTRAINT DF_Produto_Ativo DEFAULT 1 FOR Ativo
);

CREATE TABLE Movimentacao(
	IdMovimentacao int IDENTITY(1,1) NOT NULL,
	IdProduto int NOT NULL,
	QntdMovimentacao int NOT NULL,
	TipoMovimentacao varchar(7) NOT NULL,
	DataMovimentacao datetime NULL,
	CONSTRAINT PK_Movimentacao PRIMARY KEY (IdMovimentacao),
	CONSTRAINT FK_Movimentacao_Produto FOREIGN KEY (IdProduto) REFERENCES Produto(IdProduto),
	CONSTRAINT DF_Movimentacao_Data DEFAULT GETDATE() FOR DataMovimentacao
);
```
## 4. Guia de Instalação e Execução

### Pré-requisitos
* **Linguagem:** Python 3.x instalado.
* **Banco de Dados:** Microsoft SQL Server em execução local.
* **Driver de Conexão:** ODBC Driver 18 for SQL Server.

### Passo a Passo para Configuração e Execução

#### 1. Clonagem e Banco de Dados
1. Clone o repositório em sua máquina local:
   ```bash
   git clone https://github.com/gabiveron/Gerenciador_Estoque_NP1.git
   ```
2. Abra o **SQL Server Management Studio (SSMS)** (ou equivalente).
3. Execute os scripts DDL da seção 3 para criar o banco de dados `Gerenciador_Estoque` e suas respectivas tabelas.

#### 2. Configuração das Dependências (Back-end)
1. Pelo terminal, acesse a pasta raiz do back-end do projeto.
2. Instale o driver de comunicação com o banco de dados executando:
   ```bash
   pip install pyodbc
   ```

#### 3. Execução do Servidor (Back-end)
1. No mesmo terminal da pasta back-end, inicie a API com o comando:
   ```bash
   python servidor.py
   ```
2. O servidor iniciará localmente na porta `8000`.

#### 4. Execução da Interface (Front-end)
1. Navegue até a pasta que contém os arquivos de front-end.
2. Abra o arquivo `index.html` em um navegador web atualizado (ou utilize extensões como o **Live Server** do VS Code).
3. O sistema estará pronto para uso. Navegue pelo menu superior para realizar as operações de CRUD.

---

## 5. Evidências Visuais

Abaixo estão as capturas de tela comprovando a interface funcional e a persistência de dados (exemplos sugeridos para comprovar a execução estável do sistema):

### Tela Inicial da Interface
<img width="1350" height="639" alt="image" src="https://github.com/user-attachments/assets/7a667ab3-a79e-46d5-af0b-ccebe1b3eb9c" />
)

### Telas dos Módulos
<img width="835" height="407" alt="image" src="https://github.com/user-attachments/assets/223d5bcf-b524-4002-be14-319a51591afd" />

### Telas de Cadastro / CRUD Create
<img width="900" height="420" alt="image" src="https://github.com/user-attachments/assets/ee4071ac-ec5e-4079-aa46-8ce0040b1af6" />

### Telas de Listagem / CRUD Read
<img width="984" height="448" alt="image" src="https://github.com/user-attachments/assets/27c06493-db2d-463f-9224-89c297bb53d9" /> 
### Telas de Edição / CRUD Update





