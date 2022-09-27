def sumList(nums):
    '''Return the sum of the numbers in the list nums.'''
    sum = 0
    for num in nums:
        sum = sum + num
    return sum

def main():
    print(sumList([1, 4, 5, 6]))
    print(sumList([10, 12, 14, 16]))
    print(sumList([43, 18, 29, 300]))

main()
