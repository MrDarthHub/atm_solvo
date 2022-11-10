#if __name__ == '__main__':

#def main():    # Implementar esta funcion como la principal
print("Welcome to solvo bank!")
withdraw = int(input("Please insert the amount of money that you want to withdraw: "))



'''                     Intento de verificacion del monto y retorno del mensaje de error
listBancnote = []
def verification(withdraw):
    bancnotes = [10000, 5000, 2000]
    if  withdraw == 0:
        for bancnote in bancnotes: 
            while withdraw >= bancnote:
                withdraw -= bancnote
                listBancnote.append(bancnote)
                print(':)')
    elif withdraw >= bancnote != 0:
        print( 
            """
            
            I'm sorry but this transaction failed because the ATM does not have the banc notes that you are requesting
            
            """)
    else:
        return False


verification(withdraw)

'''



listTransactions = []
listBancnote = []
def get_cash(withdraw):
    bancnotes = [10000, 5000, 2000] #Falta: si no se puede entregar el monto exacto devolver un mensaje de error
    
    for bancnote in bancnotes: 
        while withdraw >= bancnote:
            withdraw -= bancnote
            listBancnote.append(bancnote)
    if withdraw:
        print(f"Falto: {withdraw}")

get_cash(withdraw)
print('Su dinero es '+ str(listBancnote.count(2000)) +' billetes de 2000, '+ str(listBancnote.count(5000)) +' billetes de 5000 y '+ str(listBancnote.count(10000)) +' billetes de 10 000.' )
listTransactions.append('Su dinero es '+ str(listBancnote.count(2000)) +' billetes de 2000, '+ str(listBancnote.count(5000)) +' billetes de 5000 y '+ str(listBancnote.count(10000)) +' billetes de 10 000.' )


"""
    Falta
    1. Inplementar la funcion para que cuando se termine el un ciclo se inicie otro (preguntando por el monto)
    2. Retornar un mensaje de error cuando no se puede dispensar la cantidad con la cantidad de billetes disponibles
    3. Guardar una bitacora de cada transaccion (Usar listTransactions)
    4. Hacer un listado de las bitacoras y protejida con autenticacion

"""
