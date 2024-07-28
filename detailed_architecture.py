import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(16, 12))

# Set the limits and title
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_title("stayComitted MVP Architecture", fontsize=16)

# Function to draw rectangles
def draw_rectangle(ax, x, y, width, height, text):
    rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='black', facecolor='lightgrey')
    ax.add_patch(rect)
    ax.text(x + width / 2, y + height / 2, text, ha='center', va='center', fontsize=10, fontweight='bold')

# Draw rectangles for components
components = {
    "User": (5, 85, 15, 10),
    "React Frontend": (40, 85, 20, 10),
    "FastAPI Backend": (75, 85, 20, 10),
    "Registration/Login (Form)": (5, 65, 15, 10),
    "/register, /login": (40, 65, 20, 10),
    "API Endpoints": (75, 65, 20, 10),
    "Dashboard": (5, 50, 15, 10),
    "Goals Input (Form)": (5, 35, 15, 10),
    "/goals": (40, 35, 20, 10),
    "Recommendations Display": (5, 20, 15, 10),
    "/recommendations": (40, 20, 20, 10),
    "Advice Display": (5, 5, 15, 10),
    "/advice": (40, 5, 20, 10),
    "Database": (75, 50, 20, 10),
    "CRUD Operations": (75, 35, 20, 10),
    "ML Models": (75, 20, 20, 10),
    "External APIs (LLM)": (75, 5, 20, 10),
}

for name, (x, y, w, h) in components.items():
    draw_rectangle(ax, x, y, w, h, name)

# Draw arrows for interactions
arrows = [
    ("User", "React Frontend"),
    ("React Frontend", "/register, /login"),
    ("/register, /login", "API Endpoints"),
    ("Dashboard", "API Endpoints"),
    ("Goals Input (Form)", "/goals"),
    ("/goals", "API Endpoints"),
    ("Recommendations Display", "/recommendations"),
    ("/recommendations", "API Endpoints"),
    ("Advice Display", "/advice"),
    ("/advice", "API Endpoints"),
    ("Database", "CRUD Operations"),
    ("ML Models", "CRUD Operations"),
    ("External APIs (LLM)", "ML Models"),
]

positions = {
    "User": (15, 90),
    "React Frontend": (50, 90),
    "FastAPI Backend": (85, 90),
    "Registration/Login (Form)": (15, 70),
    "/register, /login": (50, 70),
    "API Endpoints": (85, 70),
    "Dashboard": (15, 55),
    "Goals Input (Form)": (15, 40),
    "/goals": (50, 40),
    "Recommendations Display": (15, 25),
    "/recommendations": (50, 25),
    "Advice Display": (15, 10),
    "/advice": (50, 10),
    "Database": (85, 55),
    "CRUD Operations": (85, 40),
    "ML Models": (85, 25),
    "External APIs (LLM)": (85, 10),
}

for start, end in arrows:
    ax.annotate("", xy=positions[end], xytext=positions[start],
                arrowprops=dict(arrowstyle="->", lw=1.5), bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="none"))

# Add descriptions for arrows
descriptions = {
    ("User", "React Frontend"): "Interact",
    ("React Frontend", "/register, /login"): "POST",
    ("/register, /login", "API Endpoints"): "/register, /login",
    ("Dashboard", "API Endpoints"): "API Requests",
    ("Goals Input (Form)", "/goals"): "POST",
    ("/goals", "API Endpoints"): "/goals",
    ("Recommendations Display", "/recommendations"): "API Requests",
    ("/recommendations", "API Endpoints"): "/recommendations",
    ("Advice Display", "/advice"): "GET",
    ("/advice", "API Endpoints"): "/advice",
    ("Database", "CRUD Operations"): "CRUD Operations",
    ("ML Models", "CRUD Operations"): "API Requests",
    ("External APIs (LLM)", "ML Models"): "API Requests",
}

for (start, end), desc in descriptions.items():
    pos = ((positions[start][0] + positions[end][0]) / 2, (positions[start][1] + positions[end][1]) / 2)
    ax.text(*pos, desc, ha='center', va='center', fontsize=8, rotation=0, bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"))

# Hide axes
ax.axis('off')

# Save and show the diagram
# plt.savefig("/mnt/data/stayComitted_MVP_Simplified_Architecture.png")
plt.show()
