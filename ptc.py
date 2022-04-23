def alpha(s):
    for i in range(len(s)):
        if(s[i].isalnum()):
            return True
            break
    return False
def alphbet(s):
    for i in range(len(s)):
        if(s[i].isalpha()):
            return True
            break
    return False
def digt(s):
    for i in range(len(s)):
        if(s[i].isdigit()):
            return True
            break
    return False
def low(s):
    for i in range(len(s)):
        if(s[i].islower()):
            return True;
            break
    return False
def upp(s):
    for i in range(len(s)):
        if(s[i].isupper()):
            return True
            break
    return False
if __name__ == '__main__':
    s = input()
    print(alpha(s))
    print(alphbet(s))
    print(digt(s))
    print(low(s))
    print(upp(s))