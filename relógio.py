import math
import time
import os

#display de relógio digital

for i in range(23, -1,-1): #HORAS

    #i = f"{i}" if i >= 10 else f"0{i}"

    for j in range(59, -1,-1): #MINUTOS

        #j= f"{j}" if j>=10 else f"0{j}"

        for z in range(59, -1,-1): #SEGUNDOS E IMPRESSÃO DO RELÓGIO

            #z = f"{z}" if z >= 10 else f"0{z}"

            print(f"{i:02}:{j:02}:{z:02}")
            time.sleep(1)
            os.system('cls')
