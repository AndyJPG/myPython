import os

try:
    f = open('demofile.txt', 'r')
    # print(f.read())
    print(f.readline())

except FileNotFoundError:
    print('File not found')
finally:
    f.close()


if os.path.exists('demofile.txt'):
    print('file exist')
else:
    print('file does not exist')

