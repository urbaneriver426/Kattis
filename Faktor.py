import math

def Faktor(totalPublished,impactFactor):
    impactFactor -= 0.99
    result = math.ceil(totalPublished*impactFactor)
    return result
    
x,y = map(int, input().split())
print(Faktor(x,y))
