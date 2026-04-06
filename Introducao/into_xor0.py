def normalizar_binario_ascii(binario):
    return binario[:2] + ("0" * (7 - len(binario[2:]))) + binario[2:]

texto = "label"

chave = bin(13)
chave_normalizada = normalizar_binario_ascii(chave)

texto_ascii = []
texto_binario = []
texto_cifrado = ""


for caractere in texto:
    texto_ascii.append(ord(caractere))

for ascii in texto_ascii:
    texto_binario.append(bin(ascii))

for binario in texto_binario:
    temp_bin = list(normalizar_binario_ascii(binario))
    for i in range(len(temp_bin)-2):
        temp_bin[(i+2)] = "0" if temp_bin[i+2] == chave_normalizada[i+2] else "1"
    
    texto_cifrado += chr(int("".join(temp_bin), 2))

    
print("texto: ", texto)
print("texto ascii: ", texto_ascii)
print("texto binario: ", texto_binario)
print("texto cifrado: ", texto_cifrado)

