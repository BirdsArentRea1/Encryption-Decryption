message = input("enter you message in cipher")

shift = int(input("how many spaces do u want to shift"))
            
encrypted_message = ""

for i in message:
    shifted = (ord(i) - ord('A') + shift) %26
    encrypted_message += chr(shifted + ord('A'))

print ("Encrypted message: ", encrypted_message)
