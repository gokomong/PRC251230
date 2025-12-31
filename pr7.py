import tkinter as tk

root =tk.Tk()
# root.title("제목")
# root.geometry("800x600")
# label =tk.Label(root, text="안녕하세요")
# label.pack()
# label.grid()
# root.mainloop()

title_entry = tk.Entry(root, width=30 ,font=("Arila",10))
title_entry.pack()
text = title_entry.get()
title_entry.insert(0, "기본값")
title_entry.delete(0, tk.END)