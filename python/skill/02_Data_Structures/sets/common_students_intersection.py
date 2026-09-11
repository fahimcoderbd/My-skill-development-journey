#2.problem
class_A = {"fahim", "rahim", "karim", "sadia"}
class_B = {"rahim", "sadia", "arif", "tanvir"}
class_C = {"sadia", "rahim", "rakib"}

'''steps to solve
task1 =>
1.i have to find the common with intersection
'''

common = class_A.intersection(class_B).intersection(class_C)
print(f"these students: {common} are in all three classes")

'''task2 =>
union of all three classes
'''

main_set = class_A.union(class_B).union(class_C)
print(f"these students: {main_set} are in at least one class")