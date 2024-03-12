import random
import string
random_text = ""
sampleLatters = "ABCDEFJ"
# length - длина строки, characters - символы строки
def generate_random_text(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))

# В 10ом задании - подстрокой счтиается последовательность длиной 2 и более.

file_path = 'generated_text.txt'
random_text += "&" + generate_random_text(50000, string.ascii_letters + string.digits + '?,.!') + "&\n" # 1
random_text += "&" + generate_random_text(50000, string.ascii_letters + string.digits + '?,.!') + "&\n" # 2
random_text += "&" + generate_random_text(50000, string.ascii_letters) + "&\n" # 3
random_text += "&" + generate_random_text(50000, string.ascii_letters) + "&\n" # 4
random_text += "&" + generate_random_text(50000, string.ascii_letters) + "&\n" # 5
random_text += "&" + generate_random_text(50000, string.ascii_letters + string.digits + '?,.!') + "&\n" # 6
random_text += "&" + generate_random_text(50000, '*?.!') + "&\n" # 7
random_text += "&" + generate_random_text(50000, string.ascii_letters + string.digits + '?,.!') + "&\n" # 8
random_text += "&" + generate_random_text(50000, sampleLatters + '?,.!') + "&\n" # 9
random_text += "&" + generate_random_text(50000, 'ABCD2.!') + "&\n" # 10
random_text += "&" + generate_random_text(50000, string.ascii_letters + string.digits + '?') + "&\n" # 11
random_text += "&" + generate_random_text(50000, string.ascii_letters +  '.') + "&\n" # 12
random_text += "&" + generate_random_text(50000, string.ascii_letters + string.digits + '?,.!') + "&\n" # 13
random_text += "&" + generate_random_text(50000, string.digits + 'ABC') + "&\n" # 14

with open(file_path, 'w') as file:
    file.write(random_text)

print(f'Текстовый ффайл "{file_path}" успешно сгенерировал {len(random_text)} символов')