
x=int(input("enter a number for row size: "))
row_size=x
col_size=x

# row_count=1
# while row_count <= row_size:
#     col_count=col_size
#     while col_count<=col_size and col_count>=0:
#         print(col_count," ",end="")
#         col_count=col_count-1
#     print("")
#     row_count=row_count+1

row_count=1
while row_count <= row_size:
    col_count=col_size
    while col_count<=col_size and col_count>=0:
        if col_count%2 ==0:
            print("__","",end="")
        else:
            print("$$","",end="")
        col_count=col_count-1
    print("")
    row_count=row_count+1

