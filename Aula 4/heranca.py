class Person: # Criado a classe Person
    def __init__(self, nome, idade): # Método construtor
        self.nome = nome
        self.idade = idade

    def __str__(self): # Método toString
        return f"Nome: {self.nome}, Idade: {self.idade}"
    
class Student(Person): # Criando a classe Studet que herda de Person
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Matricula: {self.matricula}"

class Employee(Person): # Criando a classe Employee que herda de Person
    def __init__(self, nome, idade, matricula, salario):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.salario = salario

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Matricula: {self.matricula}, Salario: {self.salario}"

person = Person("Guilherme", 20) # Instanciando a classe Person
print(person)

student = Student("Guilherme", 20, 1234) # Instanciando a classe Student
print(student)
    
employee = Employee("Guilherme", 20, 1234, 1000) # Instanciando a classe Employee
print(employee)