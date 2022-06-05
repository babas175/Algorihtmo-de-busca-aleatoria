import csv
import numpy
import random
import time
import math


vetor=[]
vetor1=[]
vetor2=[]
vetor3=[]
vetor4=[]



def Repetir_meu_código(vezes):
    
    for v in range(vezes):
        #Qatar
        t1 = time.time()
        arq = open("qatar.tsp") 
        arq = open("qatar.tsp")
        linhas = arq.readlines()
        random.shuffle(linhas)
        print(linhas)

        a = numpy.array(linhas)

        with open('resultados.csv', 'w', newline="") as file:
            mywriter = csv.writer(file, delimiter=' ')
            mywriter.writerows(a)  
    
        tempoExec = time.time() - t1
        print("Tempo de execução: {} segundos".format(tempoExec))
        print("==================================================================================================================== Qatar")
        print()
        vetor.append(tempoExec)        
        
Repetir_meu_código(10) # Repetir 10 vezes

#Uruguay
def Repetir_meu_código(vezes1):
    
    for v in range(vezes1):
        
        t1 = time.time()
        arq = open("uruguay.tsp") 
        arq = open("uruguay.tsp")
        linhas = arq.readlines()
        random.shuffle(linhas)
        print(linhas)

        a = numpy.array(linhas)

        with open('resultados.csv', 'w', newline="") as file:
            mywriter = csv.writer(file, delimiter=' ')
            mywriter.writerows(a)  
    
        tempoExec = time.time() - t1
        print("Tempo de execução: {} segundos".format(tempoExec))
        print("==================================================================================================================== Qatar")
        print()
        vetor1.append(tempoExec)        
        
Repetir_meu_código(10) # Repetir 10 vezes


#western
def Repetir_meu_código(vezes2):
    
    for v in range(vezes2):
        #Qatar
        t1 = time.time()
        arq = open("western.tsp") 
        arq = open("western.tsp")
        linhas = arq.readlines()
        random.shuffle(linhas)
        print(linhas)

        a = numpy.array(linhas)

        with open('resultados.csv', 'w', newline="") as file:
            mywriter = csv.writer(file, delimiter=' ')
            mywriter.writerows(a)  
    
        tempoExec = time.time() - t1
        print("Tempo de execução: {} segundos".format(tempoExec))
        print("==================================================================================================================== Qatar")
        print()
        vetor2.append(tempoExec)        
        
Repetir_meu_código(10) # Repetir 10 vezes

#Zimbabwe
def Repetir_meu_código(vezes3):
    
    for v in range(vezes3):
        #Qatar
        t1 = time.time()
        arq = open("zimbabwe.tsp") 
        arq = open("zimbabwe.tsp")
        linhas = arq.readlines()
        random.shuffle(linhas)
        print(linhas)

        a = numpy.array(linhas)

        with open('resultados.csv', 'w', newline="") as file:
            mywriter = csv.writer(file, delimiter=' ')
            mywriter.writerows(a)  
    
        tempoExec = time.time() - t1
        print("Tempo de execução: {} segundos".format(tempoExec))
        print("==================================================================================================================== Qatar")
        print()
        vetor3.append(tempoExec)        
        
Repetir_meu_código(10) # Repetir 10 vezes



#Djibouti
def Repetir_meu_código(vezes4):
    
    for v in range(vezes4):
        #Qatar
        t1 = time.time()
        arq = open("djibouti.tsp") 
        arq = open("djibouti.tsp")
        linhas = arq.readlines()
        random.shuffle(linhas)
        print(linhas)

        a = numpy.array(linhas)

        with open('resultados.csv', 'w', newline="") as file:
            mywriter = csv.writer(file, delimiter=' ')
            mywriter.writerows(a)  
    
        tempoExec = time.time() - t1
        print("Tempo de execução: {} segundos".format(tempoExec))
        print("==================================================================================================================== Qatar")
        print()
        vetor4.append(tempoExec)        
        
Repetir_meu_código(10) # Repetir 10 vezes

avg4 = sum(vetor4)/len(vetor4)
print(vetor4)

print(avg4)

print("======================")


avg3 = sum(vetor3)/len(vetor3)
print(vetor3)

print(avg3)


print("======================")


avg2 = sum(vetor2)/len(vetor2)
print(vetor2)

print(avg2)

print("======================")


avg1 = sum(vetor1)/len(vetor1)
print(vetor1)

print(avg1)


print("======================")


avg = sum(vetor)/len(vetor)
print(vetor3)

print(avg)


#desvio padrao
print("=====================================================================================")
mean = sum(vetor4) / len(vetor4)
var = sum((l-avg)**2 for l in vetor4) / len(vetor4)
st_dev = math.sqrt(var)

print("O desvio padrao é " + str(st_dev))


mean = sum(vetor3) / len(vetor4)
var = sum((l-avg)**2 for l in vetor3) / len(vetor3)
st_dev = math.sqrt(var)

print("O desvio padrao é " + str(st_dev))


mean = sum(vetor2) / len(vetor2)
var = sum((l-avg)**2 for l in vetor2) / len(vetor2)
st_dev = math.sqrt(var)

print("O desvio padrao é " + str(st_dev))


mean = sum(vetor1) / len(vetor1)
var = sum((l-avg)**2 for l in vetor1) / len(vetor1)
st_dev = math.sqrt(var)

print("O desvio padrao é " + str(st_dev))


mean = sum(vetor) / len(vetor)
var = sum((l-avg)**2 for l in vetor) / len(vetor)
st_dev = math.sqrt(var)

print("O desvio padrao é " + str(st_dev))




