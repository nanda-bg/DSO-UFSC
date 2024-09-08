from Sistema import Sistema
from LivroCategoriaAutor.Livro import Livro
from AmigoContato.Amigo import Amigo


# Instancia a classe Sistema
sistema = Sistema()

# Cria instâncias de Amigo
amigo1 = Amigo("João", "1234-5678", "joao@example.com")
amigo2 = Amigo("Maria", "8765-4321", "maria@example.com")

# Cadastra amigos no sistema
sistema.cadastrar_amigo(amigo1)
sistema.cadastrar_amigo(amigo2)

# Cria instâncias de Livro
livro1 = Livro("1984", "Distopia", "George Orwell", ("Ficção", "Adulto"), "Winston")
livro2 = Livro("O Hobbit", "Aventura", "J.R.R. Tolkien", ("Fantasia", "Todos"), "Bilbo")
livro3 = Livro("Brave New World", "Futuro distópico", "Aldous Huxley", ("Ficção", "Adulto"), "Bernard Marx")
livro4 = Livro("O Senhor dos Anéis", "Fantasia épica", "J.R.R. Tolkien", ("Fantasia", "Todos"), "Frodo")
livro5 = Livro("A Revolução dos Bichos", "Sátira política", "George Orwell", ("Ficção", "Adulto"), "Napoleon")

# Cadastra livros no sistema
sistema.cadastrar_livro(livro1)
sistema.cadastrar_livro(livro2)
sistema.cadastrar_livro(livro3)
sistema.cadastrar_livro(livro4)
sistema.cadastrar_livro(livro5)

# Registra empréstimos
sistema.registrar_emprestimo(amigo1, livro1)
sistema.registrar_emprestimo(amigo1, livro3)
sistema.registrar_emprestimo(amigo1, livro5)
sistema.registrar_emprestimo(amigo2, livro2)
sistema.registrar_emprestimo(amigo2, livro4)

# Lista todos os empréstimos
print("Todos os Empréstimos:")
for emprestimo in sistema.listar_emprestimos():
    print(emprestimo)

# Lista livros emprestados ao amigo João
print("\nLivros emprestados ao João:")
livros_do_joao = sistema.livros_com_amigos(amigo1)
for livro in livros_do_joao:
    print(livro)