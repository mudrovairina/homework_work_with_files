dict_with_len = {}
dict_with_text = {}

with open('1.txt', encoding='utf-8') as file:
    data = file.readlines()
    name = file.name
    dict_with_len[name] = len(data)
    dict_with_text[name] = data

with open('2.txt', encoding='utf-8') as file:
    data = file.readlines()
    name = file.name
    dict_with_len[name] = len(data)
    dict_with_text[name] = data

sorted_by_len = sorted(dict_with_len.values())
for len_1 in sorted_by_len:
    for name, len_2 in dict_with_len.items():
        if len_1 == len_2:
            with open('3.txt', 'a', encoding='utf-8') as file:
                file.writelines(f'{name}\n')
                file.writelines(f'{dict_with_len[name]}\n')
                file.writelines(dict_with_text[name] + ['\n'])
