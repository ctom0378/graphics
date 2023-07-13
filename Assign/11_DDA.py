#  Write a python program to translate a line by using the DDA algorithm.



import matplotlib.pyplot as plt

def dda_translate(x1, y1, x2, y2, dx, dy):
    """
    Translates a line defined by two points (x1, y1) and (x2, y2)
    using the DDA algorithm and the translation distances dx and dy.
    """
    # Calculate the difference between the x-coordinates and y-coordinates
    dx_line = x2 - x1
    dy_line = y2 - y1

    # Calculate the number of steps required for translation
    steps = max(abs(dx_line), abs(dy_line))

    # Calculate the increment values for each step
    x_increment = dx_line / steps
    y_increment = dy_line / steps

    # Initialize the translated line coordinates
    translated_x1 = x1 + dx
    translated_y1 = y1 + dy
    translated_x2 = x2 + dx
    translated_y2 = y2 + dy

    # Store the translated line coordinates
    translated_coordinates = []

    # Perform the translation using the DDA algorithm
    for _ in range(int(steps)):
        translated_coordinates.append((translated_x1, translated_y1))
        translated_x1 += x_increment
        translated_y1 += y_increment

    return translated_coordinates

# Define the original line coordinates
x1 = 1
y1 = 1
x2 = 8
y2 = 5

# Define the translation distances
dx = 3
dy = 2

# Perform the translation
translated_line = dda_translate(x1, y1, x2, y2, dx, dy)

# Plotting the original line and translated line
plt.plot([x1, x2], [y1, y2], 'b-', label='Original Line')
plt.plot([coord[0] for coord in translated_line], [coord[1] for coord in translated_line], 'r-', label='Translated Line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('DDA Line Translation')
plt.grid(True)
plt.show()