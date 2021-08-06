asciiPrintable = [" ", "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "\\", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~"]
nonoFunctions = ["eval(", ]
complete = False
#f = open("tempscript.py", "w")
def decimalToCustom(decimal, array):
    r = ''
    r2 = []
    base = len(array)
    n = 1
    i = 0
    while n <= decimal:
        n = n * base
        i = i + 1
    n = n / base #Return longest number less than decimal
    for x in range(i):
        r2.append(decimal // n)
        decimal = decimal % n #subtract and set up for next loop
        n = n / base #increment number down a place
    for x in r2:
        r = r + array[int(x)]
    return r

#print(len(asciiPrintable))
loop = 0
while not complete:
    code = decimalToCustom(loop, asciiPrintable)
    contains = False
    for x in nonoFunctions:
        if x in code:
            contains = True
            break
    if not contains:
        eval(code)
    try:
        if functionName(5, 5) == 25: complete = True
    except:
        pass
print(decimalToCustom(loop, asciiPrintable))
