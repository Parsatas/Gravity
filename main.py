from customtkinter import *
from CTkMessagebox import CTkMessagebox

root = CTk()
root.geometry("340x150")
font = CTkFont("Vazir", size=16)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

e_m = CTkEntry(root, placeholder_text="وزن", font=font, justify=RIGHT)
e_m.grid(column=0, row=0, pady=(0, 60))
e_r = CTkEntry(root, placeholder_text="شعاع", font=font, justify=RIGHT)
e_r.grid(column=0, row=0, pady=(60, 0))


def math_():
    try:
        x = (float(e_m.get()) * (6.67408/(10**11)))/(float(e_r.get())**2)
        CTkMessagebox(message=f"{x} N", icon="check", title="Finish", font=font)
    except ValueError:
        CTkMessagebox(message="مقادیر وارد شده نادرست است", icon="cancel", title="Error", font=font)


btn = CTkButton(root, text="محاسبه", font=font, command=math_)
btn.grid(column=1, row=0)

root.mainloop()
