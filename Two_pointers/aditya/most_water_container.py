def maxArea(height):
    i =0
    j=len(height)-1
    volume=[]

    while i<j:
        area = min(height[i], height[j]) * (j-i)
        volume.append(area)
        if height[i] <= height[j]:
            i+=1
        
        elif height[i] > height[j]:
            j-=1

    return max(volume)


print(maxArea([1,8,6,2,5,4,8,3,7]))