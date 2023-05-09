import trie as tr
import sys

def compress(file, output_name):
    with open(output_name, 'w+b') as f:
        dictionary = tr.Trie()
        i = 1
        prefix = ''
        data = file.read()
        for char in data: 
            if dictionary.search(prefix + char) == -1:
                f.write(dictionary.search(prefix).to_bytes(3,sys.byteorder))
                f.write(ord(char).to_bytes(2,sys.byteorder))
                dictionary.insert(i, prefix+char)
                prefix = ''
                i+=1 
            else:
                prefix = prefix+char

def decompress(file, output_name):
    with open(output_name, 'w') as f:
        dicionario = ['']
        while True:
            index = file.read(3)
            if index == b'':
                break
            index = int.from_bytes(index,sys.byteorder)
            char = file.read(2)
            char = chr(int.from_bytes(char,sys.byteorder))
            if index == 0:
                word = ''
            else:                
                word = dicionario[index]
            word = word + char
            f.write(word)
            dicionario.append(word)
                  

if __name__=='__main__':
    if sys.argv[1] == "-c":
        file = open(sys.argv[2], 'r', encoding = 'utf-8-sig')
        output_name = sys.argv[4]
        output_name += ".z78" 
        compress(file, output_name)
        file.close()

    if sys.argv[1] == "-x":
        file = open(sys.argv[2], 'r+b')
        output_name = sys.argv[4]
        output_name += ".txt"
        decompress(file, output_name)
        file.close()