def notas(*n, sit=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if r['media'] >= 7:
        r['situação'] = 'BOA'
    elif r['media'] <= 3:
        r['situação'] = 'RUIM'
    else:
        r['situação'] = 'RAZOÁVEL'
    return r


#programa principal
resp = notas(5.5, 2.5, 6, 8, 5, sit=True)
print(resp)