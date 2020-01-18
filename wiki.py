import wikipedia
wikipedia.set_lang("ru")

search = input("Что найти?\n")
w = wikipedia.page(search)
print(w.content)
