num = [10,20,30,40,50,60,70]
target = 50

low = 0
high = len(num)-1

while low<=high:
    mid = (low + high)//2
    if num[mid]==target:
        print("Found at index: ",mid)
        break

    elif num[mid]<target:
        low = mid+1
        
    else:
        high = mid-1

else:
    print("Element not found")