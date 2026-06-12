entrada = float(input())

if(entrada >= 0 and entrada <= 25):
    print("Intervalo [0,25]")
else if(entrada <= 50):
    print("Intervalo [25,50]")
else if(entrada <= 75):
    print("Intervalo [50,75]")
else if(entrada <= 100):
    print("Intervalo [75,100]")
else:
    print("Fora de intervalo")