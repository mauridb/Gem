import os
import random
import sys


ENCRIPT_FILE = sys.argv[1]
print ENCRIPT_FILE
SET_KEY = [ 
    ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
    ['0','1','2','3','4','5','6','7','8','9'],
    [',',';',':','>','-','_','.','=','!']
]
def encript_line(string_line):
    solution = []
    new_line = ""
    for index, char in enumerate(string_line):
        t_list_char = SET_KEY[random.randint(0, len(SET_KEY)-1)]
        rand_char = t_list_char[random.randint(0, len(t_list_char)-1)]
        solution.append((index, char, str(rand_char)))
        new_line += str(rand_char)
    return [new_line, solution]
    
def encript_file(enc_file):
    with open("{}".format(enc_file), 'r') as f:
        list_readlines = f.readlines()
        for index, line in enumerate(list_readlines):
            crypted_line = encript_line(line)
            print crypted_line[0]
            with open("crypted.txt", "a") as cf:
                cf.write(crypted_line[0]+"\n")
            with open("key.txt", "a") as keyf:
                # TODO: key in other file
                print "ukulele"
        
encript_file(ENCRIPT_FILE)
