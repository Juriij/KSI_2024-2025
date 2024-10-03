def sum(n: int):
    if n <= 0:
        return 0
    
    elif n == 1:
        return 1
    
    return n + sum(n-1)
