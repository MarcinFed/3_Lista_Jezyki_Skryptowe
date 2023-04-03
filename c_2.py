def get_entries_by_addr (logs, parameter):
    try:
        entries = []
        for entrie in logs:
            if entrie[0] == parameter:
                entries.append(entrie)
        return entries
    except TypeError:
        raise Exception("Błąd typu")