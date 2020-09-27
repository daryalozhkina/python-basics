row_record = '217.168.17.5 - - [17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"'

correct_requests_IP_address = '217.168.17.5'
correct_requests_date = '17/May/2015:08:05:12 +0000'
requests_IP_address = row_record.split() [0]
requests_date = row_record.split() [3]
print(requests_IP_address, requests_date)

assert requests_IP_address == correct_requests_IP_address
assert requests_date == correct_requests_date