row_record = '217.168.17.5 - - [17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"'
#correct_result = '217.168.17.5'
correct_result = [
    '217.168.17.5',
    '- - [17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"']
result = row_record.split(maxsplit=1)
print(result)

assert result == correct_result