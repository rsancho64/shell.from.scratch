control = True

def canonize(exp):
    return exp.lower()

def eval(exp):
    exp = canonize(exp)
    if ( exp in ["bye", "exit"]):
        print("adios")
        exit(0)
    if ( exp in ["help"]):
        print("no hay ayuda todavia")
        return control
    return f"{exp}: desconocido"
    
while True:
    print("comando? ", end = '')   
    cmd = input()

    val = eval(cmd)
    if val:
        print(val) # print("    val: ", val)
    else:
        pass # print("    cmd: ", cmd)   # just echo cmd
        

