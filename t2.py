
con0 = 1
con1 = 0
con2 = 0
con3 = 0
con2_1 = 0
con2_2 = 0
while con0:
    a = str(input())


    if len(a) >= 8:
        con1 = 1
    else:
        con1 = 0


    for i in range(0,len(a)+1):
        if con2_1 == 1 and con2_2 == 1 :
            con2 = 1
        else:
            if a[i].isupper() == True:
                con2_1 = 1
            else:
                con2_2 = 1


    for j in range(0, len(a)):
        b=a[j]
        if not(str.isalpha(a[j])):
            con3 = 1



    if con1 == 1 and con2 == 1 and con3 == 1:
        con0 = 0







print(a)