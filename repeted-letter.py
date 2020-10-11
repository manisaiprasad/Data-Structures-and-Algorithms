map_letters = {' ':0,
    'a':0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0}

with open('mytest.txt','r') as f:
    file_data = f.read()

file_data=file_data.replace(" ", "")    
# print(file_data) 
for i in file_data:
    # if map_letters[' '] == map_letters[i]:
    #     continue
    map_letters[i.lower()]+=1

max_key = max(map_letters, key=lambda k: map_letters[k])
print("{} is max occurred letter ".format(max_key))
# print(file_data)