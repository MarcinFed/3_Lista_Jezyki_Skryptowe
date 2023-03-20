import re
import datetime

def process_line(line):
    try:
        data = re.match(r"(.+) - - \[(.+) \"(.+)\" (.+) (.+)", line)
        return [data[1], data[2], data[3], data[4], data[5]]
    except:
        raise Exception("Wrong data!")

def get_code(line):
    code = process_line(line)[3]
    if code.isdigit():
        return int(code)
    return 0

def get_bytes(line):
    bytes = process_line(line)[4]
    if bytes.isdigit():
        return int(bytes)
    return 0

def get_request(line):
    request = process_line(line)
    return request[2]

def get_path(line):
    request = get_request(line)
    splited = request.split()
    if len(splited) < 2:
        return request
    return splited[1].strip()

def get_date(line):
    date = process_line(line)[1].split()[0]
    time = datetime.datetime.strptime(date, "%d/%b/%Y:%H:%M:%S")
    return time

def get_host(line):
    host = process_line(line)
    return host[0]

def check_code(code):
    codes = [100,101,110,111,200,201,202,203,204,205,206,300,301,302,303,304,305,306,307,310,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,421,422,423,424,425,426,428,429,431,451,500,501,502,503,504,505,506,507,508,509,510,511]
    return True if code in codes else False