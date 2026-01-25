"""
Ejercicio 89
Checa si una palabra es palindromo usando lambda
"""

palindromo = lambda palabra : palabra == palabra[::-1]      #Recibe una palabra y la compara con la  misma palabra alreves      
print(palindromo("udu"))        #Le pasa el valor de la palbra y pinta en pantalla