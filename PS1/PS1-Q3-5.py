s1 ="Nice to have it"
s2 = "here"
print(s1 + " " +s2)
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])

s=a
s.append(s2)
s.insert(0,s1)
print (s)
