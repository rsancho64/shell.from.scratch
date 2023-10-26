#! /usr/bin/python3

from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP

def help():
    return "no hay contenido de ayuda todavia"

def myEval(e):

    e = e.lower() ## canonize(exp)

    if ( e in ["bye", "exit"]):
        print("adios")
        exit(0)

    if ( e in ["help", "--h", "--help", "/h", "?"]):
        return help()

    return eval(e) # https://www.mygreatlearning.com/blog/eval-in-python
    # return f"{exp}: desconocido"

if __name__ == "__main__":

    """REPL: bucle read,eval,print o print(eval(read()))"""
    while True:
    
        # R
        inp = input("e? ")  # print("e? ", end = '') ";" in = input()

        # E
        out = myEval(inp)
        
        # P
        print(out)



        

