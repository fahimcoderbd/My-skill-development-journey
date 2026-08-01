#real life example 2
#division

def divide(n1,n2):
    try:
        if n1 > n2: 
            output = n1 / n2
        return output
    except ZeroDivisionError:
        print("bro thik thak daw!")

divide(5,0)