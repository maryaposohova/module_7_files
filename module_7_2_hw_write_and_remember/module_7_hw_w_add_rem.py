def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    print(file.tell())
    for str_1 in info:
        string_info= str(str_1)
        file.write(string_info + '\n')
    print(file.tell())

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', [info])
for elem in result.items():
  print(elem)