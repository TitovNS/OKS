import pathlib
import os
print("INN")
inn1=input()
print("KPP")
kpp1=input()
max_smena=int(input('maximalnaya smena '))
max_smena+=1

for number in range(1, max_smena):
    oks= "export"+str(number)+".txt" 
    try:
        f = open(oks)   
        fd = f.readlines(50) # находим дату в строке
        data = fd[3][2:12]  # разбираем дату на год, месяц, день
        day = data[0:2]
        month = data[3:5]
        year = data[6:10]
        print(number)
        print(data)
        print(fd[3])

        f.close()
        os.rename("D:/oks/"+oks, "D:/oks_new/"+inn1+"_"+kpp1+"_"+year+"-"+month+"-"+day+"_"+str(number)+".txt") # переименуюем и кладем куда хотим
    except FileNotFoundError:
        pass
print("done")
