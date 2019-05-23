char = input('Digite um caractere:')
if char >= chr(66) and char <= chr(90):
    status = 'Consoante'
elif char == chr(65) or char == chr(69) or char == chr(73) or char == chr(79) or char == chr(85):
    status = 'Vogal'
elif char >= chr(97) and char <= chr(122):
    status = 'Consoante'
    if char == chr(97) or char == chr(101) or char == chr(105) or char == chr(111) or char == chr(117):
        status = 'Vogal'
elif char >= chr(48) and char <= chr(57):
    status = 'Número'
else:
    status = 'Caractere Especial'
print(status)