from a_2 import read_log
from b_2 import sort_log
from c_2 import get_entries_by_addr
from d_2 import get_entries_by_code
from e_2 import get_failed_reads
from f_2 import get_entires_by_extension
from g_2 import print_entries
from a_3 import entry_to_dict
from b_3 import log_to_dict
from c_3 import get_addrs
from d_3 import print_dict_entry_dates

def main():
    lines = open("test.txt", mode="r", encoding="utf-8")
    my_list = read_log(lines)
    #print(sort_log(my_list,0))
    #print(get_entries_by_addr(my_list, "199.72.81.55"))
    #print(get_entries_by_code(my_list, 200))
    #print(get_failed_reads(my_list,1))
    #print_entries(get_entires_by_extension(my_list, "jpg"))
    #print(entry_to_dict(my_list[0]))
    #print(log_to_dict(my_list))
    #print(get_addrs(log_to_dict(my_list)))
    print_dict_entry_dates(log_to_dict(my_list))

if __name__ == "__main__":
    main()