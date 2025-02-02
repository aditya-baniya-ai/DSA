
# This is using two pointers but it doesnot pass all the test cases
# So now i will post the one using stacks

def dailyTemperature(array):
    
    final_array = []
    
    for i in range(len(array)):
        isBreak = True
        j=i
        while j<len(array) and isBreak:
            if array[j] > array[i]:
                final_array.append(j-i)
                isBreak=False
                
            j+=1
            
        if isBreak:
            final_array.append(0)
            
            
    return final_array

print(dailyTemperature([73,74,75,71,69,72,76,73]))