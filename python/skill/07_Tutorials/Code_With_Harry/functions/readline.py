data = open('code_with_harry\\functions\\myfile.txt', 'r')

while True:
    line = data.readline()
    if not line:
        break
    print(line)