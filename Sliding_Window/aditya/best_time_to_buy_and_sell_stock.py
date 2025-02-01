""" 
    logic: first finding the first smallest left element 
    then appending the j-i element to array
    and returning the max from the array
"""


def maxProfit(prices):
    i= 0
    j=1

    output=[0]

    while i<j<len(prices):
        if prices[j] < prices[i]:
            i = j
            j = i+1

        else:
            output.append(prices[j]-prices[i])
            j+=1

        
    return max(output)


print(maxProfit([7,1,5,3,6,4]))