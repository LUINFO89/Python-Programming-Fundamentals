def promedio(lista:list)->float:
    return round(sum(lista)/len(lista),2)
    
def inicio():
    ciclos=int(input())
    vectemperatura=[]
    vecprofundidad=[]
    sumamente_apto = 0
    moderadamente_apto=0
    marginalmente_apto =0
    no_apto=0
    
    for ciclo in range(ciclos):
        vectemperatura.append(promedio(list(map(lambda x: float(x), input().split(" ")))))
        
        vecprofundidad.append(promedio(list(map(lambda x: float(x), input().split(" ")))))
       
        
        if (vectemperatura [ciclo] > 75 and vectemperatura [ciclo]  <= 82) and (vecprofundidad[ciclo] > 39.37):
            sumamente_apto += 1
        elif(vectemperatura [ciclo] > 75 and vectemperatura [ciclo] <= 82) and (vecprofundidad[ciclo] > 19.68 and vecprofundidad[ciclo] <= 39.37):
            moderadamente_apto += 1
        elif (vectemperatura [ciclo] > 75 and vectemperatura [ciclo] <= 82) and (vecprofundidad[ciclo] > 9.84 and vecprofundidad[ciclo] <= 19.68):
            marginalmente_apto += 1
        elif (vectemperatura [ciclo] > 75 and vectemperatura [ciclo] <= 82) and (vecprofundidad[ciclo] < 9.84):
            no_apto += 1
        elif ((vectemperatura [ciclo] > 82 and vectemperatura [ciclo] <= 86) or (vectemperatura [ciclo] > 68 and vectemperatura [ciclo] <=75)) and (vecprofundidad[ciclo] > 39.37):
            moderadamente_apto += 1
        elif ((vectemperatura [ciclo] > 82 and vectemperatura [ciclo] <= 86) or (vectemperatura [ciclo] > 68 and vectemperatura [ciclo] <=75)) and  (vecprofundidad[ciclo] > 19.68 and vecprofundidad[ciclo] <= 39.37):
            moderadamente_apto += 1
        elif ((vectemperatura [ciclo] > 82 and vectemperatura [ciclo] <= 86) or (vectemperatura [ciclo] > 68 and vectemperatura [ciclo] <=75)) and  (vecprofundidad[ciclo] > 9.84 and vecprofundidad[ciclo] <= 19.68):
            marginalmente_apto += 1
        elif ((vectemperatura [ciclo] > 82 and vectemperatura [ciclo] <= 86) or (vectemperatura [ciclo] > 68 and vectemperatura [ciclo] <=75)) and  (vecprofundidad[ciclo] < 9.84):
            no_apto += 1
        elif ((vectemperatura [ciclo] > 86 and vectemperatura [ciclo] <= 90) or (vectemperatura [ciclo] >= 64 and vectemperatura [ciclo] <=68)) and (vecprofundidad[ciclo] > 39.37):
            marginalmente_apto += 1
        elif ((vectemperatura [ciclo] > 86 and vectemperatura [ciclo]<= 90) or (vectemperatura [ciclo] >= 64 and vectemperatura [ciclo] <=68)) and  (vecprofundidad[ciclo] > 19.68 and vecprofundidad[ciclo] <= 39.37):
            marginalmente_apto += 1
        elif ((vectemperatura [ciclo] > 86 and vectemperatura [ciclo] <= 90) or (vectemperatura [ciclo] >= 64 and vectemperatura [ciclo] <=68)) and  (vecprofundidad[ciclo] > 9.84 and vecprofundidad[ciclo] <= 19.68):
            marginalmente_apto += 1
        elif ((vectemperatura [ciclo] > 86 and vectemperatura [ciclo] <= 90) or (vectemperatura [ciclo] >= 64 and vectemperatura [ciclo] <=68)) and  (vecprofundidad[ciclo] < 9.84):
            no_apto += 1
        elif (vectemperatura [ciclo] < 64 or vectemperatura [ciclo] > 90) and (vecprofundidad[ciclo] > 39.37):
            no_apto += 1
        elif (vectemperatura [ciclo] < 64 or vectemperatura [ciclo] > 90) and (vecprofundidad[ciclo] > 19.68 and vecprofundidad[ciclo] <= 39.37):
            no_apto += 1
        elif (vectemperatura [ciclo] < 64 or vectemperatura [ciclo] > 90) and (vecprofundidad[ciclo] >= 9.84 and vecprofundidad[ciclo] <= 19.68):
            no_apto += 1 
        elif (vectemperatura [ciclo] < 64 or vectemperatura [ciclo] > 90) and (vecprofundidad[ciclo] < 9.84):
             no_apto += 1
    
       
    
    for e in vectemperatura:
        print(f"{e:2.2f}",end=" ")
    print()
    for x in vecprofundidad :
        print(f"{x:2.2f}",end=" ")
            
    
    print()
    print("sumamente apto",sumamente_apto)
    print("Moderadamente Apto",moderadamente_apto)
    print("Marginalmente Apto",marginalmente_apto )
    print("No apto",no_apto)
    
    
if __name__ == '__main__':
    inicio()

