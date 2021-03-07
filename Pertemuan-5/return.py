def persegi(p,l):
    luas = p*l
    keliling = p+p+l+l
    return luas, keliling

print(persegi(5,2))
luas = persegi(5,2)
print(luas[1])

def putusan(kata):
    if kata == 'y':
        return "YA"
    else:
        return "NO"

print(putusan('y'))

