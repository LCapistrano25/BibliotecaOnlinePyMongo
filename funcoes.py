# Nome: Leonardo Capistrano de Sousa Silva
from pymongo import MongoClient, errors
from cores import BOLD_BLACK, BOLD_BLUE, BOLD_CYAN, BOLD_GREEN, BOLD_MAGENTA, BOLD_RED, BOLD_WHITE, BOLD_YELLOW, RESET

# Função para conectar ao banco de dados MongoDB ----------------------------------------------------------------------
def conectar_mongo():
    try:
        cliente = MongoClient("mongodb://localhost:27017/")
        db = cliente["livraria_online"]
        print("\nConectado ao banco:", db)    
        return db
    except errors.ConnectionError as e:
        print("\nErro de conexão:", e)
    except Exception as e:
        print("\nOutro erro ocorreu:", e)

# Função para criar coleções no banco de dados ------------------------------------------------------------------------
def criar_colecoes(db):
    return db.get_collection('livros'), db.get_collection('autores'), db.get_collection('categorias'), db.get_collection('pedidos')

# Função para inserir dados nas coleções do banco de dados ------------------------------------------------------------
def inserir_varios_documentos(db, colecao, dados):
    collection = db[colecao]
    collection.insert_many(dados)
    
    print(f"{BOLD_YELLOW}Documentos inseridos na coleção '{colecao}':{RESET}\n")
    for dado in dados:
        for key, value in dado.items():
            print(f"{key}: {value}")
        print("\n")


# Função para obter o ID de um documento no banco de dados -----------------------------------------------------------
def obter_id(db, colecao, campo, valor):
    collection = db[colecao]
    documento = collection.find_one({campo: valor})
    
    if documento:
        id = documento["_id"]
        print(f"ID do documento com '{campo}' igual a '{valor}': {BOLD_MAGENTA}{id}{RESET}", )
        return id
    else:
        print("\nNenhum documento encontrado com '{}' igual a '{}'.".format(campo, valor))
        return None

# Função para inserir dados nas coleções do banco de dados ------------------------------------------------------------
def inserir_documento(db, colecao, dado):
    collection = db[colecao]
    collection.insert_one(dado)
    
    print(f"\n{BOLD_YELLOW}Documento inserido na coleção '{colecao}':{RESET}\n")
    for key, value in dado.items():
        print(f"{key}: {value}")

# Função para atualizar um documento no banco de dados ----------------------------------------------------------------
def atualizar_documento(db, colecao, campo, valor, novo_valor):
    collection = db[colecao]
    collection.update_one({campo: valor}, {"$set": novo_valor})
    documento_atualizado = collection.find_one({campo: valor})
    print(f"{BOLD_YELLOW}Documento atualizado na coleção '{colecao}':{RESET}\n")
    for key, documento in documento_atualizado.items():
        print(f"{key}: {documento}")

# Função para mostrar todos os livros ----------------------------------------------------------------------------------

def encontrar_todos_livros(db, livros):
    print(f"\n{BOLD_BLUE}Todos os livros na coleção 'livros':{RESET}\n")
    for livro in livros:
        print(f"Título: {livro['titulo']}")
        print(f"Ano de Publicação: {livro['ano_publicacao']}")
        print(f"Preço: R$ {livro['preco']:.2f}")

        # Exibir autores relacionados
        autores_ids = livro.get("ids_autores", [])
        autores_nomes = [db.autores.find_one({"_id": autor_id})["nome"] for autor_id in autores_ids]
        print(f"Autores: {', '.join(autores_nomes)}")

        # Exibir categorias relacionadas
        categorias_ids = livro.get("ids_categorias", [])
        categorias_nomes = [db.categorias.find_one({"_id": categoria_id})["nome"] for categoria_id in categorias_ids]
        print(f"Categorias: {', '.join(categorias_nomes)}")
        print("-" * 40)  # Separador entre livros

# Função para deletar um documento no banco de dados ------------------------------------------------------------------
def deletar_documento(db, colecao, campo, valor):
    collection = db[colecao]
    collection.delete_one({campo: valor})
    print(f"{BOLD_RED}\nDocumento deletado da coleção '{colecao}':{RESET}")
    print(f"{campo}: {valor}")
    print(f"{collection}")

# Função para consultar um documento no banco de dados ----------------------------------------------------------------
def consultar_documento(db, colecao, campo, valor):
    collection = db[colecao]
    documentos = collection.find_one({campo: valor})
    if documentos:
        print(f"{BOLD_YELLOW}Documentos encontrados na coleção '{colecao}':{RESET}\n")
        for key, documento in documentos.items():
            print(f"{key}: {documento}")
        print("\n")