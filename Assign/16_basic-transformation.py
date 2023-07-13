# Write a python program to implement basic transformations (translation, rotation,
# scaling on a rectangle



import pygame
import math

# Rectangle class
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self, angle):
        cx = self.x + self.width / 2
        cy = self.y + self.height / 2
        radians = math.radians(angle)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        dx = self.x - cx
        dy = self.y - cy
        rotated_dx = dx * cos_angle - dy * sin_angle
        rotated_dy = dx * sin_angle + dy * cos_angle
        self.x = cx + rotated_dx
        self.y = cy + rotated_dy

    def scale(self, scale_factor):
        self.width *= scale_factor
        self.height *= scale_factor


# Initialize Pygame
pygame.init()

# Window dimensions
width, height = 800, 600

# Create the Pygame window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rectangle Transformations')

# Create a rectangle
rectangle = Rectangle(100, 100, 200, 100)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the rectangle
    rectangle.draw(screen)

    # Apply transformations
    rectangle.translate(2, 2)  # Translation
    rectangle.rotate(1)  # Rotation (in degrees)
    rectangle.scale(1.01)  # Scaling

    # Update the display
    pygame.display.flip()

# Quit the program
pygame.quit()