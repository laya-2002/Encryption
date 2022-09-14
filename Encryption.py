from random import randint as rn    

class Encryption:
    def __init__(self,s): 
        self.s=s 
        self.n=len(self.s)
        self.keys=[]
        self.matrix=[[1 for j in range(5)] for i in range(5)]
        self.m=dict()
        self.encrypt()

    def display(self):
        print(self.s)

    def gen(self):
        p=set()
        p.add('j')
        k=""
        n=rn(4,9)
        r=0
        while(r<n): 
            c=chr(rn(97,122))
            if(c in p):
                continue
            else:
                p.add(c)
                k+=c 
                r+=1 
        return k 

    def genM(self): 
        self.m['j']=[-1,-1]
        n=len(self.keys[1])
        i=0 
        c=0 
        h=97 
        while(i<5):
            j=0 
            while(j<5): 
                if(c<n): 
                    self.matrix[i][j]=self.keys[1][c] 
                    self.m[self.keys[1][c]]=[i,j]
                    c+=1 
                else: 
                    while(chr(h) in self.m): 
                        h+=1 
                    self.matrix[i][j]=chr(h)
                    self.m[chr(h)]=[i,j]
                    h+=1 
                j+=1 
            i+=1 

    def playFair(self): 
        k=self.gen()
        self.keys.append(k)
        self.genM()
        temp=""
        i=0 
        t=0
        l=self.n 
        while(i<(self.n-1)):
            p1=self.s[i]
            p2=self.s[i+1]
            if(p1=='j'):
                p1='i'
            if(p2=='j'):
                p2='i'
            if(p1==p2):
                if(p1=='x'):
                    p2='r'
                else:
                    p2='x'
                t=1 
                l+=1 
            if(self.m[p1][0]==self.m[p2][0]): 
                if(self.m[p1][1]==4): 
                    temp+=self.matrix[self.m[p1][0]][0]                  
                    temp+=self.matrix[self.m[p2][0]][self.m[p2][1]+1]
                elif(self.m[p2][1]==4): 
                    temp+=self.matrix[self.m[p1][0]][self.m[p1][1]+1]
                    temp+=self.matrix[self.m[p2][0]][0]
                else: 
                    temp+=self.matrix[self.m[p1][0]][self.m[p1][1]+1]
                    temp+=self.matrix[self.m[p2][0]][self.m[p2][1]+1]
            elif(self.m[p1][1]==self.m[p2][1]):
                if(self.m[p1][0]==4):
                    temp+=self.matrix[0][self.m[p1][1]]
                    temp+=self.matrix[self.m[p2][0]+1][self.m[p2][1]]
                elif(self.m[p2][0]==4):
                    temp+=self.matrix[self.m[p1][0]+1][self.m[p1][1]]
                    temp+=self.matrix[0][self.m[p2][1]]
                else:
                    temp+=self.matrix[self.m[p1][0]+1][self.m[p1][1]]
                    temp+=self.matrix[self.m[p2][0]+1][self.m[p2][1]]
            else: 
                r1=self.m[p1][0]
                r2=self.m[p2][0]
                c1=self.m[p1][1]
                c2=self.m[p2][1] 
                temp+=self.matrix[r1][c2]
                temp+=self.matrix[r2][c1] 
            if(t==1):
                i+=1 
            else:
                i+=2 
        if(i==l-1): 
            l+=1 
            p1=self.s[self.n-1]
            if(p1=='j'):
                p1='i'
            if(p1=='z'): 
                p2='r'
            else:
                p2='z' 
            r1=self.m[p1][0]
            r2=self.m[p2][0]
            c1=self.m[p1][1]
            c2=self.m[p2][1]
            if(r1==r2):
                if(c1==4):
                    temp+=self.matrix[r1][0]
                    temp+=self.matrix[r2][c2+1]
                elif(c2==4): 
                    temp+=self.matrix[r1][c1+1]
                    temp+=self.matrix[r2][0]
                else:
                    temp+=self.matrix[r1][c1+1]
                    temp+=self.matrix[r2][c2+1]
            elif(c1==c2):
                if(r1==4):
                    temp+=self.matrix[0][c1]
                    temp+=self.matrix[r2+1][c2]
                elif(r2==4):
                    temp+=self.matrix[r1+1][c1]
                    temp+=self.matrix[0][c2]
                else: 
                    temp+=self.matrix[r1+1][c1]
                    temp+=self.matrix[r2+1][c2]
            else: 
                temp+=self.matrix[r1][c2]
                temp+=self.matrix[r2][c1] 
        self.n=l 
        self.s=temp 

    def caesar(self):
        k=rn(1,25)
        self.keys.append(k)
        temp=""
        for i in range(self.n):            
            c=chr(97+((ord(self.s[i])-97+k)%26))
            temp+=c 
        self.s=temp 

    def encrypt(self):
        self.caesar()
        self.playFair() 
        self.caesar()
        self.display()


s=input()
ob=Encryption(s)
