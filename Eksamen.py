
#INF100 -H20 -Eksamen

# SPM 2 (svarene i kommentarene under)
print("SPM 2")

a = []
b = "True"
c = 42
d = -1.5

#print(type(a*b)) # error (kan ikke gange liste med str)
print(type(b*c)) # str
#print(type('b' + c)) # error (kan ikke plusse str og int)
print(type(c*a)) # list
print(type(c == 10.3)) # bool
print(type(a+a)) # list
#print(type(len(c))) # error (int har ingen len attribute)
print(type(f"{int(d) + c}")) #str
print(type([b])) # list
#print(type(a+b)) # error (kan ikke plusse på str til listen

# SPM 3
print("SPM 3: ")
a = 450
if a > 100: # if a(450) er stoerre enn 100 print 'A'
    print('A')
if a > 400: # if a er stoerre enn 100 print 'B'
    print('B')
if a % 10 == 0: # if a % 10 = 0 print 'C'
    print('C')
elif(): # hvis ikke skriv 'D' men denne blir aldri kjoert fordi if statement over er True
    print('D')

#SPM 4
print("SPM 4: ")
print("Velg slik at alle sammenligninger er True.")

xs = {
    'a' : 5,
    '5' : 'hello',
    'z' : 3.1415,
     5  : 7
}
print(xs[5] == 7)  # dette er True fordi key 5 har verdi 7
print('5' in xs.keys()) # dette er True fordi den sjekker om '5' er en key i xs og det er den
print(list(xs.items())[-1] == (5,7)) # dette er true fordi en liste av den siste(-1) key og verdien i xs er (5,7)
print(len(xs['5']) == xs['a']) # dette er riktig fordi lengden av 'hello' som er verdien
                               # av key '5' er d samme som verdien til key 'a',

# SPM 5
print("SPM 5: ")
#skriv løkke med while isteden for for.
#sum1 = 0
#for x in xs[:3]:
#    if x > 5:
#        sum1+= x # original for løkke

#i = 0
#sum = 0
#while i <= 3:
#    x = xs[i]
#    if x > 5:
#        sum += x
#    i += 1


#SPM 6
# Spør om 5 ord og skriv ut summen av lengdene
print("SPM 6: ")

length = 0 # variabel som skal holde lengden på ordene
for word in range(5): # for loop 5 ganger
    text = input("Text: ") # spør om input lagre i variabel "text"
    length += len(text) # legge til lengden av input(text) og lagre i length variabel.

print(f"The texts had {length} characters") # skriv ut resultatet til skjermen

#SPM 7
print("SPM 7: ")
# Velg slik at alle sammenligninger er True.

liste = [3, "hei", False, [7]] # samme som xs i oppgave 7 men måtte velge annet navn :)

print(liste[1] == "hei") # fordi index 1 av liste har verdien hei
print('e' == liste[1][1]) # True fordi index 1 er "hei" og index 1 av "hei" er e
print(liste[-1:-3:-1] == [[7], False]) # True fordi splice av liste -1 altså siste index og 3 har verdien False og det matcher [[7], False]
print(len(liste[3]) == 1) # True fordi lengden av [7] er 1.
                            # liste[3] har verdi [7] altså en ny liste med kun en verdi. mindfuck as

#SPM 8
print("SPM 8: ")
print(5 > 7 or 4 > 5) # False
print(True or False) # True fordi når man bruker "or" så er det true om et av argumentene True uans om andre er False
print(18<20<21<27<25) # False
print(list(range(3)) == [1,2,3]) # False fordi det blir [0,1,2]
print(not(not (not False) )) # True
print(False and True) # False fordi når man bruker "and" om et av argumentene e False blir heile uttrykket False
print(5 in range(5)) # False fordi den blir 0,1,2,3,4
print(25 // 2 == 12) # True fordi (//) den tar 25 delt på 12 som blir 12.5 og runder ned til 12
print(list(zip([4],[7])) == [(4,7)]) # True fordi resultatet av dem zippet listene blir en tupel med verdiene.
print([x**2 for x in range(3)] == [0,1,4,9]) # False fordi det blir 0*0 og 1*1 og 2*2 altså [0,1,4]

#SPM 9
# gitt to tall a og b returner True om begge er partall, ellers False
print("SPM 9: ")

def both_even(a,b):
    return a % 2 == 0 and b % 2 == 0

print("Testing 2,4. Result: ", both_even(2,4))
print("Testing 2,5. Result: ", both_even(2,5))

# SPM 10
print("SPM 10")
# Funksjon som sjekker om en liste er sortert fra små til stor,
# returner True eller False
def is_sorted(input):
    x = input[0] # lagrer foerste elementet i listen i en variabel x.
    for e in input[1:]: # tar en loop gjennom elementene, begynner med det andre elementet.
        if x > e: # hvis x(foerste elementet i listen) er stoerre enn andre elementet i listen return False
            return False
        x = e
    return e == x # returnerer True siden listen er sortert stigende

# Tester funksjonen

small_to_big = [2,5,6,8,9]
big_to_small = [9,8,6,5,2]

print(f'Er listen sortert? {is_sorted(small_to_big)}') # skal returnere True
print(f'Er listen sortert? {is_sorted(big_to_small)}') # skal returnere False


#SPM 11 HVOR OFTE FINNES x i input listen
def count(input, x): # funksjonen count, tar to parameter, input(en liste) x(elementet man ønsker å sjekke)
    ct = 0 # counter variabel som holder telling på hvor mange ganger vi har funnet elementet i listen.
    for i in input: # loop gjennom alle elementer i input(listen)
        if i == x: # hvis i (et element i listen) er lik x
            ct += 1 # øk ct(tellingen) med 1.
    return ct # returner tellingen resultatet av for loopen

# Eksempel
input = [1,2,3,4,5,6,7,7,7,8,8,9,10,11,11,11,11]

print(count(input, 7)) # printer ut 3 fordi 7 er i listen 3 ganger
print(count(input, 8)) # printer ut 2 fordi 8 er i listen 2 ganger
print(count(input, 9)) # printer ut 1 fordi 9 er i listen 1 gang
print(count(input, 11)) # printer ut 4 fordi 11 er i listen 4 ganger


#SPM 12
#filename = "foo.txt"
#with open(filename) as f:
 #   line = f.readlines()
 #   for i, line in zip(f):
 #       if 'Alice' in line:
 #           print(f'Alice found in line{i + 1}')
 #           break

# Det riktige svaret ^

