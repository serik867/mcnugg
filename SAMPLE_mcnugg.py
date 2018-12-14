
def mcnugg(x):
    mcnumbs=[0]
    i=1
    not_nug=[]
    while i<=x:
        if i-6 in mcnumbs or i-9 in mcnumbs or i-20 in mcnumbs:
            mcnumbs.append(i)
            i+=1
        else:
            i+=1
            not_nug.append(i)
    return not_nug

value = input('Choose a number: ')
value= int(value)

answer = mcnugg(value)
print(answer)

