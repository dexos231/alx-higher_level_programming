#!/usr/bin/python3
def safe_print_list_integers(my_list[], x=0):
    m = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]))
            m += 1
        except(ValueError,IndexError,TypeError):
            pass
    print("")
    return(m)
