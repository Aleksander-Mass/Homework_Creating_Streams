# Импорты необходимых модулей и функций
import time
from time import sleep
from threading import Thread

# Определяем функцию для записи слов в файл с задержкой
def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # задержка в 0.1 секунды между записями
    print(f"Завершилась запись в файл {file_name}")

# Запускаем функции с замером времени
start_time = time.time()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

# Вычисляем и выводим время выполнения последовательного запуска
end_time = time.time()
print("Время выполнения функций:", end_time - start_time)

# Определяем время для запуска функций в потоках
start_time_threads = time.time()

# Создаем и запускаем потоки для параллельного выполнения
threads = [
    Thread(target=write_words, args=(10, "example5.txt")),
    Thread(target=write_words, args=(30, "example6.txt")),
    Thread(target=write_words, args=(200, "example7.txt")),
    Thread(target=write_words, args=(100, "example8.txt"))
]

# Запускаем все потоки
for thread in threads:
    thread.start()

# Ждем завершения всех потоков
for thread in threads:
    thread.join()

# Вычисляем и выводим время выполнения с потоками
end_time_threads = time.time()
print("Время выполнения с потоками:", end_time_threads - start_time_threads)

'''
###    Вывод на консоль:
Завершилась запись в файл example1.txt
Завершилась запись в файл example2.txt
Завершилась запись в файл example3.txt
Завершилась запись в файл example4.txt
Время выполнения функций: 34.19624066352844
Завершилась запись в файл example5.txt
Завершилась запись в файл example6.txt
Завершилась запись в файл example8.txt
Завершилась запись в файл example7.txt
Время выполнения с потоками: 20.118637800216675
'''