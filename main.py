# Функция для вывода символов каждый 15-й символ строки, игнорируя повторения
def func1(paragraph):
    seen_characters = set()
    output = ""
    for i, char in enumerate(paragraph):
        if i % 15 == 0 and char not in seen_characters and i!=0:
            output += char
            seen_characters.add(char)
    return output

# Функция для подсчета количества символов в абзаце
def func2(paragraph):
    return len(paragraph)

# Функция для подсчета количества символов 'J' в абзаце
def func3(paragraph):
    return paragraph.count('J')

# Функция для подсчета количества символов 'B' и 'C' в абзаце
def func4(paragraph):
    return paragraph.count('B') + paragraph.count('C')

# Функция для подсчета количества символов 'Y', стоящих после 'B'
def func5(paragraph):
    c = 0
    for i in range(len(paragraph)-1):
        if(paragraph[i] == 'B' and paragraph[i+1]=='Y'):
            c+=1
    return c

# Функция для подсчета количества знаков пунктуации
def func6(paragraph):
    punctuation_chars = ',.?!'
    return sum(paragraph.count(char) for char in punctuation_chars)

# Функция для поиска самой длинной подстроки из символов '*'
def func7(paragraph):
    max_length = 0
    current_length = 0
    for char in paragraph:
        if char == '*':
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    return max_length

# Функция для подсчета суммы всех цифр в абзаце
def func8(paragraph):
    return sum(int(char) for char in paragraph if char.isdigit())

# Функция для поиска длины самой длинной подстроки из символов 'J'
def func9(paragraph):
    max_length = 0
    current_length = 0
    for char in paragraph:
        if char == 'J':
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    return max_length

# Функция для подсчета количества подстрок из символов 'A' и 'D'
def func10(paragraph):
    c = 0
    substr = ""
    flag = False
    for letter in paragraph:
        if letter=="A" or letter =="D":
            substr += letter
            if len(substr)>1:
                flag = True
        else:
            if flag:
                c += 1
            substr = ""
            flag = False

    return c

# Функция для подсчета количества символов, после которых идет знак '?'
def func11(paragraph):
    c = 0
    for i in range(len(paragraph)-1):
        if (paragraph[i] != '?' and paragraph[i + 1] == '?'):
            c += 1
    return c

# Функция для подсчета количества предложений в абзаце
def func12(paragraph):
    sentence_count = 0
    for char in paragraph:
        if char in '.!?':
            sentence_count += 1
    return sentence_count

# Функция для подсчета количества различных символов в абзаце
def func13(paragraph):
    return len(set(paragraph))

# Функция для нахождения максимального количества идущих подряд в неубывающем порядке цифр
def func14(paragraph):
    max_count = 0
    current_count = 1
    for i in range(len(paragraph) - 1):
        if paragraph[i] <= paragraph[i + 1] and paragraph[i].isdigit() and paragraph[i+1].isdigit():
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 1
    return max_count

# Чтение данных из файла
with open("generated_text.txt") as f:
    s = f.readlines()

# Перебор каждого абзаца и выполнение заданных операций
print(f"Абзац 1: {func1(s[0])}")
print(f"Абзац 2: {func2(s[1])}")
print(f"Абзац 3: {func3(s[2])}")
print(f"Абзац 4: {func4(s[3])}")
print(f"Абзац 5: {func5(s[4])}")
print(f"Абзац 6: {func6(s[5])}")
print(f"Абзац 7: {func7(s[6])}")
print(f"Абзац 8: {func8(s[7])}")
print(f"Абзац 9: {func9(s[8])}")
print(f"Абзац 10: {func10(s[9])}")
print(f"Абзац 11: {func11(s[10])}")
print(f"Абзац 12: {func12(s[11])}")
print(f"Абзац 13: {func13(s[12])}")
print(f"Абзац 14: {func14(s[13])}")