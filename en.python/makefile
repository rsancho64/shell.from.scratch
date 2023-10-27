shell:
	chmod +x shell.py

++++
# REPL
#     READ   read()
#     EVAL   eval()
#     PRINT  print()
#     LOOP

def myPrint(s):
    if s == "":
        print(s, end='')

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






++++
