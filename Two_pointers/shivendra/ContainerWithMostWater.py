def maxArea(height):
        
        maxarea = 0
        l, r = 0, len(height)-1 #simple two pointer approach

        while (l<r):
            #area = min of height to hold the water * width 
            area = min(height[l], height[r]) * (r-l)
            maxarea = max (maxarea, area)
            #update the pointer such as more height could be achieved
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxarea

print(maxArea([1,8,6,2,5,4,8,3,7]))
