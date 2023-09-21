import matplotlib.pyplot as plt
import numpy as np

# Define the points
points = [(0, 3, "$r_1$"), (0, 5, "$r_2$"), (2, 0, "$x_1$"), (6, 0, "$x_2$")]

# Define the lines
x = np.linspace(-1, 15, 400)
lines = [
    (0.2 * x + 6, "$f_{11}$"),
    (-0.1 * x + 2, "f_{00}$"),
    (0.05 * x + 3.9, "f_{01}$"),
    (2 * x - 4, "$f_{10}$"),
]

# Create the plot
plt.figure(figsize=(10, 6))
for x_val, y_val, label in points:
    plt.scatter(x_val, y_val, marker="o", s=100)
    plt.text(x_val + 0.1, y_val + 0.1, label, fontsize=12)
for line, label in lines:
    plt.plot(x, line, label=label)
    # Add labels for the lines
    plt.text(
        4, line[300] - 3, label, fontsize=12
    )  # Adjust the position for your preference

plt.axhline(y=3, linestyle="--", color="gray")
plt.axhline(y=5, linestyle="--", color="gray")
plt.axvline(x=2, linestyle="--", color="gray")
plt.axvline(x=6, linestyle="--", color="gray")

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Fat-Shattering 2 points with the affine functions class")

# Show the plot
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
