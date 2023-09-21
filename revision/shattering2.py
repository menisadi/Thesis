import matplotlib.pyplot as plt
import numpy as np

# Define the points
points = [(0, 3, "$r_1$"), (0, 5, "$r_2$"), (2, 0, "$x_1$"), (6, 0, "$x_2$")]

# Define the lines
x = np.linspace(-1, 9, 400)
lines = [
    (0.2 * x + 6, "$f_{11}$"),
    (-0.1 * x + 2, "$f_{00}$"),
    (0.05 * x + 3.9, "$f_{01}$"),
    (2 * x - 4, "$f_{10}$"),
]


# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
for x_val, y_val, label in points:
    ax.scatter(x_val, y_val, marker="o", s=100)
    ax.text(x_val + 0.1, y_val + 0.1, label, fontsize=12)
for line, label in lines:
    ax.plot(x, line, label=label)
    # Add labels for the lines

# Add labels manually
ax.text(8, lines[0][0][390] - 0.7, lines[0][1], fontsize=12)
ax.text(8, lines[1][0][390] - 0.3, lines[1][1], fontsize=12)
ax.text(8, lines[2][0][350] - 0.3, lines[2][1], fontsize=12)
ax.text(6, lines[3][0][300] - 0.3, lines[3][1], fontsize=12)

ax.axhline(y=3, linestyle="--", color="gray")
ax.axhline(y=5, linestyle="--", color="gray")
ax.axvline(x=2, linestyle="--", color="gray")
ax.axvline(x=6, linestyle="--", color="gray")

# Make the x and y axes visible
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")

# Add labels and title
# plt.title("Fat-Shattering 2 points with the affine functions class")
plt.xlim(-1, 9)
plt.ylim(-1, 9)

# Show the plot
# plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
# plt.savefig("shattering.pdf")
