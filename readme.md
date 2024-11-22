# Running the ROS Nodes

## Dependencies

- ROS (Robot Operating System)
- A ROS workspace (`~/catkin_ws/src`)
- Python 2 or 3 (depending on the ROS version)
- Required ROS packages:
  - `game_control` package

## Setting Up

1. Clone the repository into your ROS workspace:
   - Navigate to `~/catkin_ws/src` directory.
   - Run the following command:
     ```
     git clone <repository-url>
     ```
   
2. Build the workspace:
   - Navigate to the root of your workspace:
     ```
     cd ~/catkin_ws
     ```
   - Build the workspace using:
     ```
     catkin_make
     ```

3. Source the setup file:
   - Run the following command to ensure ROS recognizes the new packages:
     ```
     source devel/setup.bash
     ```

## Running the Nodes

1. **Collect User Information**:
   - Run the `info_user.py` node to collect user information:
     ```
     rosrun game_control info_user.py
     ```

2. **Start the Game**:
   - Run the `game_node.py` to start the game:
     ```
     rosrun game_control game_node.py
     ```

3. **Control the Paddle**:
   - For keyboard control, run:
     ```
     rosrun game_control control_node.py
     ```
   - For pygame control, run:
     ```
     rosrun game_control control_node_pygame.py
     ```

4. **Display Final Score**:
   - Run the `result_node.py` to display the final score:
     ```
     rosrun game_control result_node.py
     ```

## Communication Between Nodes

- These nodes communicate via ROS topics to manage:
  - User input
  - Game logic
  - Display the final score
