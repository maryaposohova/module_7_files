# def custom_write(file_name, strings):
#     file = open(file_name, 'a', encoding='utf-8')
#     print(file.tell())
#     for str_1 in strings:
#         string_info= str(str_1)
#         file.write(string_info + '\n')
#         strings_positions = {[0], file.tell()}
#         return  strings_positions
#
#
# info = [
#     'Text for tell.',
#     'Используйте кодировку utf-8.',
#     'Because there are 2 languages!',
#     'Спасибо!'
#     ]
#
# result = custom_write('test.txt', info)
# for elem in result.items():
#   print(elem)



# def custom_write(file_name, strings):
#     file = open(file_name, 'a', encoding='utf-8')
#     start_ = file.tell()
#     for str_1 in strings:
#         string_info= str(str_1)
#         file.write(string_info + '\n')
#         for num_str in enumerate(str_1):
#             n_s = num_str
#     return {(n_s, start_): string_info}


# def custom_write(file_name, strings):
#     results = []
#     file = open(file_name, 'a', encoding='utf-8')
#     for index, str_1 in enumerate(strings, start=1):
#         start_ = file.tell()
#         string_info = str(str_1)
#         file.write(string_info + '\n')
#         results.append(((index, start_), string_info))
#     file.close()
#     return results
#
#
# info = [
#     'Text for tell.',
#     'Используйте кодировку utf-8.',
#     'Because there are 2 languages!',
#     'Спасибо!'
# ]
#
# result = custom_write('test.txt', info)
# for elem in result:
#     print(elem)


def custom_write(file_name, strings):
    results = {}
    file = open(file_name, 'a', encoding='utf-8')
    for index, str_1 in enumerate(strings, start=1):
        start_ = file.tell()
        string_info = str(str_1)
        file.write(string_info + '\n')
        results[index] = (start_, string_info)
    file.close()
    return results


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)



