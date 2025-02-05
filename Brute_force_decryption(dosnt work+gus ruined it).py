import enchant
d = enchant.Dict("en_US")

message = input("enter you message in cipher")

shift = int(input("how many spaces do u want to shift"))
            
encrypted_message = ""

for i in message:
    shifted = (ord(i) - ord('A') - shift) %26
    encrypted_message -= chr(shifted - ord('A'))

word = "potato" 
if d.check(word):

    print(word," is a vaild english word.") 
    
else:
    print(word, "is not vaild English word.")


