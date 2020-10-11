concrete_request = 'https://translate.google.com/?view=home&op=translate&sl=en&tl=ru&text=patronymic'



def parse_get_data(reguest):
    trash, raw_get_data = request.split('?', maxsplit=1)
    get_data = raw_get_data.split('&')
    parsed_get_data_as_dict = {}
    for pair in get_data:
        tmp = pair.split('=')
        parsed_get_data_as_dict[tmp[0]] = tmp[1]
    return parsed_get_data_as_dict

request_1 = parse_get_data('https://translate.google.com/?view=home&op=translate&sl=en&tl=ru&text=patronymic')
print(request_1)
