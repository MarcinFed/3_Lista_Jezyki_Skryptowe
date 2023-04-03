def sort_log (logs, parameter):
    try:
        sorted_log = sorted(logs, key=lambda x: x[parameter])
        return sorted_log
    except IndexError:
        raise Exception("Podana liczba przekracza rozmiar krotki")

