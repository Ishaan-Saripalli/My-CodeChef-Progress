class Stack:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
for j in range(int(input())):
    arr=[x for x in input()]
    s=Stack()
    balanced=True
    answer=0
    fanswer=0
    for h in range(len(arr)):
        if arr[h]=="<":
            s.push("<")
        else:
            if s.isempty():

                break
            else:
                s.pop()
                if not s.isempty():
                    balanced=False
                    answer=answer+1
                else:
                    balanced=True
                    fanswer=fanswer+1


                if h==(len(arr)-1) and s.isempty()!=True:
                    answer=0
    if balanced==False: answer=0                
    print((answer+fanswer)*2)
