def get_summ(one, two, delimiter='&'):
    return str(str(one)+delimiter+str(two))

summ= get_summ("Learn", "python")
print (summ)
print(summ.upper())