# PhysicsSim

PhysicsSim is a Python-based simulation project for visualizing and interacting with physics environments, focusing on projectile motion. The project uses Pygame for rendering and user interaction, and is organized for extensibility and clarity.

## Features
- Interactive projectile motion simulation
- Modular codebase with clear separation of environments, assets, interfaces, and examples
- Customizable parameters via UI elements (buttons, input boxes)
- Visual feedback for simulation state and user actions

## Project Structure
```
main.py                        # Entry point for the simulation
Assets/                        # UI components, constants, images, and input handling
    Button.py                  # Button class for UI
    constants.py               # Simulation and UI constants
    imagePaths.py              # Paths to image assets
    Input.py                   # Handles user input
    InputBox.py                # Text input box for UI
    Images/                    # Image assets (background, cannon, projectile, floor)
Environments/                  # Physics environments and objects
    Projectile/                # Projectile motion environment and related classes
        Cannon.py
        Controller.py
        Environment.py
        Floor.py
        Projectile.py
Examples/                      # Example scripts for usage and testing
    projectileMotionExample.py
    textBoxExample.py
Interfaces/                    # Interface definitions for main simulation objects
    CannonInterface.py
    ControllerInterface.py
    EnvironmentInterface.py
    FloorInterface.py
    ProjectileInterface.py
Simulations/                   # Simulation drivers
    projectileDriver.py        # Main driver for projectile simulation
```

## Getting Started
### Prerequisites
- Python 3.9+
- [Pygame](https://www.pygame.org/)

### Installation
1. Clone the repository:
   ```powershell
   git clone https://github.com/Asabs18/PhysicsSim.git
   cd PhysicsSim
   ```
2. Install dependencies:
   ```powershell
   pip install pygame
   ```

### Running the Simulation
Run the main entry point:
```powershell
python main.py
```

## Author
- [Asabs18](https://github.com/Asabs18)