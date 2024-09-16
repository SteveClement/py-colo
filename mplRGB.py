import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, 800)
ax.set_ylim(0, 500)
ax.set_aspect('equal', adjustable='box')
ax.axis('off')

# Define colors with alpha channels
RED = (1, 0, 0, 0.4)
GREEN = (0, 1, 0, 0.4)
BLUE = (0, 0, 1, 0.4)

# Add circles
circle1 = patches.Circle((430, 280), 60, color=BLUE)
circle2 = patches.Circle((370, 280), 60, color=GREEN)
circle3 = patches.Circle((400, 220), 60, color=RED)

ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)

# Display the plot
plt.show()
