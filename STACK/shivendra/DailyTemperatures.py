
def dailyTemperatures(temperatures):
        stack = []
        n = len(temperatures)
        res = [0] * n

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t: #lastly added element's t in (t,i)
                stackT, stackI = stack.pop() #storing (t,i)
                res[stackI] = i - stackI #populating the resut with what found and where found
            stack.append((t,i)) #regulat stacking if <t not found
        return res

print(dailyTemperatures([73,74,75,71,69,72,76,73]))