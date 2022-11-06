# print("\ti*2\ti*3\ti*4\ti*5\ti*6\ti*7\ti*8\ti*9\ti*10\ti*11\ti*12")
# for i in range (1,10):
#     print(i,"\t",i*2,"\t",i*3,"\t",i*4,"\t",i*5,"\t",i*6,"\t",i*7,"\t",i*8,"\t",i*9,"\t",i*10,"\t",i*11,"\t",i*12,sep='')

elrendezes = '{:>3}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}'

print (elrendezes.format("1","2","3","4","5","6","7","8","9","10","11","12"))
for i in range(2,13):
    print(elrendezes.format(i,i*2,i*3,i*4,i*5,i*6,i*7,i*8,i*9,i*10,i*11,i*12))