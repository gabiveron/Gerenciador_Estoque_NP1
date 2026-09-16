import pyodbc

servidor="localhost"
banco="Gerenciador_Estoque"

conexao=pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={servidor};"
    f"DATABASE={banco};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)