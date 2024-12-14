class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def __str__(self):
        return f'{self.file_names}'

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    reader_file = file.read().lower()
                    for znaki in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        reader_file = reader_file.replace(znaki, '')
                    words = reader_file.split()
                    all_words[file_name] = words
                    # print(reader_file)
            except:
                print("Ошибка при работе с файлами")
        return all_words

    def find(self, word):
        find_words = {}
        for file_name, words in self.get_all_words().items():
            if word.lower() in words:
                position = words.index(word.lower())
                find_words[file_name] = position+1
            return find_words

    def count(self, word):
        count_words = {}
        for file_name, words in self.get_all_words().items():
            count_ = words.count(word.lower())
            count_words[file_name] = count_
        return count_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
