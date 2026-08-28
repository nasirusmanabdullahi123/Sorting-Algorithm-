"""
Create a sorting algorithm that sorts a list of numbers in ascending order 
using the bubble sort technique. The algorithm should iterate through the list multiple times, comparing adjacent elements and swapping them if they are in the wrong order. 
The process should continue until no more swaps are needed, indicating that the list is sorted.

"""
#[1,4,5,6,8,2,3,7] ===> [1,2,3,4,5,6,7,8]

def sorting(num):
    for i in range(len(num)):           
        for j in range(0, len(num)-i-1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]

num = [1,4,5,6,8,2,3,7]
num.sort(num)
print(num)