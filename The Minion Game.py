def minion_game(string):
    # eg - [ BANANA ]
    #      [ 012345 ]
    vowels = 'AEIOU'
    kev = 0
    stu = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kev += (len(s)-i)  #first occurance 6-1 , since s[1]=A
        else:
            stu += (len(s)-i)  #first occurance 6-0 , since s[0]=B

    if kev > stu:
        print ("Kevin", kev)
    elif kev < stu:
        print("Stuart", stu)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
    
"""
Input (stdin)
  BANANA
Output
  Stuart 12
"""
