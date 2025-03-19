valor_1 = input("Digite o valor (True/False): ")
valor_2 = input("Digite o valor (True/False): ")
valor_3 = input("Digite o valor (True/False): ")

arr = [valor_1, valor_2, valor_3]
count = 0

for i in arr:
    if(i == 'True'):
        count += 1

if(count == 2):
    print("Pelo menos dois são verdadeiros")