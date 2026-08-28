#Delivery system package analyzer

def handle_packages(weights:list):
    if not weights: return

    normal_weights = 0
    medium_weights = 0
    heavy_weights = 0

    for weight in weights:
        if weight <= 0: continue #edge case handling
        if weight <= 5: normal_weights += 1
        elif 5 < weight <= 10: medium_weights += 1
        else: heavy_weights += 1

    return (
        f"Normal packages: {normal_weights} \n"
        f"Medium packages: {medium_weights} \n"
        f"Heavy packages: {heavy_weights}"
    )

print(handle_packages([2.5, 7.2, 1.8, 12.5, 4.3, 9.1]))
print(handle_packages([]))
print(handle_packages([0,0,-1,2,5,6,10.1]))
