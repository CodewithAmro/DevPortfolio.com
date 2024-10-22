from collections import deque

def reverse(queue):
        
        if not queue:
            return False
            
        data=queue.popleft()

        reverse(queue)

        queue.append(data)
q = deque([1, 2, 3, 4, 5])
reverse(q)
print("Reversed queue:", list(q))   # Output: [5, 4, 3, 2, 1]

#expalin the sequence f the line of code 
#explain the storage of the variabe front
#in base case unwind is processed expalin why does the append is happening sucessfully 