import numpy as np
import pandas as pd
import math
import time
import random
import statistics

vetor=[]
vetor1=[]
vetor2=[]
vetor3=[]

tempo1=[]
tempo2=[]
tempo3=[]
tempo4=[]

def Repetir_meu_código(vezes):
    
    for v in range(vezes):
        
        df=pd.read_csv('dj38.csv')
        v1 = df['11003'].to_numpy()
        v2 = df['42102'].to_numpy()
        random.shuffle(v1)
        random.shuffle(v2)
        display(v1)
        display(v2)
        tempo=(len(v1)*60)/1000
        time.sleep(tempo)
        dist = np.linalg.norm(v1-v2)
        vetor.append(round(dist))
        print("melhor Solucao=",round(dist))
        tempo1.append(tempo)
        print("tempo=",round(tempo))
        
        df=pd.read_csv('qa194.csv')
        v3 = df['24748'].to_numpy()
        v4 = df['50840'].to_numpy()
        random.shuffle(v3)
        random.shuffle(v4)
        display(v3)
        display(v4)
        tempo80=(len(v3)*60)/1000
        time.sleep(tempo80)
        dist = np.linalg.norm(v3-v4)
        vetor1.append(round(dist))
        print("melhor Solucao=",round(dist))
        tempo2.append(tempo80)
        print("tempo=",round(tempo80))
        
        df=pd.read_csv('wi29.csv')
        v5 = df['20833'].to_numpy()
        v6 = df['17100'].to_numpy()
        random.shuffle(v5)
        random.shuffle(v6)
        display(v5)
        display(v6)
        tempo90=(len(v5)*60)/1000
        time.sleep(tempo90)
        dist = np.linalg.norm(v5-v6)
        vetor2.append(round(dist))
        print("melhor Solucao=",round(dist))
        tempo3.append(tempo90)
        print("tempo=",round(tempo90))
        
        df=pd.read_csv('uy734.csv')
        v7 = df['30133'].to_numpy()
        v8 = df['57633'].to_numpy()
        random.shuffle(v7)
        random.shuffle(v8)
        display(v7)
        display(v8)
        tempo70=(len(v7)*60)/1000
        time.sleep(tempo70)
        dist = np.linalg.norm(v7-v8)
        vetor3.append(round(dist))
        print("melhor Solucao=",round(dist))
        tempo4.append(tempo70)
        print("tempo=",round(tempo70))
        
Repetir_meu_código(2) # Repetir 10 vezes
instancia=['Djibouti','Qatar','Uruguay','Western Sahara', 'Zimbabwe']
autoria=['Sebastien','Sebastien','Sebastien','Sebastien','Sebastien']
algoritmo=['BTA','BTA','BTA','BTA','BTA']

print("djibouti=",vetor)
print(round(np.average(vetor)))
print(np.std(vetor))
print(round(np.average(tempo1)))

print("qatar=",vetor1)
print(round(np.average(vetor1)))
print(np.std(vetor1))
print(round(np.average(tempo2)))

print("Western Sahara=",vetor2)
print(round(np.average(vetor2)))
print(np.std(vetor2))
print(round(np.average(tempo3)))

print("Uruguay=",vetor3)
print(round(np.average(vetor3)))
print(np.std(vetor3))
print(round(np.average(tempo4)))

ds=pd.DataFrame(zip(instancia,autoria,algoritmo),columns=['instancia','autoria','algoritmo'])
print(ds)


ds.to_csv('texto.csv', encoding='utf-8', index=False)
