#: List[List[int]]

# def findJudge( N, trust):
#     dict =  {}
  
#     count = 0
#     if not trust:
#         return N

#     for i in trust:
#         if i[0] not in trust:
#             dict[i[0]] = 1
#             count += 1
#         else:
#             dict[i[0]] += 1
#             count += 1
   
    
#     if count==N:
#         return -1
#     else:
#         for i in trust:
#             if i[1] in dict:
#                 return -1
#             else:
#                 return i[1]
def findJudge(N, trust):
    if len(trust) < N-1:
        return -1
    indegree = [0]*(N+1)
    outdegree = [0]*(N+1)

    for out_, in_ in trust:
        outdegree[out_] += 1
        indegree[in_] += 1
    for i in range(1, N+1):
        if indegree[i]==N-1 and outdegree[i]==0:
            return i
    return -1
        



print(findJudge(3, [[1,2],[2,3]])) 
print(findJudge(3,[[1,3],[2,3]]))

        