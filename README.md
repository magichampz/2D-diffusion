# 2D-diffusion

*As part of a programming assignment. The assignment handout can be found in the directory.*

Python script written to simulate 2 dimensional diffusion of a material through space and time. The class Diffusion represents a 2D array consisting of value states (float values between 0.0 and 1.0). Each state represents the normalised density of diffusing material.

The simulaiton accounts for different boundary conditions which can be set when the class is initialized. Boundary conditions for each border can be set to Neumann (0) or Direchelt (1) as described in the handout.

### Functions
The class Diffusion contains the following functions:

**set_cell(self, row_range, col_range, value)**: Modifies the state of cells in the material by modifying the space attribute

**print_space(self)**: View the current state of the material

**next_step(self, time_steps)**: Simulates diffusion through the material depending on the number of time_steps
