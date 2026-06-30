import sqlite3


def conectar():
    return sqlite3.connect("biblioteca.db")


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        disponivel INTEGER DEFAULT 1
    )
    """)

    conn.commit()
    conn.close()

def cd_livro(titulo, autor):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO livros (titulo, autor)
    VALUES (?, ?)
    """, (titulo, autor))

    conn.commit()
    conn.close()


def exibir_livros():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    conn.close()
    return livros


def emprestar_livro(id_livro):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE livros
    SET disponivel = 0
    WHERE id = ? AND disponivel = 1
    """, (id_livro,))

    conn.commit()
    alterado = cursor.rowcount
    conn.close()

    return alterado > 0



def devolver_livro(id_livro):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE livros
    SET disponivel = 1
    WHERE id = ?
    """, (id_livro,))

    conn.commit()
    alterado = cursor.rowcount
    conn.close()                    

    return alterado > 0 


def remover_livro(id_livro):
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    cursor.execute("""DELETE FROM livros WHERE id = ?""",
                    (id_livro,))
    
    removido = cursor.rowcount > 0
    conn.commit()
    conn.close()

    return True


