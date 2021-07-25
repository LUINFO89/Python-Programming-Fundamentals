n = int(input(""))
    
i = 0
suma_temperatura=0
suma_profundidad=0
sumamente_apto = 0
marginalmente_apto = 0
moderadamente_apto = 0
no_apto = 0
while (i < n) :
    i = i + 1 
  
   
    temperatura = int(input(""))
    profundidad = float(input(""))
    suma_temperatura = suma_temperatura + temperatura
    suma_profundidad = suma_profundidad + profundidad
    pt = suma_temperatura / n
    pp = suma_profundidad / n
    #suma1 = suma1 + Temperatura
    #promt =   suma1 / n
    #suma2 = suma2 + Profundidadefectivadelsuelo
    #promp =   suma2 / n
    if (temperatura >= 76 and temperatura <= 82) and (profundidad > 39.37):
        sumamente_apto += 1
    elif(temperatura >= 76 and temperatura <= 82) and (profundidad > 19.68 and profundidad <= 39.37):
        moderadamente_apto += 1
    elif (temperatura >= 76 and temperatura <= 82) and (profundidad > 9.84 and profundidad <= 19.68):
        marginalmente_apto += 1
    elif (temperatura >= 76 and temperatura <= 82) and (profundidad < 9.84):
        no_apto += 1
    elif ((temperatura >= 83 and temperatura <= 86) or (temperatura >= 69 and temperatura <=75)) and (profundidad > 39.37):
        moderadamente_apto += 1
    elif ((temperatura >= 83 and temperatura <= 86) or (temperatura >= 69 and temperatura <=75)) and  (profundidad > 19.68 and profundidad <= 39.37):
        moderadamente_apto += 1
    elif ((temperatura >= 83 and temperatura <= 86) or (temperatura >= 69 and temperatura <=75)) and  (profundidad > 9.84 and profundidad <= 19.68):
        marginalmente_apto += 1
    elif ((temperatura >= 83 and temperatura <= 86) or (temperatura >= 69 and temperatura <=75)) and  (profundidad < 9.84):
        no_apto += 1
    elif ((temperatura >= 87 and temperatura <= 90) or (temperatura >= 64 and temperatura <=68)) and (profundidad > 39.37):
        marginalmente_apto += 1
    elif ((temperatura >= 87 and temperatura <= 90) or (temperatura >= 64 and temperatura <=68)) and  (profundidad > 19.68 and profundidad <= 39.37):
        marginalmente_apto += 1
    elif ((temperatura >= 87 and temperatura <= 90) or (temperatura >= 64 and temperatura <=68)) and  (profundidad > 9.84 and profundidad <= 19.68):
        marginalmente_apto += 1
    elif ((temperatura >= 87 and temperatura <= 90) or (temperatura >= 64 and temperatura <=68)) and  (profundidad < 9.84):
        no_apto += 1
    elif (temperatura < 64 or temperatura > 90) and (profundidad > 39.37):
        no_apto += 1
    elif (temperatura < 64 or temperatura > 90) and (profundidad > 19.68 and profundidad <= 39.37):
        no_apto += 1
    
    elif (temperatura < 64 or temperatura > 90) and (profundidad >= 9.84 and profundidad <= 19.68):
        no_apto += 1 
    elif (temperatura < 64 or temperatura > 90) and (profundidad < 9.84):
        no_apto += 1
    
print(f'{pt:.2f}')
print(f'{pp:.2f}' )
print("Sumamente Apto",sumamente_apto)
print("Moderadamente Apto",moderadamente_apto)
print("Marginalmente Apto",marginalmente_apto )
print("No apto",no_apto)