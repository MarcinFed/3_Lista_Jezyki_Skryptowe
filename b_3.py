from a_3 import entry_to_dict
def log_to_dict(logs):
    dictionary = {}
    for log in logs:
        host_name = log[0]
        if host_name not in dictionary:
            dictionary[host_name] = []
        dictionary[host_name].append(entry_to_dict(log))
    return dictionary