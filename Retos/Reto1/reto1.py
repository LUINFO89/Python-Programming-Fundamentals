Temperaturamediaanual = int(input(""))
Profundidadefectivadelsuelo = float(input(""))
if Temperaturamediaanual >= 76 and Temperaturamediaanual <= 82 and Profundidadefectivadelsuelo >= 39.37: 
    print("Sumamente Apto")
elif Temperaturamediaanual >=83 and Temperaturamediaanual <= 86 or Temperaturamediaanual <= 75 and Temperaturamediaanual >= 69 and Profundidadefectivadelsuelo > 19.69 and Profundidadefectivadelsuelo < 39.37:
    print("Moderadamente Apto")
elif Temperaturamediaanual >= 87 and Temperaturamediaanual <= 90 or Temperaturamediaanual <=68 and Temperaturamediaanual >=64 and  Profundidadefectivadelsuelo > 9.84 and Profundidadefectivadelsuelo < 19.68:
    print("Marginalmente Apto")
elif Temperaturamediaanual < 64 or Temperaturamediaanual > 90 and Profundidadefectivadelsuelo < 9.84:
    print("No apto")
    