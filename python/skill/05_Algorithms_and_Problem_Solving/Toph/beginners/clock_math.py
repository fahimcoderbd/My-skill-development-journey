H,M = map(int, input().split())

angle = abs(30 * H - 5.5 * M)

if angle > 180:
    angle = 360 - angle

print(f"{angle:.7f}")