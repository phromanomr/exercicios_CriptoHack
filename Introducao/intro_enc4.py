from Crypto.Util.number import *

texto_crifrado = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Decodificação de base10 para texto plano
texto_plano = long_to_bytes(texto_crifrado)

print(texto_plano)