def get_entires_by_extension (logs, parameter):
    entries = []
    for entrie in logs:
        if entrie[2].endswith(parameter):
            entries.append(entrie)
    return entries