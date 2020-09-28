#f = open('nginx_logs_head.txt', 'r', encoding='utf-8')
#__enter__
#__exit__
#transaction.atomic()
with open('nginx_logs_head.txt', 'r', encoding='utf-8') as f:
    for row in f.read().splitlines():
        print(row)

#print(f.closed)
#f.close()
#print(f.closed)