class Person: # Criado a classe Person


    def __init__(self, nome, idade): # Método construtor
        self.nome = nome
        self.idade = idade

    def __str__(self): # Método toString
        return f"Nome: {self.nome}, Idade: {self.idade}"

person = Person("Guilherme", 20) # Instanciando a classe Person
print(person)

    