#! /usr/bin/python3
# from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
# REPL:
#     READ   read()
#     EVAL   eval()
#     PRINT  print()
#     LOOP
#
#     while (True) : print(eval(read()))
#

def myPrint(str):
    """print output string from expresion evaluation"""
    if str == "":
        print(str, end='')

def myHelp():
    print("lo siento, no hay ayuda por ahora")

def myEval(e):

    if e == "":
        return e # None

    if e in ["exit", "bye", "adios"]:
        print("bye")
        exit(0)

    if e in ["help", "/h", "?"]:
        myHelp()
        return None

    return eval(e)

if __name__ == "__main__":
    """wrapper REPL en python"""

    while True:        
        # read
        algo = input("dime algo: ")
        # print(algo)

        # eval ; print
        myPrint(myEval(algo))

#def help():
#    return "no hay contenido de ayuda todavia"

#def myEval(e):

#    e = e.lower() ## canonize(exp)

#    if ( e in ["bye", "exit"]):
#        print("adios")
#        exit(0)

#    if ( e in ["help", "--h", "--help", "/h", "?"]):
#        return help()

#    return eval(e) # https://www.mygreatlearning.com/blog/eval-in-python
#    # return f"{exp}: desconocido"

#if __name__ == "__main__":

#    """REPL: bucle read,eval,print o print(eval(read()))"""
#    while True:
    
        # R
#        inp = input("e? ")  # print("e? ", end = '') ";" in = input()

        # E
#        out = myEval(inp)
        
        # P
#        print(out)



        

