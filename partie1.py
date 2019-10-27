import math
#search bigger number
print("Exercice 1\n")
a=32
b=76
c=1
d=45
 
if  a>b and a>c and a>d:
    print(a)     
elif b>a and b>c and b>d:
     print(b)   
elif c>a and c>b and c>d:
     print(c)
else:
     print(d)    

#enter information 
print("Exercice 2\n")
try:
    age = int(input("Entrer votre age :"))
    if age <= 0: 
        print ("Indiquez un age réel :")
    if age% 2== 0:
        print ("Votre âge est pair")   
    if math.sqrt(age).is_integer: 
        print ("votre âge est carré")     
    if age >= 21 :
        print ("Accès autorisé")   
except ValueError:
    print("Error")

#Question and condition
print("Exercice 3\n")
secret=143
trouver=True
while trouver==True:
    question = int(input("Entrer un nombre :"))
    if question < secret :
        print("Le nombre est plus grand")
    if question > secret :
        print("Le nombre est plus petit")
    if question == secret :
        print ("vous avez gagné!")
        trouver=False

#1at100
print("Exercice 4\n")f calcul(lon=35, lar=48, pro=4, deb=9):
    result= lon*lar*pro
    result1=result/deb
for i in range (1,101):
    print(i)

#Range pair
print("Exercice 5\n")
for p in range (0,101, 2):
    print (p)

#Fill the pool
print("Exercice 6\n")
def calcul(lon=35, lar=48, pro=4, deb=9):
    result= lon*lar*pro
    result1=result/deb
    print ("le temps pour remplir la piscine est de {} minute".format(result1))
calcul()

print("Exercice 7\n")

#pi for circle and import math
from math import pi
r=float(input("Taper le rayon d'un cercle :"))
print ("le périmètre du cercle ",r," est :", round(2*pi*r))
print ("l'aire du cercle ",r," est :", round(pi*r**2))


#Make tree
print ("Exercice 8\n")
liste=["```","*","**","***","****","*****","```"]
for i in (liste) :
    print(i)

#Make Fizzbuzz for boucle
print ("Exercice 9\n")


for i in range (0,101):
    if i%15 == 0 :
        print("FIZZBUZZ")
    elif i%3 == 0: 
        print("BUZZ")
    elif i%5 == 0:
        print("FIZZ")
    else :
        print(i)
   
