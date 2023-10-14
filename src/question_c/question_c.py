#write functions here, don't add input('') statements here!

def get_sum_of_evens(num):
    if num % 2 == 1:
        num - 1
    sum = 0
    now_even = num
    for x in range(0, (now_even+1), 2):
        sum += x
    return sum