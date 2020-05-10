# def canConstruct(ransomNote: str, magazine: str):
#     if ransomNote == magazine == "":
#         return True

#     dict = {}
#     for i in ransomNote:
#         if i not in dict:
#             dict[i] = 1
#         else:
#             dict[i] +=1
#     for i in magazine:
#         if i in ransomNote:
#             return dict[i]==magazine.count(i)
#     print(dict)
def canConstruct(ransomNote: str, magazine: str):
    
    if len(ransomNote) > len(magazine):
        return False
    
    dict = {}
    for i in magazine:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] +=1
    for char in ransomNote:
        
        if char not in dict:
            return False
        if dict[char]<=0:
            return False
        dict[char] -= 1
        
    return True

print(canConstruct("aa","aab"))