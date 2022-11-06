
elrendezes = '{:>3}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}'

print (elrendezes.format("1","2","3","4","5","6","7","8","9","10","11","12"))
for i in range(2,13):
    print(elrendezes.format(i,i*2,i*3,i*4,i*5,i*6,i*7,i*8,i*9,i*10,i*11,i*12))