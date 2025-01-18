import pyAesCrypt
import os

def encryption(file, password):
    buffer_size = 512 * 1024
    try:
        pyAesCrypt.encryptFile(
            str(file),
            str(file) + '.cmp',
            password,
            buffer_size
        )
        print(f"[Файл {os.path.basename(file)} зашифрован]")
        os.remove(file)
    except Exception as ex:
        print(f"Ошибка при шифровании {file}: {ex}")

def walking_by_dirs(directory, password):
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            try:
                encryption(path, password)
            except Exception as ex:
                print(f"Ошибка: {ex}")

# Безопасный ввод директории
while True:
    directory = input('Введите полный путь к директории для шифрования: ')
    if os.path.exists(directory):
        break
    else:
        print("Указанная директория не существует. Попробуйте снова.")

password = input('Введите пароль для шифрования: ')
walking_by_dirs(directory, password)
