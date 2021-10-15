# a = [1, 2, 5, 10, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]
# N = int(input("Bergan pul miqdorini kiriting: "))
# M = int(input("Jami pul miqdorini kiriting: "))
# k=0
# KupyuraSoni=0
# if N<M:
#     print(0)
# else:
#     k = N - M
#     print("k=",k)
#     for i in range(len(a)-1,-1,-1):
#         while k>=a[i]:
#             k=k-a[i]
#             KupyuraSoni+=1
#             print(a[i],"\t")
            
# print("Kupyura soni", KupyuraSoni)            

# barca = 4
# roma = 1
# hisob = input("hisobni kiriting: ")
# hisob = hisob.split('-')
# barca+=int(hisob[1])
# roma+=int(hisob[0])
# if roma < barca:
#     print("lost")
# else:    
#     print("win")

# N = int(input())
# k=0
# for A in range(1,N+1):
#     for B in range(2,N+1):
#         for C in range(3,N+1):
#             if A<B and B<C and B-A==C-B:
#                 k+=1
                
# print(k)                

# text = input("Sozni kiriting: ")
# text = text.split('#')
# k=0
# matn =''
# for i in text:
#     if k%2==1:
#         matn += i+")"
#         k+=1
#     elif i== text[-1]:
#         matn+=i        
#     else:
#         matn += i+"("
#         k+=1

# print(matn)        

numbers = input().split()
x = int(numbers[0])
y = int(numbers[1])
