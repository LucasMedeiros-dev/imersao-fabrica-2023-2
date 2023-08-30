def soma(x: int | float, y: int | float):
    '''### Soma  
        x: recebe um `int` ou `float`.      
        y: recebe um `int` ou `float`.               
       
        retorno: `int` ou `float` com a  soma de `x + y`
    
    '''
    return x + y

def print_subtracao(x: int | float, y: int | float):
    '''### Printa o resultado da subtração.  
        x: recebe um `int` ou `float`.  
        y: recebe um `int` ou `float`.
    '''
    print(f"{x - y}")

def soma_sem_parametro():
    """### soma dois valores préviamente estabelecidos na função.
    `x` = 5.\n
    `y` = 5.
    """
    x = 5
    y = 5
    return x + y
