#jokhon kon boro file porbo
#target: jate memory crash na hoi

def file_reader(file):
    for line in file:
        yield line

read_notes = file_reader("HI\n I am a programmer")
print(next(read_notes))