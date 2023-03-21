def entry_to_dict (log):
    names = ("Host", "Date", "Path", "Code", "Bytes")
    return dict(zip(names,log)) if len(log) == len(names) else "Błąd danych"