# буфер бот

данный бот был высран на стриме по metal gear rising у [JEIKO](https://t.me/jeikohub), из-за локального мема про фильтр твича.  
имеет функцию уборки сообщений по каким-то словам через regex.

## сетап

для бота нужны следующие библиотеки: `disnake, colorama`, остальные идут с питоном.

сетап *максимально* лёгкий, после клона репозитория надо создать файл `env.py`, туда надо написать:
```py
TOKEN = "сюда вставить токен своего дискорд бота"
BANWORDS = ["слова", "для", "чистки"]
```
в список банвордов можно закинуть **какие хотите** слова, пример выше.

запускаем бота через `python bot.py` в консоли и кайфуем.
