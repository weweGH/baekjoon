def solution(s):
    words = s.split(' ')
    result = []
    
    for word in words:
        if word:
            if word[0].isalpha():
                result.append(word[0].upper() + word[1:].lower())
            else:
                result.append(word.lower())
        else:
            result.append('')
    
    return ' '.join(result)
