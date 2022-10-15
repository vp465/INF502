from itertools import permutations
n=int(input("Maximum shift:"))
ans=input("Which approach you prefer 1.Number of matches, 2.Maximum Chain:")
if ans=="1":
    with open('dna_file1.txt') as f:
        s1 = f.read().replace('\n', '')
    with open('dna_file2.txt') as f:
        s2= f.read().replace('\n', '')
    print(len(s1),len(s2))
    c=0
    m=[]
    for i in range(n+1):
        if(i>0):
            s1="".join([s1,'-'])
            s2="".join(['-',s2])
            for j in range(len(s1)):
                if s1[j]==s2[j]:
                    c=c+1
            print("Shift strings {0},{1}".format(s1,s2))
        else:
            for j in range(0,len(s1)):
                if s1[j]==s2[j]:
                    c=c+1
            print("Shift strings {0},{1}".format(s1,s2))
        m.append(c)
        c=0
    print("Highest score:{0}".format(max(m)))

elif ans=="2":
    with open('dna_file1.txt') as f:
        s1 = f.read().replace('\n', '')
    with open('dna_file2.txt') as f:
        s2= f.read().replace('\n', '')
    cn=0
    ss=[]
    for i in range(1,n+1):
        if(i>0):
            s1="".join(['-',s1])
            s2="".join([s2,'-'])
            for j in range(0,len(s1)):
                for k in range(j,len(s1)):
                    if s1[j:k]==s2[j:k]:
                        cn=cn+1
                    else:
                        break
                ss.append(cn)
                cn=0
    print("The size of maximum contiguous chain that matches the squence is {0}".format(max(ss)))
