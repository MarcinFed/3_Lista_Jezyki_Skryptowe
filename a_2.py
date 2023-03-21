from Tools import get_host, get_date, get_path, get_code, get_bytes
def read_log (lines):
    my_list=[]
    for line in lines:
        my_list.append((get_host(line),get_date(line), get_path(line), get_code(line), get_bytes(line)))
    return my_list