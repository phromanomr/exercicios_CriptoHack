texto_cifrado = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# Decodificação de hexadecimal/base 16 para texto plano
texto_plano = bytes.fromhex(texto_cifrado)

print(texto_plano)
