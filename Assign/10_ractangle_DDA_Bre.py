# . Write a python program to draw a rectangle by using BRESENHAM and DDA
# algorithm.



import matplotlib.pyplot as plt

def draw_rectangle_bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy > dx
    
    if slope:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    error = dx / 2
    ystep = 1 if y1 < y2 else -1
    y = y1
    
    points = []
    
    for x in range(x1, x2 + 1):
        coord = (y, x) if slope else (x, y)
        points.append(coord)
        error -= dy
        if error < 0:
            y += ystep
            error += dx
    
    return points

def draw_rectangle_dda(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steps = max(dx, dy)
    
    x_increment = dx / steps
    y_increment = dy / steps
    
    x = x1
    y = y1
    
    points = []
    
    for _ in range(steps + 1):
        coord = (int(x), int(y))
        points.append(coord)
        x += x_increment
        y += y_increment
    
    return points

# Rectangle coordinates
x1 = 2
y1 = 2
x2 = 8
y2 = 5

# Draw rectangle using Bresenham algorithm
points_bresenham = draw_rectangle_bresenham(x1, y1, x2, y2)

# Draw rectangle using DDA algorithm
points_dda = draw_rectangle_dda(x1, y1, x2, y2)

# Plotting the points
x_coords_bresenham, y_coords_bresenham = zip(*points_bresenham)
x_coords_dda, y_coords_dda = zip(*points_dda)

plt.plot(x_coords_bresenham, y_coords_bresenham, '-r', label='Bresenham')
plt.plot(x_coords_dda, y_coords_dda, '-g', label='DDA')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Rectangle Drawing')

plt.legend()
plt.grid(True)
plt.show()