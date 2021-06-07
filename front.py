from tkinter import *
from tkinter import messagebox
import back

window = Tk()
window.geometry("600x550")
window.resizable(width=FALSE, height=FALSE)
selected = ''


def clear():
    lst_1.delete(0, END)


def iterate_list(data):
    for item in data:
        lst_1.insert(END, item)


def view_data():
    clear()
    users = back.view()
    iterate_list(users)


def search_user():
    clear()
    users = back.search(entry_1.get(), entry_2.get(), entry_3.get(),
                        entry_4.get(), entry_5.get(), entry_6.get())
    iterate_list(users)


def register():
    test = back.create(entry_1.get(), entry_2.get(), entry_3.get(),
                       entry_4.get(), entry_5.get(), entry_6.get())
    view_data()
    if test == 404:
        messagebox.showerror("Error", "Cant register again")


def get_selected_row(event):
    global selected
    if len(lst_1.curselection()) > 0:
        index = lst_1.curselection()[0]
        selected = lst_1.get(index)

        entry_1.delete(0, END)
        entry_1.insert(END, selected[1])

        entry_2.delete(0, END)
        entry_2.insert(END, selected[2])

        entry_3.delete(0, END)
        entry_3.insert(END, selected[3])

        entry_4.delete(0, END)
        entry_4.insert(END, selected[4])

        entry_5.delete(0, END)
        entry_5.insert(END, selected[5])

        entry_6.delete(0, END)
        entry_6.insert(END, selected[6])


def delete_user():
    global selected
    back.delete(selected[0])
    view_data()


def update_user():
    back.update(selected[0], entry_1.get(), entry_2.get(), entry_3.get(),
                entry_4.get(), entry_5.get(), entry_6.get())
    view_data()


def exit_app():
    window.destroy()


# ============================== Labels  =======================================
label_1 = Label(window, text="Name")
label_1.grid(row=0, column=0)

label_2 = Label(window, text="Last Name")
label_2.grid(row=0, column=6)

label_3 = Label(window, text="Code")
label_3.grid(row=2, column=0)

label_4 = Label(window, text="Address")
label_4.grid(row=4, column=0)

label_5 = Label(window, text="Phone Number")
label_5.grid(row=6, column=0)

label_6 = Label(window, text="Birth day")
label_6.grid(row=6, column=6)

# ============================== Entries =======================================
entry_1 = Entry(window, bg='skyblue')
entry_1.grid(row=1, column=0, padx=5, ipady=3)

entry_2 = Entry(window, bg='skyblue')
entry_2.grid(row=1, column=6, ipady=3)

entry_3 = Entry(window, width=45, bg='skyblue')
entry_3.grid(row=3, column=0, columnspan=7, ipady=3)

entry_4 = Entry(window, width=45, bg='skyblue')
entry_4.grid(row=5, column=0, columnspan=7, ipady=3)

entry_5 = Entry(window, bg='skyblue')
entry_5.grid(row=7, column=0, ipady=3)

entry_6 = Entry(window, bg='skyblue')
entry_6.grid(row=7, column=6, ipady=3)

# ============================== Buttons =======================================
button_1 = Button(window, text='Register', width=20, command=register)
button_1.grid(row=0, column=7, padx=30, pady=5)

button_2 = Button(window, text='View', width=20, command=view_data)
button_2.grid(row=1, column=7, pady=5)

button_3 = Button(window, text='Edit', width=20, command=update_user)
button_3.grid(row=2, column=7, pady=5)

button_4 = Button(window, text='Search', width=20, command=search_user)
button_4.grid(row=3, column=7, pady=5)

button_5 = Button(window, text='Delete', width=20, command=delete_user)
button_5.grid(row=4, column=7, pady=5)

button_6 = Button(window, text='Exit', width=20, command=exit_app)
button_6.grid(row=7, column=7, pady=5)

# ============================== List    =======================================

lst_1 = Listbox(window, width=65, height=13)
lst_1.grid(row=8, column=0, columnspan=8)
lst_1.bind("<<ListboxSelect>>", get_selected_row)

# ============================== Scroll  =======================================
scr1 = Scrollbar(window)
scr1.place(x=575, y=400)

# ============================== Configuration =================================
scr1.configure(command=lst_1.yview)
lst_1.configure(yscrollcommand=scr1.set)

# ==============================================================================


window.mainloop()
