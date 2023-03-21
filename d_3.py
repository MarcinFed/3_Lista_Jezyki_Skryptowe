def print_dict_entry_dates (dictionary):
    for key in dictionary:
        print(f"Nazwa/IP hosta: {key}")
        count_200 = 0
        count_all = 0
        dates = []
        for value in dictionary.get(key):
            dates.append(value.get("Date"))
            count_all+=1
            if value.get("Code") == 200:
                count_200+=1
        sorted(dates)
        print(f"\tLiczba żądań: {count_all}")
        print(f"\tStosunek żądań z kodem 200 do wszystkich: {count_200/count_all:.2f}")
        print(f"\tData pierwszego żądania: {dates[0]}")
        print(f"\tData ostatniego żądania: {dates[-1]}\n")