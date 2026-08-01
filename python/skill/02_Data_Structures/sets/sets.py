"""
🔷 SETS IN PYTHON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Unique + Fast = Set
⚡ O(1) fast searching
"""

# ✨ SET CREATION
print("📌 Creating a Set:")
numbers = {1, 2, 3, 4, 4, 5}
print(f"   {numbers}\n")

# 🔧 SET METHODS
print("📌 Adding Elements:")
numbers.add(6)
print(f"   After add(6): {numbers}\n")

print("📌 Removing Elements:")
numbers.remove(1)
print(f"   After remove(1): {numbers}\n")

# 🔗 UNION AND INTERSECTION
print("📌 Set Operations:")
a = {1, 2, 3}
b = {3, 4, 5}

print(f"   Set A: {a}")
print(f"   Set B: {b}\n")

# 🔀 UNION (All elements)
print(f"   🔀 Union (A | B): {a | b}")

# 🎯 INTERSECTION (Common elements)
print(f"   🎯 Intersection (A & B): {a & b}")