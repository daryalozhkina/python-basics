row_record = [
    '93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"',
    '93.180.71.3 - - [17/May/2015:08:05:23 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"',
    '80.91.33.133 - - [17/May/2015:08:05:24 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)"',
    '217.168.17.5 - - [17/May/2015:08:05:34 +0000] "GET /downloads/product_1 HTTP/1.1" 200 490 "-" "Debian APT-HTTP/1.3 (0.8.10.3)"',
    '217.168.17.5 - - [17/May/2015:08:05:09 +0000] "GET /downloads/product_2 HTTP/1.1" 200 490 "-" "Debian APT-HTTP/1.3 (0.8.10.3)"',
    '93.180.71.3 - - [17/May/2015:08:05:57 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"',
    '217.168.17.5 - - [17/May/2015:08:05:02 +0000] "GET /downloads/product_2 HTTP/1.1" 404 337 "-" "Debian APT-HTTP/1.3 (0.8.10.3)"',
    '217.168.17.5 - - [17/May/2015:08:05:42 +0000] "GET /downloads/product_1 HTTP/1.1" 404 332 "-" "Debian APT-HTTP/1.3 (0.8.10.3)"',
    '80.91.33.133 - - [17/May/2015:08:05:01 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)"',
    '93.180.71.3 - - [17/May/2015:08:05:27 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"',
    '217.168.17.5 - - [17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"',
    '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"',
]

correct_requests_IP_address = '93.180.71.3'
correct_requests_date = '17/May/2015:08:05:32 +0000'
requests_IP_address = row_record.split() [0]
requests_date = row_record.split() [3]
print(requests_IP_address, requests_date)

assert requests_IP_address == correct_requests_IP_address
assert requests_date == correct_requests_date


correct_requests_IP_address = ' 93.180.71.3'
correct_requests_date = '17/May/2015:08:05:23 +0000'
requests_IP_address = row_record.split() [0]
requests_date = row_record.split() [3]
print(requests_IP_address, requests_date)

assert requests_IP_address == correct_requests_IP_address
assert requests_date == correct_requests_date


correct_requests_IP_address = '80.91.33.133'
correct_requests_date = '17/May/2015:08:05:24 +0000'
requests_IP_address = row_record.split() [0]
requests_date = row_record.split() [3]
print(requests_IP_address, requests_date)

assert requests_IP_address == correct_requests_IP_address
assert requests_date == correct_requests_date


correct_requests_IP_address = '217.168.17.5'
correct_requests_date = '17/May/2015:08:05:34 +0000'
requests_IP_address = row_record.split() [0]
requests_date = row_record.split() [3]
print(requests_IP_address, requests_date)

assert requests_IP_address == correct_requests_IP_address
assert requests_date == correct_requests_date


correct_requests_IP_address = '217.168.17.5'
correct_requests_date = '17/May/2015:08:05:09 +0000'
requests_IP_address = row_record.split() [0]
requests_date = row_record.split() [3]
print(requests_IP_address, requests_date)

assert requests_IP_address == correct_requests_IP_address
assert requests_date == correct_requests_date



correct_requests_IP_address = '93.180.71.3'
correct_requests_date = '17/May/2015:08:05:57 +0000'
requests_IP_address = row_record.split() [0]
requests_date = row_record.split() [3]
print(requests_IP_address, requests_date)

assert requests_IP_address == correct_requests_IP_address
assert requests_date == correct_requests_date



correct_requests_IP_address = '217.168.17.5'
correct_requests_date = '17/May/2015:08:05:02 +0000'
requests_IP_address = row_record.split() [0]
requests_date = row_record.split() [3]
print(requests_IP_address, requests_date)

assert requests_IP_address == correct_requests_IP_address
assert requests_date == correct_requests_date


correct_requests_IP_address = '217.168.17.5'
correct_requests_date = '17/May/2015:08:05:42 +0000'
requests_IP_address = row_record.split() [0]
requests_date = row_record.split() [3]
print(requests_IP_address, requests_date)

assert requests_IP_address == correct_requests_IP_address
assert requests_date == correct_requests_date


correct_requests_IP_address = '80.91.33.133'
correct_requests_date = '17/May/2015:08:05:01 +0000'
requests_IP_address = row_record.split() [0]
requests_date = row_record.split() [3]
print(requests_IP_address, requests_date)

assert requests_IP_address == correct_requests_IP_address
assert requests_date == correct_requests_date

correct_requests_IP_address = '93.180.71.3'
correct_requests_date = '17/May/2015:08:05:27 +0000'
requests_IP_address = row_record.split() [0]
requests_date = row_record.split() [3]
print(requests_IP_address, requests_date)

assert requests_IP_address == correct_requests_IP_address
assert requests_date == correct_requests_date

correct_requests_IP_address = '217.168.17.5'
correct_requests_date = '17/May/2015:08:05:12 +0000'
requests_IP_address = row_record.split() [0]
requests_date = row_record.split() [3]
print(requests_IP_address, requests_date)

assert requests_IP_address == correct_requests_IP_address
assert requests_date == correct_requests_date


correct_requests_IP_address = '188.138.60.101'
correct_requests_date = '17/May/2015:08:05:49 +0000'
requests_IP_address = row_record.split() [0]
requests_date = row_record.split() [3]
print(requests_IP_address, requests_date)

assert requests_IP_address == correct_requests_IP_address
assert requests_date == correct_requests_date



