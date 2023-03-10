test = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

inp = test.split("\n")

class valve:
    def __init__(self,name,flow,to) -> None:
        self.name = name
        self.flow = flow
        self.to = to
        if flow == 0:
            self.kiinni = False
        if flow > 0:  
            self.kiinni = True
    def __repr__(self) -> str:
        return f"{self.name} {self.flow} {self.to}"

    def __repr__(self) -> str:
        return f"{self.to} {self.kiinni}"

venttiilit = {}

for i in inp:
    alku , loppu = i.split(";")
    alku , flow = alku.split("has flow rate=")
    name = alku.strip("Valve ")
    to = loppu.strip(" tunnels lead to valves ")
    venttiilit[name] = valve(name,int(flow),list(map(lambda x: x.strip(), to.split(","))))

#print(venttiilit)

def reitti(venttiilit,nimi,aika,releaseCum,avattu):
    if aika <= 0 or avattu == len(venttiilit):
        print(releaseCum,avattu,len(venttiilit))
        return releaseCum
    aika -= 1
    if venttiilit[nimi].flow > 0 and venttiilit[nimi].kiinni and aika > 0:
        aika -=1
        releaseCum += venttiilit[nimi].flow * aika 
        venttiilit[nimi].kiinni = False
        avattu += 1
    retReleaseCums = []
    for nextNimi in venttiilit[nimi].to:
        retReleaseCums.append(reitti(venttiilit,nextNimi,aika,releaseCum,avattu))
    return max(retReleaseCums)
print(reitti(venttiilit,"AA",30,0,0))
