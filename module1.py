import random
def grotte():
    id1=["chaude","froide","bonne"]
    id2=["humide","sec","bonne"]
    id3=["peuplé d'orc","peuplé d'elfe noir","peuplé d'elf noir","peuplé de nain","peuplé de gobelin","peuplé d'insectes","inhabité","peuplé de chauve souris","inhabité","inhabité","peuplé d'insectes","peuplé de chauve souris","peuplé d'insectes","inhabité"]
    a=random.choice(id1)
    b=random.choice(id2)
    c=random.choice(id3)
    print("La température est " + a + " et l'humidité est " + b + ", la grotte est " + c + ".")


print("1=grotte")
a=(str(input("que choississez vous? ")))
if (str(a==1)):
    grotte()
else:
    print("choissisez parmis la liste s'il vous plaits.")