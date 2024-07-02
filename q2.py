def search(nums , target , left , right):
    nums.sort()
    if left <=right:
        mid = left +(right - left )//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return search(nums , target , mid + 1, right)
        else:
            return search(nums ,target, left , mid -1)
    else:
        return -1

nums = [8,1,2,3,4,5,6,7,0,9]
target=int(input("Please enter element to search:"))
left,right=0,len(nums)-1
result=search(nums,target,left,right)
if(result != -1):
    print("Your element found at : ",result)
else:
    print("Your element not found")