from hashlib import md5

def power(h, m):
    return md5(h.encode('utf-8') + m.encode('utf-8')).hexdigest()[:4]


def val(hl, m, hr):
    return power(hl, m), power(hr, m)


def AHash(hl, hr, M):
    message = list(map(''.join, zip(*[iter(M)] * 4)))
    for m in message:
        hl, hr = val(hl, m, hr)
        #print hl
        #print hr
    return hl + hr

charset = 'abcdefghijklmnopqrstuvwxyz1234567890'

f = open("hl.txt","w+")

for M in range(10000):
    print(M)
    for hr1 in charset:
        for hr2 in charset:
            for hr3 in charset:
                for hr4 in charset:
                    hr = hr1+hr2+hr3+hr4
                    ans = power(hr,str(M).zfill(4))
                    #print(ans)
                    if(ans == 'cbe9'):
                        #print(M,hr)
                        f.write(str(M)+","+hr+"\n")
            #l,r = val(hl,str(M).zfill(4),hr)
            #if((r=='cbe9') and (l=='88e6')):
            #    print (M,l,r)
    #if (M%100==0):
