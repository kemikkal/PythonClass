l1 = [1,3,6,7,3,6,8,4,7,8]
l2 = [0,3,1,6]
def comp():
    global l1, l2
    for i in range (0 , len(l2)):
        for x in range (0 , len(l1)):
            if l2[i] == l1[x]:
                return True
            else:
                continue


print(comp())
