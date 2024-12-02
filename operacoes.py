# Nome: Leonardo Capistrano de Sousa Silva
from cores import BOLD_BLUE, BOLD_GREEN, RESET
from funcoes import (
    conectar_mongo, 
    criar_colecoes, 
    inserir_varios_documentos, 
    inserir_documento,
    obter_id,
    atualizar_documento,
    encontrar_todos_livros,
    deletar_documento,
    consultar_documento
)

# conectando ao banco de dados ----------------------------------------------------------------------------------------
db = conectar_mongo()

# bucando coleções ----------------------------------------------------------------------------------------------------
livros, autores, categorias, pedidos = criar_colecoes(db)

# inserindo dado em autor -------------------------------------------------------------------------------------------

print(f"\n{BOLD_BLUE}Inserindo dados nas coleções{RESET}")
autor = {
    "nome": "George Orwell",
    "pais_origem": "Reino Unido",
    "biografia": "Autor de clássicos como '1984' e 'A Revolução dos Bichos', conhecido por suas críticas ao totalitarismo e às injustiças sociais."
}

inserir_documento(db, "autores", autor)

print("\n")
# inserindo dado em categoria -------------------------------------------------------------------------------------------
categorias_orwell = [
    {"nome": "Distopia", "descricao": "Obras que retratam sociedades opressivas e autoritárias."},
    {"nome": "Fábula Política", "descricao": "Histórias simbólicas que satirizam sistemas políticos."},
]

inserir_varios_documentos(db, "categorias", categorias_orwell)

# inserindo dados de livros -------------------------------------------------------------------------------------------
print(f"{BOLD_GREEN}Obter IDs dos autores e categorias{RESET}\n")
id_autor_orwell = obter_id(db, "autores", "nome", "George Orwell")
id_categoria_distopia = obter_id(db, "categorias", "nome", "Distopia")
id_categoria_fabula_politica = obter_id(db, "categorias", "nome", "Fábula Política")

livros_orwell = [
    {
        "titulo": "1984",
        "ano_publicacao": 1949,
        "preco": 49.90,
        "ids_autores": [id_autor_orwell],
        "ids_categorias": [id_categoria_distopia]
    },
    {
        "titulo": "A Revolução dos Bichos",
        "ano_publicacao": 1945,
        "preco": 39.90,
        "ids_autores": [id_autor_orwell],
        "ids_categorias": [id_categoria_fabula_politica]
    }
]
print("\n")
inserir_varios_documentos(db, "livros", livros_orwell)

# inserindo dados de pedidos -------------------------------------------------------------------------------------------
print(f"{BOLD_GREEN}Obter IDs das pedidos{RESET}\n")
id_livro_1984 = obter_id(db, "livros", "titulo", "1984")
id_livro_a_revolucao_dos_bichos = obter_id(db, "livros", "titulo", "A Revolução dos Bichos")

pedido = [
    {
    "nome_cliente": "Daniel Alves", 
    "itens": [{"id_livro": id_livro_1984, "quantidade": 1}], 
    "status": "pendente"
    },
    {
    "nome_cliente": "Neymar Junior",
    "itens": [{"id_livro": id_livro_a_revolucao_dos_bichos, "quantidade": 2}],
    "status": "concluído"
    }
]

print("\n")
inserir_varios_documentos(db, "pedidos", pedido)

# atualizando dados de autor -------------------------------------------------------------------------------------------
print(f"{BOLD_BLUE}Atualizando dados nas coleções{RESET}\n")
atualizar_documento(db, "autores", "nome", "George Orwell", {"biografia": "Autor de clássicos como '1984' e 'A Revolução dos Bichos', conhecido por suas críticas ao totalitarismo e às injustiças sociais. Seu verdadeiro nome é Eric Arthur Blair."})

# mostrando todos os livros -------------------------------------------------------------------------------------------
livros = livros.find()
encontrar_todos_livros(db, livros)

# deletando categoria -------------------------------------------------------------------------------------------------
deletar_documento(db, "categorias", "nome", "Realismo Mágico")

# deletando livro -----------------------------------------------------------------------------------------------------
deletar_documento(db, "livros", "titulo", "Cem Anos de Solidão")

# consultando lirvo de uma determinada categoria ----------------------------------------------------------------------
print(f'\n{BOLD_GREEN}Obter ID da categoria "Teatro Clássico"{RESET}')
id_categoria_realismo_magico = obter_id(db, "categorias", "nome", "Teatro Clássico")

print(f"\n{BOLD_BLUE}Consultando livros de uma categoria específica{RESET}")
consultar_documento(db, "livros", "ids_categorias", id_categoria_realismo_magico)

# consultando todos os pedidos de um cliente -------------------------------------------------------------------------
print(f"{BOLD_BLUE}Consultando pedidos de um cliente específico{RESET}\n")
consultar_documento(db, "pedidos", "nome_cliente", "José Pereira")

# consultar os livros publicados por um autor específico -------------------------------------------------------------
print(f"{BOLD_GREEN}Obter ID do autor 'George Orwell'{RESET}\n")
id_autor_gabriel_garcia_marquez = obter_id(db, "autores", "nome", "George Orwell")

print(f"\n{BOLD_BLUE}Consultando livros de um autor específico{RESET}\n")
consultar_documento(db, "livros", "ids_autores", id_autor_gabriel_garcia_marquez)

# Filtrar pedidos com status “pendente” ------------------------------------------------------------------------------
print(f"{BOLD_BLUE}Filtrando pedidos com status 'pendente'{RESET}\n")
consultar_documento(db, "pedidos", "status", "pendente")