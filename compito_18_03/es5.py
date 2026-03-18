nome = input("Come ti chiami?")
eta = int(input("Quanti anni hai?"))

if eta <= 0 or eta > 120:
    print(f"età non valida")
else:
    print(f"Ciao {nome}! Tra 5 anni avrai {eta + 5} anni")