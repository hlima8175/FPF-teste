
senha = input("Digite a senha a ser decodificada: ")
lista = list(senha)

print(lista)

meio = len(lista) // 2

for i in range(meio, len(lista) - 1) :
    lista[i], lista[i + 1] = chr(ord(lista[i]) + 1), chr(ord(lista[i + 1]) + 1)

print("Lista após alterações:", lista)

lista.reverse()

print(lista)

def deslocar_caracteres(lista):
    resultado = ""
    for char in lista:
        if char.isalpha(): 
            codigo = ord(char) 

            novo_codigo = codigo - 3

            if char.isupper():
                if novo_codigo < ord('A'):
                    novo_codigo += 26
          
            else:
                if novo_codigo < ord('a'): 
                    novo_codigo += 26
            resultado += chr(novo_codigo)  
        else:
            resultado += char 
    return resultado

lista_deslocado = deslocar_caracteres(lista)
print("Texto Original:", lista)
print("Texto Deslocado:", lista_deslocado)

