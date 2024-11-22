# Running the ROS Nodes

## Dependencies

- **ROS (Robot Operating System)**
- **Pygame** (for pygame-based control)
  - Install Pygame using:
    ```bash
    pip install pygame
    ```

## Setting Up

1. Clone the repository into your ROS workspace:
   - Navigate to the `~/catkin_ws/src` directory.
   - Run the following command:
     ```bash
     git clone https://github.com/RodrigoDuranM/RP_Nazarie_Horia_Duran_Rodrigo.git
     ```

2. Move to the `ROS` branch:
   - After cloning the repository, switch to the `ROS` branch:
     ```bash
     cd RP_Nazarie_Horia_Duran_Rodrigo
     git checkout ROS
     ```

3. Build the workspace:
   - Navigate to the root of your workspace:
     ```bash
     cd ~/catkin_ws
     ```
   - Build the workspace using:
     ```bash
     catkin_make
     ```

4. Source the setup file:
   - Run the following command to ensure ROS recognizes the new packages:
     ```bash
     source devel/setup.bash
     ```

## Running the Nodes (in different terminals)

1. **Collect User Information**:
   - Run the `info_user.py` node to collect user information:
     ```bash
     rosrun game_control info_user.py
     ```

2. **Start the Game**:
   - Run the `game_node.py` to start the game:
     ```bash
     rosrun game_control game_node.py
     ```

3. **Control the Paddle**:
   - For keyboard control, run:
     ```bash
     rosrun game_control control_node.py
     ```
   - For pygame control, run:
     ```bash
     rosrun game_control control_node_pygame.py
     ```

4. **Display Final Score**:
   - Run the `result_node.py` to display the final score:
     ```bash
     rosrun game_control result_node.py
     ```

## Communication Between Nodes

- These nodes communicate via ROS topics to manage:
  - User input
  - Game logic
  - Displaying the final score
