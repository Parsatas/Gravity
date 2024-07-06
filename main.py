from customtkinter import *
from CTkMessagebox import CTkMessagebox

root = CTk()
root.geometry("250x240")
font = CTkFont("Vazir", size=16)
root.resizable(False, False)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)

frame_ = CTkFrame(root)
frame_.grid(column=0, row=0, sticky=NSEW, pady=20, padx=20)

frame_.grid_columnconfigure(0, weight=1)
frame_.grid_columnconfigure(1, weight=0)
frame_.grid_rowconfigure(0, weight=1)
frame_.grid_rowconfigure(1, weight=1)

l_m = CTkLabel(frame_, text="kg", font=font)
l_m.grid(column=1, row=0, pady=(10, 0), padx=(5, 15))
e_m = CTkEntry(frame_, placeholder_text="وزن", font=font, justify=RIGHT)
e_m.grid(column=0, row=0, pady=(10, 0), padx=(10, 0))
l_m = CTkLabel(frame_, text="m", font=font)
l_m.grid(column=1, row=1, pady=(0, 10), padx=(5, 15))
e_r = CTkEntry(frame_, placeholder_text="شعاع", font=font, justify=RIGHT)
e_r.grid(column=0, row=1, pady=(0, 10), padx=(10, 0))


def math_():
    try:
        x = (float(e_m.get()) * (6.67408 / (10 ** 11))) / (float(e_r.get()) ** 2)
        CTkMessagebox(message=f"{x} N", icon="check", title="Finish", font=font)
    except ValueError:
        CTkMessagebox(message="مقادیر وارد شده نادرست است", icon="cancel", title="Error", font=font)


btn = CTkButton(root, text="محاسبه", font=font, command=math_)
btn.grid(column=0, row=1, pady=10, padx=10)

root.mainloop()
