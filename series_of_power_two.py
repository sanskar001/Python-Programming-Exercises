# This is pyhton program to print 1, 2, 4, 8, 16, 32,......
series_list=[]
def series(number):
    for x in range(number):
        series_list.append(str(2**x))
    print(" ".join(series_list))
series(64)    
