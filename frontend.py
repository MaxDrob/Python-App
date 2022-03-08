from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),bookstack_text.get(),shelf_text.get()):
        list1.insert(END,row)



def add_command():
    backend.insert(title_text.get(),author_text.get(),bookstack_text.get(),shelf_text.get())
    list1.delete(0,END)
    list1.insert(END, (title_text.get(),author_text.get(),bookstack_text.get(),shelf_text.get()))

def delete_command():    
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),bookstack_text.get(),shelf_text.get())    

window=Tk()

window.wm_title("Наши книги")

l1=Label(window,text="Название")
l1.grid(row=0,column=0)

l2=Label(window,text="Автор")
l2.grid(row=0,column=2)

l3=Label(window,text="Стеллаж")
l3.grid(row=1,column=0)

l4=Label(window,text="Полка")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

bookstack_text=StringVar()
e3=Entry(window,textvariable=bookstack_text)
e3.grid(row=1,column=1)

shelf_text=StringVar()
e4=Entry(window,textvariable=shelf_text)
e4.grid(row=1,column=3)

### окно вывода



list1 = Listbox(window, height=10, width=40)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)


scb1=Scrollbar(window)
scb1.grid(row=2,column=2,rowspan=8)

list1.configure(yscrollcommand=scb1.set)
scb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

# кнопки

b1=Button(window, text="Коллекция", width=17, command=view_command)
b1.grid(row=2,column=3)

b2=Button(window, text="Поиск", width=17, command=search_command)
b2.grid(row=3,column=3)

b3=Button(window, text="Добавить", width=17,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window, text="Обновить выбранное", width=17,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window, text="Удалить выбранное", width=17,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window, text="Закрыть", width=17,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()