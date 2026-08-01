#copying an arr
from copy import deepcopy

my_skills = ["python", "web-development", "AI usage", "Javascript"]

my_skills_copy = deepcopy(my_skills)
my_skills_copy.append("CSS")

print(my_skills)
print(my_skills_copy)

