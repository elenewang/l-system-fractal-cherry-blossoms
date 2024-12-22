
# Fractal Flora

The goal of this project is to create a visually appealing simulation of a fractal plant using L-systems. The simulation includes features such as wind animation and flower generation to enhance realism. The project is divided into multiple versions, each adding new features and improvements.


## Stages of Development

1. **Stage 0: Basic L-System Plant**
   - **Design Decisions:**
     - Created `LSystem` class with methods for generating L-system strings.
     - Created `TurtleDrawer` class for drawing the plant structures.  
     - Used Turtle graphics for rendering.
   - **Level of Achievement:**
     - Successfully generated and displayed a static fractal plant.

2. **Stage 1: Enhanced L-System with Flowers**
   - **Design Decisions:**
     - Added flower generation to the L-system rules.
     - Updated `draw_l_system` method to interpret new symbols for flowers.
   - **Level of Achievement:**
     - Successfully integrated flower drawing into the plant structure.

3. **Stage 2: Animated Wind Effect**
   - **Design Decisions:**
     - Introduced wind animation using threading.
     - Created `WindAnimator` class for managing wind effects.
     - Added `animate_wind` method for dynamic wind simulation.
     - Used Screen.tracer() to improve animation performance.  
     - added stop_animation() method to stop the animation with the 'r' key gracefully.  
   - **Level of Achievement:**
     - Achieved a dynamic and animated fractal plant with wind effects.

### Project Structure
```
Fractal_Flora/
│
├── README.md
│
└── fractal_flora_project/
    ├── v0/
    │   ├── l_system.py
    │   ├── main.py
    │   └── turtle_drawer.py
    ├── v1/
    │   ├── l_system.py
    │   ├── main.py
    │   └── turtle_drawer.py
    └── v2/
        ├── l_system.py
        ├── main.py
        ├── turtle_drawer.py
        └── wind_animator.py
```
### Design Decisions

- **Classes and important Functions:**
  - `LSystem`: Core class handling L-system generation.
  - `TurtleDrawer`: Handles drawing branches and flowers using Turtle graphics.
  - `WindAnimator`: Manages wind animation effects.
  - `draw_l_system`: Draws branches with optional wind effects.
  - `draw_flower`: Draws flowers at specified positions.
  - `animate_wind`: Continuously updates wind parameters for animation.

- **Data Structures:**
  - Used lists to manage stack operations for turtle graphics.
  - Utilized threading for concurrent wind animation.
  - Used Dictionary to store the L-system rules for generating the fractal plant. 
    

## Instructions for Use

1. **Running the Program:**
   - Ensure Python and Turtle graphics are installed.
   - Run the main script in the desired version directory (e.g., `fractal_flora/v2/main.py`).

2. **Interacting with the Simulation:**
   - Press command + `r` to stop the animation in version 2.

