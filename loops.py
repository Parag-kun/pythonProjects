def fibonacci(num, memo = {}):
    if num == 0: return 0
    if num == 1: return 1
    if num not in memo: memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo)   
    return memo[num]

print(fibonacci(99))