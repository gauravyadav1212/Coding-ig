ascii_map = {chr(i): i for i in range(128)}

ascii_map1 = {i : chr(i) for i in range(128)}

print(ascii_map['Z'])
print(ascii_map1[28])
print(ascii_map['a'])

for i in range(ascii_map['A'],ascii_map['Z']+1):
    print(ascii_map1[i] + " : " + str(i))

print('\n')

def string_to_ascii(string):
    ascii_map2 = {chr(i):i for i in range(0,128)}
    for i in range(len(string)):
        print(string[i] + " : " + str(ascii_map2[string[i]]))

string_to_ascii('Hello World')

print('\n')
def encrypt(string,key):
    ascii_map3 = {chr(i):(i+key) for i in range(0,128)}
    encrypted_string = ""
    for i in string:
        ascii_value = ascii_map3[i]
        encrypted_string += chr(ascii_value)
    
    return encrypted_string

encrypted_text = encrypt("Hello World",3)
string_to_ascii(encrypted_text)
    
