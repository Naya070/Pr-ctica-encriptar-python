letras = open("letras.txt", 'r') #Entrada del archivo .txt
letras_r = letras.read()         #Leer y guardar el contenido del archivo .txt en la variable letras_r
letras_l = letras_r.split("\n")  #Crear una lista cortando al string letras_r en cada salto de línea

encripta = open("encripta.txt", 'r') 
encripta_r = encripta.read()
encripta_r = encripta_r.replace('\n', '').replace('\r', '').replace(' ', '')
#Eliminar saltos de línea y epacios

indice = 0 #establecemos un contador
while indice < len(encripta_r):  #mientras el contador sea menor a la longitud de la cadena
    caracter = encripta_r[indice] #tomar caracter
    
    for elemento in letras_l: #recorrer la lista elemento por elemento
        j = elemento[0]       #tomar la primera letra de cada elemento
                
        palabra = elemento[2:] # establecer subcadena a partir de la tercera letra de cada elemento
        if caracter == j: #comparar cada caracter tomado con la primera letra de cada elemento de la lista
            print(palabra)
    indice += 1             #sumar 1 al contador
    
    
