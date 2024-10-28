ab=input()
result=[]
size=ab.count('a')

for i in range(len(ab)):
    b_count=0
    for j in range(size):
        index=i+j
        if index>len(ab)-1:
            index-=len(ab) 
        if ab[index]=="b":
            b_count+=1
    result.append(b_count)

print(min(result))