# Deljenje



def deli(a, b, mode): # deli a z b, mode je lahko 0 ali 1,
    # 0 je navadno deljenje, 1 je celoštevilsko, drugače vrne None


    try:
        if mode == 0:
            return a/b
        elif mode == 1:
            return a//b
        else:
            return None
    except:
        return None

print(deli(42, 0, 1))
