def solution(price):
    
    if 1000000 >= price >= 500000:
        price = price * 0.8
        
    elif price >= 300000:
        price = price * 0.9
        
    elif price >= 100000:
        price = price * 0.95

    return int(price)


solution(150000)