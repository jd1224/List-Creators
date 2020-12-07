
for i in range(2020,2021):
    dateout= ''
    year=str(i)
    for j in range(1,13):
        month = str(f'{j:02}')
        for k in range(1,32):
            day = str(f'{k:02}')
            print(f'{year}{month}{day}')
