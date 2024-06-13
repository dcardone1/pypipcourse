
N = int(input('¿largo de la base?'))

def piramide(n, m):

    x = n*' ' + m*'#'
    print(x)
    if n>0:
        piramide(n-1, m+2)
    else:
        return
   
n = N//2

piramide(n, 1)
