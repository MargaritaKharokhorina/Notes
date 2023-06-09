# Краткая инструкция-пояснение 

Приложение релизовано с помощью библиотеки Tkinter. Функции, такие как: 
* открытие и создание файла
* запись в файл
* сохранение

отображены и действительны в окне Tkinter.

Также имеются кнопки, за функционал которых отвечают
**def list_remove_files** (демонстрация списка заметок и удаление; удаление - через относительный путь к файлу) и **def sort_by_date** (сортировка по дате - от раннего к позднему). Вывод этих действий идет в консоль.

Отмечу, что приложение в большей степени рассчитано на локальное использование в связи с тем, что у пользователя должна быть собственная папка с файлами-заметками; и, конечно, оно еще нуждается в доработке, хотя на данный момент уже справляется с обозначенными задачами. 

Пример создания новой заметки и сохранения ее в папку Files на рабочем столе: 

[![1.jpg](https://i.postimg.cc/9f5FNhBc/1.jpg)](https://postimg.cc/RWdBN28Y)
[![2.jpg](https://i.postimg.cc/P5GjdMv4/2.jpg)](https://postimg.cc/8jb3HMHJ)
[![3.jpg](https://i.postimg.cc/VL98LC9P/3.jpg)](https://postimg.cc/PPqcSNFS)
[![4.jpg](https://i.postimg.cc/P5fBXFr1/4.jpg)](https://postimg.cc/qzYmQwK7)
[![5.jpg](https://i.postimg.cc/W1J0ks3V/5.jpg)](https://postimg.cc/3kYyM5mf)

Для того чтобы отредактировать файл, достаточно просто снова открыть его, внести необходимые измения и заново сохранить - заменить **(def save_as)**:

*исправлено red на orange и добавлен новый цвет*
[![6.jpg](https://i.postimg.cc/pX5m0qtY/6.jpg)](https://postimg.cc/JGm7030G)



