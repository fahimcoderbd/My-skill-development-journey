def split_generator(sentence):
    for word in sentence.split():
        yield word

text = split_generator("I love python")
print(next(text))
print(next(text))