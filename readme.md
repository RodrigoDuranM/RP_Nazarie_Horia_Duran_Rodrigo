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

## Running the Nodes (with the Launcher)

1. **Launch All Nodes**:  
   Use the provided launch file to start all nodes together in separate terminals:
   ```bash
   roslaunch game_control start_game.launch

2. **Test Parameters and Services**:
   Use 'rosparam' and 'rosservice' methods to test the nodes.