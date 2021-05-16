def solution(s):
   
    st = ''
    for x in s:
        if x == x.upper():
            st += ' '   
        st += x    
       
    return st
print(solution(input('Write something here: ')))    