def machine(n, ini='A', aux='B', fim='C'):
    if n == 2:
        seg = [[ini, aux], [ini, fim], [aux, fim]]
        return seg
    elif n > 2:
        n1 = machine(n-1, ini, fim, aux)
        n1.append([ini, fim])
        n1.append(machine(n-1, aux, ini, fim))
        return n1


print(machine(6))
