class Pocs:
    def __init__(self,sor:str):
        adatok=sor.strip().split("  ")
        self.vmi=float(adatok[0])
        self.vmi2=int(adatok[1])
        self.vmi3=adatok[2]
        
pocs:list[Pocs]=[]
file=open("csv/txt" , "r/w" , encoding="utf-8")
fejlec=file.readline()
for sor in file:
    pocs.append(Pocs(sor))
file.close()

print(f"{len(pocs)}")
van=False
szamlalo=0
for i in pocs:
    if vmi1==vmi2:
        szamlalo+=1
        van=True
if van==True:
    print("")
else:
    print("")
max=pocs[0].vmi
valami=""
valami2=""
for i in pocs:
    if max<i.vmi:
        max=i.vmi
        valami=i.vmi2
        valami2=i.vmi3
        
        /n/t
        
valamiszotar={}
for i in pocs:
    if i.vmi not in valamiszotar:
        valamiszotar [i.vmi2]=1
    else:
        valamiszotar[i.vmi2]+=1

for i in valamiszotar:
    if valamiszotar[i]>0:
        print(f"\t{i}: {valamiszotar[i]} darab")