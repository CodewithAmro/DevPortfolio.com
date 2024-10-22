class sort_stack:
    def __init__(self):
        self.stack=[]
       
    def sort_the_stack(self,mystack):
        #we take the number at the head of the stack to compare
        temp=mystack.pop()
        
        for num in mystack:
            
            if num<temp:
                self.stack.append(num)
            else:
                temp=num
                self.stack.append(temp)
                

                
        return self.stack
s=sort_stack()
mystack=[11,23,40,1,4,5,2,6,8,12]
answer=s.sort_the_stack(mystack)
print(answer)