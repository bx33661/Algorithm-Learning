def sanjiaoxing(a):
    if (ord(a)>=ord('A') and ord(a)<=ord('Z')):
        for i in range(1,ord(a)-ord('A')+2):
            for j in range(1,ord(a)-i+1-ord('A')):
                print(" ",end="")
            #输出空格

            for k in range(1,i+1):
                print(chr(ord('A')+k-1),end="")
            #正向输出

            for l in range(i-1,0,-1):
                print(chr(ord('A')+l-1),end="")
            print()
sanjiaoxing("F")
