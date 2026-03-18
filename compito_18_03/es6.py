parola = input("Scegli una parola:")

if len(parola) <5:
    print(f"Parola corta")
elif len(parola) >=5 and len(parola) <=8:
    print(f"Parola media")
else:
    print(f"Parola lunga")