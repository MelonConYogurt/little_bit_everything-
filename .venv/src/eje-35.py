def verificar_numero_primo(numero: int) -> bool:
    if numero < 2:return False
    elif numero == 2: return True
    elif numero % 2 == 0:return False
    else:
        for i in range(3, numero, 1):
            print(i)
            if numero % i == 0:
                return False
        return True
    
def repartir_anillos(anillos: int)-> str:
    for inpar in range(1, anillos+1, 2):
        for primo in range(2, anillos, 1):
            if verificar_numero_primo(primo):
                for par in range(2, anillos+1, 2):
                    if (inpar + primo + par + 1) == anillos: 
                        return f"inpar:{inpar}, par: {par}, primo: {primo}"
    return f"No hay reparto posible con la cantida de anillos {anillos}"
                    
if __name__ == '__main__': print(repartir_anillos(123))
    