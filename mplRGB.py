import numpy as np
import matplotlib.pyplot as plt

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, 800)
ax.set_ylim(0, 500)
ax.set_aspect('equal', adjustable='box')
ax.axis('off')

# Create an image array (height x width x RGB)
width, height = 800, 500
image = np.zeros((height, width, 3), dtype=float)

# Create a grid of x and y coordinates
y_indices, x_indices = np.indices((height, width))

# Define circles with their positions and colors
circles = [
    {'center': (430, 220), 'radius': 60, 'color': np.array([0, 0, 1])},  # Blue
    {'center': (370, 220), 'radius': 60, 'color': np.array([0, 1, 0])},  # Green
    {'center': (400, 280), 'radius': 60, 'color': np.array([1, 0, 0])},  # Red
]

# Draw each circle onto the image array
for circle in circles:
    cx, cy = circle['center']
    r = circle['radius']
    color = circle['color']
    # Calculate the distance of each point from the circle's center
    distance = np.sqrt((x_indices - cx)**2 + (y_indices - cy)**2)
    # Create a mask for the circle
    mask = distance <= r
    # Add the circle's color to the image where the mask is True
    image[mask] += color

# Clip the image values to ensure RGB values are between 0 and 1
image = np.clip(image, 0, 1)

# Display the image with correct orientation and extent
ax.imshow(image, origin='upper', extent=(0, width, height, 0))

# Show the plot
plt.show()
