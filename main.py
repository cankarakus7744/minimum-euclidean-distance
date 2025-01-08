import math

def euclideanDistance(point_A,point_B):
    x1, y1 = point_A
    x2, y2 = point_B
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

points = [(0,1),(1,5),(4,7),(-1,-4)]
distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append( euclideanDistance(points[i], points[j]) )
        
print(f"Minimum Öklid mesafesi: {min(distances)}")