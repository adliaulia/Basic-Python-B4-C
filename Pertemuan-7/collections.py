thisList = ["Apple", "Banana", "Cherry"]
thisTupple = ("Apple", "Banana", "Cherry")
thisSets = {"Apple", "Banana", "Cherry"}

print(thisList)
print(thisTupple)
print(thisSets)

print(thisList[0])
print(thisTupple[2])

for x in thisSets:
    if x == "Banana":
        print(x)

thisList.append("Anggur")
print(thisList)

addTupple = "Anggur"
thisTupple = (*thisTupple, addTupple)
thisSets.add("Anggur")
print(thisList)
print(thisList)
print(thisTupple)