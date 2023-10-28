#! /usr/bin/python3
# from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
# a REPL is a { Read -read()-; Eval -eval()-; Print -print()- } Loop
# while (True) : print(eval(read()))
#

def myPrint(str):
    """print output string from expresion evaluation"""
    if str == "":
        return  # pass # print(str, end='')
    print(str)


def myHelp():
    return "lo siento, no hay ayuda por ahora"


def myEval(e):

    if e == "":
        return e  # None

    if e in ["exit", "bye", "adios"]:
        print("bye")
        exit(0)

    if e in ["help", "/h", "?"]:
        return myHelp()

    # tokenizing e(xpr) ...
    # https://blog.gitnux.com/code/python-tokenizing-strings-in-list-of-strings
    # :/
    # import nltk
    # nltk.download('punkt')
    # tokens = nltk.word_tokenize(e)
    # return tokens

    # https://www.tutorialspoint.com/5-simple-ways-to-perform-tokenization-in-python
    # :/
    # goo: parse python expression in tokens ...
    # - [] try pyparsing
    # - [] try TDParser    

    # return eval(e)

if __name__ == "__main__":
    """wrapper REPL en python"""

    while True:
        # read
        # print(e)
        e = input("dime algo: ")

        # eval ; print
        myPrint(myEval(e))

# def help():
#    return "no hay contenido de ayuda todavia"

# def myEval(e):

#    e = e.lower() ## canonize(exp)

#    if ( e in ["bye", "exit"]):
#        print("adios")
#        exit(0)

#    if ( e in ["help", "--h", "--help", "/h", "?"]):
#        return help()

#    return eval(e) # https://www.mygreatlearning.com/blog/eval-in-python
#    # return f"{exp}: desconocido"

# if __name__ == "__main__":

#    """REPL: bucle read,eval,print o print(eval(read()))"""
#    while True:

        # R
#        inp = input("e? ")  # print("e? ", end = '') ";" in = input()

        # E
#        out = myEval(inp)

        # P
#        print(out)
