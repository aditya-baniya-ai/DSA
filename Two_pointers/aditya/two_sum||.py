def two_sum(numbers, target):
    i=0
    j=len(numbers)-1
    
    while(i<j):
        suma = numbers[i] + numbers[j]
        if suma > target:
            j-=1
            
        elif suma < target:
            i+=1
            
        else:
            return [i+1,j+1]
        
