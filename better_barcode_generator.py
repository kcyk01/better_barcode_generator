'''
Better Barcode Generator v1.0
May 19, 2015

Github: kcyk01


'''

from itertools import product
from random import randint

### Default Values ###

length = 4
min = 0
max = 100

filename1 = "betterBarcode.txt"
filename2 = "randomBarcode.txt"

######################

length_string = "Length of barcode: "
length_condition = lambda x: not x.isnumeric() or int(x) <= 0
min_string = "Minimum GC %: "
min_condition = lambda x: not x.isnumeric() or float(x) < 0 or float(x) > 100
max_string = "Maximum GC %: "
max_condition = lambda x: not x.isnumeric() or float(x) < 0 or float(x) > 100
number_string = "Number of barcodes: "


def get_input(prompt, condition_function):
    new_input = input(prompt)
    while condition_function(new_input):
        print("Invalid input: '" + new_input + "'\n")
        new_input = input(prompt)
    return new_input

def compare(x, min, max):
    k = float(x.count('c') + x.count('g')) / len(x) * 100
    if k >= min and k <= max:
        
        return True
    return False
    
def generate(length, min, max):
    c = map(lambda x: ''.join(x),
            filter( lambda x: False if x == None else True,
                    map(lambda x: x if compare(x, min, max) else None,    
                        list(product('atcg', repeat=length)))))
    return list(c)
    
def save_to_files(c, filename):
    f = open(filename, "w")
    print("Total barcodes: " + str(len(c)), file=f)
    for a in c:
        print(a, file=f)
    f.close()
    
def pick_random(c, num):
    result = []
    i = 0
    while i < num and len(result) < len(c):
        n = randint(0,len(c)-1)
        if c[n] not in result:
            result.append(c[n])
            i += 1
    return result
    

if __name__ == '__main__':
    length = int(get_input(length_string, length_condition))
    min = float(get_input(min_string, min_condition))
    max = float(get_input(max_string, max_condition))
    print('Generating...Please wait')
    result = generate(length, min, max)
    save_to_files(result, filename1)
    print("Full list saved to file: " + filename1)
    num = int(get_input(number_string, length_condition))
    result2 = pick_random(result, num)
    save_to_files(result2, filename2)
    print("Random list saved to file: " + filename2)
    input("Program terminated successfully. Press enter to exit.")
