
def suma(a: float, b: float):
    return a+b

def resta(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a/b


if __name__ == "__main__":
    res = 0
    try:
        res = div(a=3, b=3)
    except Exception as e:
        print(f'Hubo un error en la division: {e.args}')
    print(res)
    try:
        res = suma(a='tres', b=2)
    except Exception as e:
        print(f'Hubo un error en la suma: {e.args}')
    print(res)
    
# end main