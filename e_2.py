def get_failed_reads (logs, parameter=False):
    C400 = []
    C500 = []
    for log in logs:
        if str(log[3]).startswith("4"):
            C400.append(log)
        elif str(log[3]).startswith("5"):
            C500.append(log)
    return C400+C500 if parameter else (C400, C500)