'''
5. Divide Calculator ➗ (Easy)
Scenario

Calculator divide করবে।

Input

Number1
Number2

যদি

number2 == 0
raise ZeroDivisionError

except ZeroDivisionError

Cannot divide by zero

Otherwise

Result print করো।
'''

#sollution
def divide_calc(num1, num2):
    try:
        if num2 == 0:
            raise ZeroDivisionError
        result = num1 / num2
        return result
        
    except ZeroDivisionError:
        return "Can't devide by zero!"

print(divide_calc(1,0))
print(divide_calc(1,2))