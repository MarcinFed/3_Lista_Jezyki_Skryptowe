def entry_to_dict (log):
    names = ("Host", "Date", "Path", "Code", "Bytes")
    return dict(zip(names,log))