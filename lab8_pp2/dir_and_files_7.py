with open('text.txt','r') as text, open('text2.txt','a') as text2: 
	for line in text: 
			text2.write(line)

print("done")