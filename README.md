# Append-to-csv-file-except-duplicate-values
Append values of a file to another file except duplicate values.

#file1.csv has values:

1,apple,red  
2,banana,yellow  
3,melon,green  

file2.csv has values:

1,apple,red  
3,melon,green  
4,grape,purple  

when append values of file2 to file1, the program will detect duplicate values (1 and 3) and ignore it. Then it only appends the new value (4)
