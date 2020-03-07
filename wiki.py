import wikipedia
wikipedia.set_lang("ru")

while True:
    try:
        search = input("Что найти?\n")
        if search == "стоп": 
            break
        w = wikipedia.page(search)
        print(w.content)
    except:
        print("Не удалось найти")
        valid_variants = wikipedia.search(search)
        print("Доступные варианты:")
        for variants in valid_variants:
            print(variants)
     