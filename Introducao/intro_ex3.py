texto_ascii = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
texto_plano = []

for caractere in texto_ascii:
    texto_plano.append(chr(caractere))

for caractere in texto_plano:
    print(caractere, end="")