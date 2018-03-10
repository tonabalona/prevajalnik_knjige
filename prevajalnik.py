import json
import os

print("Mehanicni Dedo 1.0")

knjiga = open("knjiga.txt", mode="rt")
besede = []
for line in knjiga:
    line = line.lower()
    besede = besede + line.split(" ")

if os.path.isfile('prevodi.json'):
    with open('prevodi.json', 'r') as fp:
        prevodi = json.load(fp)
else:
    prevodi = {}

rezultat = []

for b in besede:
    if b in prevodi:
        rezultat.append(prevodi[b])
    else:
        prevodi[b] = input("Prevod za " + b + ":\n")
        rezultat.append(prevodi[b])


with open('prevodi.json', 'w') as fp:
    json.dump(prevodi, fp)

print("Original:")
for b in besede:
    print(b, end=" ")
print()
print()
print("Prevedeno:")
for b in rezultat:
    print(b, end=" ")
print()