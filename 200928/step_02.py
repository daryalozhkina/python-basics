f = open('nginx_logs_head.txt', 'r', encoding='utf-8')
#print(type(f))
#print(dir(f))

#file_data = f.read().splitlines()
#print(file_data)

#print(type(f.readlines()))

for row in f.read().splitlines():
    print(row)

print(f.closed)
f.close()
print(f.closed)