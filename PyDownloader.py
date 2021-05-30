from __future__ import unicode_literals
import youtube_dl
import easygui as g
import pyperclip
import os
url = g.buttonbox(title = 'Ссылка на файл' , msg = "               Скопируйте ссылку и нажмите кнопку 'СКАЧАТЬ'",
choices = ['  СКАЧАТЬ  '])
if url == "  СКАЧАТЬ  " :
    link = pyperclip.paste()
if link == '':
    fail = g.msgbox(title="Ошибка!" , msg = "  В буфере нет ссылки  , скопируйте ссылку  и попробуйте снова")
    quit(0)
save = g.diropenbox(title = "Выберите папку для сохранения")
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    os.chdir(save)
    ydl.download([str(link)])
info = g.msgbox (title = "Успех! ",msg="Ваш файл скачался , и находится по пути:" + "\n" + save)
