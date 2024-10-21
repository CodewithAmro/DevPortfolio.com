class sorted_stack:
    def __init__(self):
        self.stack1=[]

        self.temp=0

    def sort_the_stack(self,Mystack):

        last_val=Mystack.pop()

        self.temp=last_val

        for variables in Mystack:

            if variables<=self.temp:
                self.stack1.append(variables)
                
            else:
                self.temp=variables
      
            
            
        
s=sorted_stack()
mystc=[1,4,2,6,2,8,3,6,1]
answer=s.sort_the_stack(mystc)
print(answer)