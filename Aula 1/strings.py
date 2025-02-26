# Strings Built-in Functions

course_name = "Python Programming"

print(len(course_name)) # len(): Retorna tamanho da String
print(course_name[0])   # []: Acessa o caractere na posição 0
print(course_name[-1])  # []: Acessa o último caractere -1
print(course_name[0:3]) # [0:3]: Acessa os caracteres de 0 a 2
print(course_name[1:3])  # [1:3]: Acessa os caracteres de 1 a 2
print(course_name[3:])  # [3:]: Acessa os caracteres a partir da posição 3

# Caracteres de escape
print("=============================================")


print("Python \"Programming\"") # \" : Aspas duplas
print("Python \nProgramming")   # \n : Nova linha

# Concatenação de Strings
print("=============================================")


first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name

print(full_name)
print("{} {}".format(first_name, last_name)) # .format(): Formatação de Strings
print(f"{first_name} {last_name}") # f-string: Formatação de Strings

# Methods String
print("=============================================")

course2 = "python programming"

modifed_course_name = course_name.upper() # upper(): Converte para maiúsculo

print(modifed_course_name)
print(course_name.upper()) # upper(): Converte para maiúsculo
print(course_name.lower()) # lower(): Converte para minúsculo
print(course2.title()) # title(): Converte para título
print(course_name.strip()) # strip(): Remove espaços em branco
print(course_name.find("P")) # find(): Encontra a posição da palavra
print(course_name.replace("Python", "Java")) # replace(): Substitui a palavra
print(course_name.replace("P", "J")) # replace(): Substitui a letra
print("Programming" in course_name) # in: Verifica se a palavra está na string