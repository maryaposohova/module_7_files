import tkinter

window = tkinter.Tk()  # экземпляр
window.title('Проводник')  # поменяли название
window.geometry("350x350")  # задали размер
window.configure(bg='black')
window.resizable( False, False)  # запретили изменять размер, задав его
text = tkinter.Label(window, text='Файл', height=5, width=20, background='silver')   # размещаем текст, изначально наз Файл
text.grid(column=1, row=1)   # текст будет находиться в 1 колонне и 1 ряду, грид это сетка
button_select = tkinter.Button(window, height=5, width=20, text="Выбрать файл")  # кнопка
button_select.grid(column=1, row=2)  # размещаем кнопку



window.mainloop()  # постоянное обновление окна

