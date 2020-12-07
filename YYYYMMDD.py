import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', help='Start Year',
                    type=int, required=True)
parser.add_argument('-e', help='End Year',
                    type=int, required=True)

args = parser.parse_args()
for i in range(args.s, args.e+1):
    dateout= ''
    year=str(i)
    for j in range(1,13):
        month = str(f'{j:02}')
        if j in [1,3,5,7,8,10,12]:
            for k in range(1,32):
                day = str(f'{k:02}')
                print(f'{year}{month}{day}')
        elif j == 2:
            if i % 4 == 0 and i % 100 != 0:
                for k in range(1,30):
                    day = str(f'{k:02}')
                    print(f'{year}{month}{day}')
            elif i % 400 == 0:
                for k in range(1,30):
                    day = str(f'{k:02}')
                    print(f'{year}{month}{day}')
            else:
                for k in range(1,29):
                    day = str(f'{k:02}')
                    print(f'{year}{month}{day}')
        else:
            for k in range(1,31):
                day = str(f'{k:02}')
                print(f'{year}{month}{day}')