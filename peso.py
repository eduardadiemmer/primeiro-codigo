print("qual seu peso?")
peso = input()
 
while(type(peso) == str):
    
    try:
        peso = float(peso)

    except:
        print("insira um valor válido")  
        peso = input()

if peso <= 20:
    print("magricelo")

elif peso >20 and peso <=30:
    print("saudável")

elif peso >30:
    print("obeso")

else:
    print("insira um valor válido")

 
