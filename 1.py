def x(size, diff, itration):
    blue_print = ""

    for i in range(size, size + diff, itration):

        if i != size+diff-1:
            blue_print += chr(i + 96) + "-"
        else:
            blue_print += chr(i + 96)

    return blue_print



def meow(size):

    for k in range(1, size+1):
        print(        '-'*(  len( x(size, -size, -1) ) - len( x(size, -k, -1) )  )     +     x(size, -k, -1)         , end = '')
        print(        x(size-k+2, k-1, 1)     +     '-'*(  len( x(2, size-1, 1) ) - len( x(size-k+2, k-1, 1) )  )         )


    for k in range(size-1, 0, -1):
        print(        '-'*(  len( x(size, -size, -1) ) - len( x(size, -k, -1) )  )     +     x(size, -k, -1)         , end = '')
        print(        x(size-k+2, k-1, 1)     +     '-'*(  len( x(2, size-1, 1) ) - len( x(size-k+2, k-1, 1) )  )         )
      

              



size = int(input("Number: "))
meow(size)
