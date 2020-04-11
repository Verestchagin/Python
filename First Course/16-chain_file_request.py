Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое последнего файла из набора, как ответ на это задание.

-------------
import requests

with open('text.txt', 'r') as fin:
    x = fin.readline().strip().split()
    print(x[0])
    r = requests.get(x[0])
    words = r.text.splitlines()
    while words[0][0] != 'W' and words[0][1] != 'e':
        fname = ''
        fpath = ''
        fname = words[0]
        fpath = 'https://stepic.org/media/attachments/course67/3.6.3/'
        fpath += fname
        print(fpath)
        r = requests.get(fpath)
        words = r.text.splitlines()
        
for i in range(len(r.text.splitlines())):
    print(r.text.splitlines()[i])
