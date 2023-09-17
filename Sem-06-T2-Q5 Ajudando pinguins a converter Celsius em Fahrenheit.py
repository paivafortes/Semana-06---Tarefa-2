def fahr(c):
    f=(c*(9/5)) + 32
    return f
c=float(input())
conversao=fahr(c)
print(f'{conversao:.2f}')