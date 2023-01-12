from tkinter import *
import requests


def get_quote():
    get_today_quote = requests.get("https://api.quotable.io/random?maxLength=130")
    get_today_quote.raise_for_status()
    todays_quote = get_today_quote.json()
    canvas.itemconfig(quote_text, text=todays_quote['content'])


window = Tk()
window.title("Quote of the day")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Press the button 👇 to get a quote...", width=250,
                                font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

refresh_img = PhotoImage(file="refresh.png")
refresh_button = Button(image=refresh_img, highlightthickness=0, borderwidth=1, command=get_quote)
refresh_button.grid(row=1, column=0)


window.mainloop()
