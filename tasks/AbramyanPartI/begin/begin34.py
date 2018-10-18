weightOfBounce = int(input('Input weightOfBounce: '))
priceOfBounce = int(input('Input priceOfBounce: '))
weightOfIris = int(input('Input weightOfIris: '))
priceOfIris = int(input('Input priceOfIris: '))

kg1ofBounce = priceOfBounce / weightOfBounce
kg1ofIris = priceOfIris / weightOfIris

diffBounceIris = kg1ofBounce / kg1ofIris

print(kg1ofBounce, kg1ofIris, diffBounceIris)
