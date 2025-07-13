class Lombok:
    def __init__(self):
        self.stack=[]
        self.reg=[0] 

    def push(self,x):
        self.stack.append(x)

    def store(self):
        self.reg[0]=self.stack.pop(-1)

    def load(self):
        self.stack.append(self.reg[0])

    def plus(self):
        a=self.stack.pop()
        b=self.stack.pop()
        self.stack.append(a+b)

    def times(self):
        a=self.stack.pop()
        b=self.stack.pop()
        self.stack.append(a*b)

    def ifzero(self,n):
        if self.stack.pop(-1)==0:
            return int(n)-1
        return None

    def done(self):
        print(self.stack.pop())


lvm=Lombok()

n=int(input())
instructions=[input().split() for i in range(n)]

i=0
while i<n:
    instr=instructions[i][0]
    print(lvm.stack)
    if instr=='PUSH':
        lvm.push(int(instructions[i][1]))
        i += 1
        
    elif instr=='STORE':
        lvm.store()
        i+=1
        
    elif instr=='LOAD':
        lvm.load()
        
    elif instr=='PLUS':
        lvm.plus()
        i+=1
    elif instr=='TIMES':
        lvm.times()
        i+=1
    elif instr=='IFZERO':
        jump=lvm.ifzero(instructions[i][1])
        if jump is not None:
            i=jump
        else:
            i+=1
    elif instr=='DONE':
        lvm.done()
        break
