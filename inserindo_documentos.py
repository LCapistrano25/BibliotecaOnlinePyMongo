# Nome: Leonardo Capistrano de Sousa Silva
from funcoes import (
    conectar_mongo, 
    criar_colecoes, 
    inserir_varios_documentos, 
    obter_id
)
from dados import (
    dados_autores, 
    dados_categorias
)

from cores import BOLD_BLACK, BOLD_BLUE, BOLD_CYAN, BOLD_GREEN, BOLD_MAGENTA, BOLD_RED, BOLD_WHITE, BOLD_YELLOW, RESET

print(f"\n{BOLD_BLUE}Inserindo dados nas coleções{RESET}")

# conectando ao banco de dados ----------------------------------------------------------------------------------------
db = conectar_mongo()

# criando coleções ----------------------------------------------------------------------------------------------------
livros, autores, categorias, pedidos = criar_colecoes(db)

print(f"\n{BOLD_YELLOW}Coleções criadas:{RESET}\n")
print("Livros:", livros)
print("Autores:", autores)
print("Categorias:", categorias)
print("Pedidos:", pedidos)

# inserindo dados de autores -------------------------------------------------------------------------------------------
print('\n')
inserir_varios_documentos(db, "autores", dados_autores)

# inserindo dados de categorias ----------------------------------------------------------------------------------------
inserir_varios_documentos(db, "categorias", dados_categorias)

# inserindo dados de livros -------------------------------------------------------------------------------------------
print(f"{BOLD_GREEN}Obter IDs das categorias{RESET}\n")
id_categoria_realismo_magico = obter_id(db, "categorias", "nome", "Realismo Mágico")
id_categoria_teatro_classico = obter_id(db, "categorias", "nome", "Teatro Clássico")
id_categoria_misterio_policial = obter_id(db, "categorias", "nome", "Mistério e Policial")
id_categoria_romance_epico = obter_id(db, "categorias", "nome", "Romance Épico")

# dados dos autores ---------------------------------------------------------------------------------------------------
print(f"\n{BOLD_GREEN}Obter IDs dos autores{RESET}\n")
id_autor_gabriel_garcia_marquez = obter_id(db, "autores", "nome", "Gabriel García Márquez")
id_autor_william_shakespeare = obter_id(db, "autores", "nome", "William Shakespeare")
id_autor_agatha_christie = obter_id(db, "autores", "nome", "Agatha Christie")
id_autor_leo_tolstoi = obter_id(db, "autores", "nome", "Leo Tolstói")

# dados dos livros ----------------------------------------------------------------------------------------------------
print(f"\n{BOLD_RED}Dados em embedding{RESET}")
livros = [
    {
        "titulo": "Cem Anos de Solidão",
        "ano_publicacao": 1967,
        "preco": 59.90,
        "ids_autores": [id_autor_gabriel_garcia_marquez],
        "ids_categorias": [id_categoria_realismo_magico]
    },
    {
        "titulo": "Romeu e Julieta",
        "ano_publicacao": 1597,
        "preco": 39.90,
        "ids_autores": [id_autor_william_shakespeare],
        "ids_categorias": [id_categoria_teatro_classico]
    },
    {
        "titulo": "Assassinato no Expresso do Oriente",
        "ano_publicacao": 1934,
        "preco": 45.90,
        "ids_autores": [id_autor_agatha_christie],
        "ids_categorias": [id_categoria_misterio_policial]
    },
    {
        "titulo": "Guerra e Paz",
        "ano_publicacao": 1869,
        "preco": 89.90,
        "ids_autores": [id_autor_leo_tolstoi],
        "ids_categorias": [id_categoria_romance_epico]
    }
]

# inserindo dados de livros -------------------------------------------------------------------------------------------
inserir_varios_documentos(db, "livros", livros)

# inserindo dados de pedidos ------------------------------------------------------------------------------------------
print(f"{BOLD_GREEN}Obter IDs dos livros{RESET}\n")
id_livro_cem_anos_de_solidao = obter_id(db, "livros", "titulo", "Cem Anos de Solidão")
id_livro_romeu_e_julieta = obter_id(db, "livros", "titulo", "Romeu e Julieta")
id_livro_assinaro_no_expresso_do_oriente = obter_id(db, "livros", "titulo", "Assassinato no Expresso do Oriente")
id_livro_guerra_e_paz = obter_id(db, "livros", "titulo", "Guerra e Paz")

# dados dos pedidos ---------------------------------------------------------------------------------------------------
print(f"\n{BOLD_RED}Dados em linking{RESET}")
pedidos = [
    {
        "nome_cliente": "José Pereira", 
        "itens": [{"id_livro": id_livro_cem_anos_de_solidao, "quantidade": 3}], 
        "status": "concluído"
    },
    {
        "nome_cliente": "Leonardo Silva", 
        "itens": [{"id_livro": id_livro_romeu_e_julieta, "quantidade": 1}, {"id_livro": id_livro_guerra_e_paz, "quantidade": 2}], 
        "status": "em andamento"
    },
    {
        "nome_cliente": "João Souza", 
        "itens": [{"id_livro": id_livro_assinaro_no_expresso_do_oriente, "quantidade": 2}], 
        "status": "cancelado"
    }
]

# inserindo dados de pedidos ------------------------------------------------------------------------------------------
inserir_varios_documentos(db, "pedidos", pedidos)