i=0
saldo = 1000
saldo_ini =(f"{saldo:,.2f}")
num_ope =int(input("ingrese el numero de operaciones:"))
while (i<num_ope):
    print("menu:")
    print("1-> consultar saldo")
    print("2-> retirar dinero")
    print("3-> deporsitar dinero")
    ope = int(input("elige una opcion:"))
    
    if ope == 1 :
        print(f"tu saldo actual es de:{saldo}")
    elif ope == 2:
        monto_retirar =float(input("ingrese su monto a retirar:$"))
        while (monto_retirar > 0) :
            if monto_retirar > saldo :
             print("fondos insuficientes")
            elif monto_retirar >= saldo :
             print("permitido el retiro")
            elif monto_retirar < saldo:
             print(f"su nuevo saldo es de:${saldo - monto_retirar}")
            
            break
        else:
               print("digite un valor correcto")
 
        i+=1     