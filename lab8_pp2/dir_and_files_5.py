
nums = [0,1,2,3]
file = open('text.txt','w')

for i in nums:
            file.write(str(i) + '\n')
file.close()
