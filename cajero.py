i=0
saldo = 1000
saldo_ini =(f"{saldo:,.2f}")
numero_operaciones = int(input("ingrese el numero de operaciones:"))

while i < numero_operaciones :
    print("menu:")
    print("1-> consultar saldo")
    print("2-> retirar dinero")
    print("3-> deporsitar dinero")
    print("0-> salir")
    operacion = int(input("elige una opcion:"))
    
    if operacion == 1 :
        print(f"tu saldo actual es de:{saldo}")
    elif operacion == 2:
        while True :
            monto_retiro = float(input("ingrese su monto a retirar:"))
            if monto_retiro > saldo :
                print("fondos insuficientes")
            elif monto_retiro< 0:
                print("error,colque un valor correcto.")
            elif monto_retiro > 0 and monto_retiro <= saldo :
                print(f"su saldo actual es de:{saldo - monto_retiro}")
                break
    elif operacion == 3:
        while True:
            monto_consignar = float(input("ingrese su monto a consignar"))
            if monto_consignar < 0 :
                print("error, ingrese un valor correcto")
            elif monto_consignar > 0 :
                print(f"su saldo actual es de:{saldo + monto_consignar}")
                break
    
    if operacion == 0 :
        print ("gracias por usar nuestro cajero")
        break
    else:
        print("opcion incorrecta")
    i+=1        
            


