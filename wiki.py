import wikipedia
wikipedia.set_lang("ru")

while True:

    search = input("Что найти?\n")
    if search == "стоп": 
        break
    w = wikipedia.page(search)
    print(w.content)
