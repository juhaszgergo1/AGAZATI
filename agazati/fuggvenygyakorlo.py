def blabla(targy,min,max):
    valami=int(input(targy))
    while valami<min or valami>max:
        print
        valami=int(input(targy))
    return valami

vmi1=blabla("",0,23)
vmi2=blabla("",0,59)
vmi3=vmi1*60+vmi2

nagy = valami_nagyon()
print(f"{nagy[0]:nagy[1]}")
mostnagyon=nagy[0]*60+nagy[1]

if mostnagyon>vmi3:
    print("")
else:
    print(f"")

