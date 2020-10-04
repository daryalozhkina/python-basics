with open('nginx_logs_head.txt', 'r', encoding='utf-8') as f:
    for row in f.read().splitlines():
        print(row)