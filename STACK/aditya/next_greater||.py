def nextGreaterElements(nums):
    # intuition will be to add every element in the stack prior to solve the problem
    # why reversed => while adding to stack, we need to make sure the last element in array should be in the bottom of stack
    # Because it is a circular array and after the last element in nums, the next element should be the first one of the nums
    # so if [5,4,3,2,1] is in nums then after 1, 5 should come, and that means stack top element should be 5 

    # then we are looping from the back of the array
    # next step is we are checking if there is anything in stack smaller than our element in array, then we pop them out until we find some
    # -one bigger than the element in array or until the stack is empty

    stack=[]
    for i in reversed(nums):
        stack.append(i)

    final_answer = [0] * len(nums)

    i=len(nums)-1

    while i>=0:
        while stack and nums[i] >= stack[-1]:
            stack.pop()

        final_answer[i] = stack[-1] if stack else -1 # stack[-1] means the next biggest element in array(stack) and if there are none then 
                                                        # we put -1 there

        stack.append(nums[i])
        i-=1

    return final_answer