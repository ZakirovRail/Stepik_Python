import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# element.send_keys(file_path)

print(os.path.abspath(__file__))                    #/Users/anastasia/Documents/GitHub/Stepik_Python/Selenium_Python/environments/chapter_2/2_2_add_file.py
print(os.path.abspath(os.path.dirname(__file__)))   # /Users/anastasia/Documents/GitHub/Stepik_Python/Selenium_Python/environments/chapter_2



