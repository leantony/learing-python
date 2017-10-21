data = open('alice.txt', 'r')
content = data.read()

i = 0
s = []
for line in content.split():
	i +=1
	s.append(line)

print(len(s))
