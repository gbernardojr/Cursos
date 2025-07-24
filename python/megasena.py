import time
tempoInicial = time.time() 
for a in range(1,61,1):
    for b in range(1,61,1):
        for c in range(1,61,1):
            for d in range(1,61,1):
                for e in range(1,61,1):
                    for f in range(1,61,1):
                        if a!=b and a!=c and a!=d and a!=e and a!=f:
                            if b!=c and b!=d and b!=e and b!=f:
                                if c!=d and c!=e and c!=f:        
                                    if d!=e and d!=f:
                                        if e!=f:
                                            print(a,',',b,',',c,',',d,',',e,',',f)
tempoFinal = time.time()
print('Duração: ',tempoFinal-tempoInicial,'s')
