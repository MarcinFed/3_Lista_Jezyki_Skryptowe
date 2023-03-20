from Tools import get_host, get_date, get_path, get_code, get_bytes, check_code

def read_log (lines):
    my_list=[]
    for line in lines:
        my_list.append((get_host(line),get_date(line), get_path(line), get_code(line), get_bytes(line)))
    return my_list

def sort_log (logs, parameter):
    try:
        sorted_log = sorted(logs, key=lambda x: x[parameter])
        return sorted_log
    except IndexError:
        return "Podana liczba przekracza rozmiar krotki"

def get_entries_by_addr (logs, parameter):
    entries = []
    for entrie in logs:
        if entrie[0] == parameter:
            entries.append(entrie)
    return entries

def get_entries_by_code (logs, parameter):
    if check_code(parameter):
        entries = []
        for entrie in logs:
            if entrie[3] == parameter:
                entries.append(entrie)
        return entries
    else:
        return "Błędny kod statusu"

def get_failed_reads (logs, parameter=0):
    C400 = []
    C500 = []
    for log in logs:
        if str(log[3]).startswith("4"):
            C400.append(log)
        elif str(log[3]).startswith("5"):
            C500.append(log)
    return (C400, C500) if parameter == 0 else C400+C500

def get_entires_by_extension (logs, parameter):
    entries = []
    for entrie in logs:
        if entrie[2].endswith(parameter):
            entries.append(entrie)
    return entries

def print_entries (logs):
    for log in logs:
        print(log)

def entry_to_dict (log):
    names = ("Host", "Date", "Path", "Code", "Bytes")
    return dict(zip(names,log)) if len(log) == len(names) else "Błąd danych"

def log_to_dict(logs):
    dictionary = {}
    for log in logs:
        host_name = log[0]
        if host_name not in dictionary:
            dictionary[host_name] = []
        dictionary[host_name].append(entry_to_dict(log))
    return dictionary

def get_addrs (dictionary):
    keys = []
    for key in dictionary:
        keys.append(key)
    return keys

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




def main():
    lines = open("test.txt", mode="r", encoding="utf-8")
    my_list = read_log(lines)
    #print(sort_log(my_list,0))
    #print(get_entries_by_addr(my_list, "199.72.81.55"))
    #print(get_entries_by_code(my_list, 200))
    #print(get_failed_reads(my_list,1))
    #print_entries(get_entires_by_extension(my_list, "jpg"))
    #print(entry_to_dict(my_list[0]))
    #print(log_to_dict(my_list))
    #print(get_addrs(log_to_dict(my_list)))
    print_dict_entry_dates(log_to_dict(my_list))

if __name__ == "__main__":
    main()