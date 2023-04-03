from Tools import check_code

def get_entries_by_code (logs, parameter):
    if check_code(parameter):
        entries = []
        for entrie in logs:
            if entrie[3] == parameter:
                entries.append(entrie)
        return entries
    else:
        raise Exception("Błędny kod statusu")