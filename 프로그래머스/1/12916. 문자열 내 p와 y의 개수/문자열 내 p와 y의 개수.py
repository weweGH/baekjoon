def solution(s):
    ll = s.upper()
    
    if len([x for x in ll if x == 'P']) == len([x for x in ll if x == 'Y']):
        return True
    else:
        return False
