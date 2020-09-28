row = '217.168.17.5 - - [17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"'
#_row_splitted = row.split(maxsplit=1)
#remote_IP_address = _row_splitted[0]
#row_tail = _row_splitted[1]

#print(remote_IP_address)
#print(row_tail)

#[first_name, last_name, age] = []

remote_IP_address, row_tail = row.split(maxsplit=1)
_, _request_datetime = row_tail.split('[', maxsplit=1)
request_datetime, row_tail = _request_datetime.split(']', maxsplit=1)
print(request_datetime)
print(row_tail)