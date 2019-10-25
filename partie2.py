import random
print("Exercice 1\n")
for x in range(8):
    for y in range(16):
        if (x + y) % 2:
            print('#', end='')
        else:
            print(' ', end='')
    print()

print("Exercice 2\n")#faux

for i in range (0, 4):
   for j in range (0, 4):
       if i == j:
           print(1)
       else:
           print (0)
   print("------")

print("Exercice 3\n") #
a = float(input(" Entrez le montant du panier : "))
def montant(a):
    if (a%2)== 0:
        print(bool(a))
    else:
        print(bool())    
montant(a)
print("Exercice 4\n")

num = 1 
n=int(input("Entrer votre nombre :"))  
for i in range(1,n+1):  
    num = num * i 
print("Le factorielle de", n, "est de  :", num) 

print("Exercice 5\n")   

n="Facture de 19286-----euro "
print(n.replace("-", "\_"))

print("Exercice 6\n")
liste = [
    "chocolat",
    "water",
    "lemon",
    "mint",
    "banana",
    "soda"
]

print (liste[0], random.choice(liste), liste[-1])

print("Exercice 7\n")
for i in [
    "Landers",
    "Mark",
    "19 ans",
    "01/01/2000"
] :
    print(i)
    
for l in [
[
    "Landers", "Mark", "19 ans", "01/01/2000"
],
    ["Atton", "Olivier", "19 ans", "01/02/2000"
]
] :
    for k in l :
        print(k)
    
print("Exercice 8\n")    

num=[1,2,10,5,59,34,23,4]
print ("le nombre le plus grand est :",max(num))

num=str([1,2,10,5,59,34,23,4,">"])
print ("le nombre le plus grand est :",max(num))

print("Exercice 9\n")   
mot=" "
tache= [] #list()
while mot !="fin":
    tache.append(mot)
    mot=input("Entrer votre tâche :")
tache.pop(0)
print(tache)