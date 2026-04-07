import base64

texto_hex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Decodificação de hexadecimal/base 16 para texto plano
texto_plano = bytes.fromhex(texto_hex)

print(texto_plano)

# Codificação de texto plano para base64
texto_base64 = base64.b64encode(texto_plano)

print(texto_base64)
