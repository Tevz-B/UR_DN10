import random
import calendar
import os.path
import os
import urllib.request

def podvojeni(xs):
    return list(dict.fromkeys(xs))

def eboran(s):
    s = s[::-1]
    return ' '.join(s.split()[::-1])

def vrzi(kocka):
    v = 0
    s = kocka.split("d")
    for _ in range(int(s[0])):
        v += random.randint(1, int(s[1]))
    return v


def pricakovana_vrednost(kocka, n):
    v = 0
    for _ in range(n):
        v += vrzi(kocka)
    return v/n

def dan(d, m, l):
    dnevi = {0: "ponedeljek",
             1: "torek",
             2: "sreda",
             3: "četrtek",
             4: "petek",
             5: "sobota",
             6: "nedelja"}
    return dnevi[calendar.weekday(l, m, d)]

def najvecja(pot2):
    naj = 0
    for dat in os.listdir(pot2):
        if naj < os.path.getsize(os.path.join(pot2, dat)):
            naj = os.path.getsize(os.path.join(pot2, dat))
            najdat = dat
    return najdat

def an_ban_pet_podgan(xs):
    i = 0
    for _ in range(len(xs) - 1):
        i = (i+10) % len(xs)
        del xs[i]
    return xs

def xkcd():
    t = urllib.request.urlopen("https://xkcd.com/").read().decode("utf-8")
    for l in t.split("\n"):
        if l.startswith("<title>xkcd:"):
            return (l.split(":")[1]).split("<")[0]

#print(xkcd())

def archi():
    s = []
    src = urllib.request.urlopen("https://www.archdaily.com/category/houses").read().decode("utf-8")
    for line in src.split("\n"):
        zacetek = None
        konec = None
        if line.strip().startswith("<a title"):
            if "Studio" in line:
                for i, c in enumerate(line):
                    if c == '"':
                        if zacetek == None:
                            zacetek = i
                        else:
                            konec = i
                            break
                s.append(line[zacetek+1:konec])
    return s

for i in archi():
    print(i)
