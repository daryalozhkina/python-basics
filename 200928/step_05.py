src_data_file = 'nginx_logs_head.txt'
parsed_data_file = 'nginx_logs_parsed.txt'

parsed_data = []

def row_parse(row):
    remote_IP_address, row_tail = row.split(maxsplit=1)
    _, _request_datetime = row_tail.split('[', maxsplit=1)
    request_datetime, row_tail = _request_datetime.split(']', maxsplit=1)

    _, _request_method, row_tail = row_tail.split('"', maxsplit=2)
    request_method, requested_resource, _ = _request_method.split(maxsplit=2)

    parsed_row = [remote_IP_address, request_datetime, request_method, requested_resource]
    return list(map(str.strip, parsed_row))

def file_parse(f_name: str) -> list:
        parsed_data = []
        with open(src_data_file, 'r', encoding='utf-8') as f:
            for row in f.read().splitlines():
                if not row:
                    continue
                parsed_row = row_parse(row)
                parsed_data.append(parsed_row)
        return  parsed_data

def save_parsed_data(f_name, data):
    with open(parsed_data_file, 'w', encoding='utf-8') as f:
        for row in data:
            f.write(f"{', '.join(row)}\n")

parsed_data = file_parse(src_data_file)
save_parsed_data(parsed_data_file, parsed_data)
        #print(parsed_data)

