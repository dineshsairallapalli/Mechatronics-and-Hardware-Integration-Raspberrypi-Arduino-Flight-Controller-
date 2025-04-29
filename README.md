# Mechatronics-and-Hardware-Integration-Raspberrypi-Arduino-Flight-Controller

### **Description**
This repository implements a hybrid mechatronics system capable of transforming from a rover to a drone. Leveraging advanced control algorithms, sensor integration, and robust mechanical design, the project demonstrates seamless transitions between land-based and aerial functionalities. The repository includes Arduino and Python code, detailed project documentation, and visual demonstrations, providing a comprehensive guide to hybrid robotic systems.

---

### **Project Overview**
#### **Objective**
To create a highly adaptable hybrid robot (Morphobot) that transitions smoothly between land-based and aerial functionalities. The system is designed for remote-controlled operations, incorporating RF and Bluetooth technologies for seamless switching.

#### **Technologies and Tools**
- **Hardware**:
  - Raspberry Pi: Main controller for rover operations.
  - Arduino: Controller for aerial (drone) operations.
  - Servo Motors: Enables mechanical transformations.
  - RF and Bluetooth Modules: Wireless communication.
- **Software**:
  - Arduino IDE for Quadcopter and Transformation Code.
  - Python for rover control and sensor integration.
- **Algorithms**:
  - PID control for quadcopter stabilization.
  - Servo control for mechanical adjustments.
  - Obstacle avoidance and motor control for rover navigation.

---

### **Features and Functionality**
1. **Rover Module**:
   - Uses Raspberry Pi as the primary controller.
   - Implements motor control for movement and navigation.
   - Python-based obstacle avoidance and remote operations.

2. **Drone Module**:
   - Arduino-based flight control using PID algorithms.
   - Stabilization and motor testing routines.
   - Seamless switching from rover to drone mode using servo motors.

3. **Transformation Mechanism**:
   - Controlled via servo motors.
   - Arduino sketch (`Servo.ino`) handles positional adjustments.

---

### **Detailed PID Control for Quadcopter Stabilization**
#### **Overview**
The **PID (Proportional-Integral-Derivative)** controller is the foundation of the quadcopter's stabilization system. It ensures the quadcopter maintains stable orientation by adjusting motor speeds to minimize errors in roll, pitch, and yaw.

#### **PID Components**
- **Proportional (P)**: Reacts to the current error for immediate correction.
- **Integral (I)**: Accumulates past errors to counteract steady-state bias.
- **Derivative (D)**: Predicts future errors to prevent overshooting and oscillations.

#### **Implementation Highlights**
- PID control adjusts the speed of all four motors based on calculated corrections:
  ```cpp
  motor1_speed = base_speed + roll_output - pitch_output + yaw_output;
  motor2_speed = base_speed - roll_output - pitch_output - yaw_output;
  motor3_speed = base_speed - roll_output + pitch_output + yaw_output;
  motor4_speed = base_speed + roll_output + pitch_output - yaw_output;
  ```
- Each axis of rotation (roll, pitch, yaw) is controlled independently:
  ```cpp
  float roll_output = Kp_roll * roll_error + Ki_roll * roll_integral + Kd_roll * roll_derivative;
  float pitch_output = Kp_pitch * pitch_error + Ki_pitch * pitch_integral + Kd_pitch * pitch_derivative;
  float yaw_output = Kp_yaw * yaw_error + Ki_yaw * yaw_integral + Kd_yaw * yaw_derivative;
  ```

#### **Performance Metrics**
- **Stabilization Time**: Stabilizes within one second of disturbance.
- **Overshoot**: Minimal due to precise tuning of derivative gain (`Kd`).
- **Responsiveness**: Quick adjustments to control inputs and disturbances.

#### **Challenges and Solutions**
- Drift and bias corrected by the integral term.
- Noise handled using low-pass filtering for sensor inputs.
- Sudden disturbances dampened with derivative adjustments.

---

### **Code Structure and Highlights**
#### **Quadcopter Code** (Arduino)
- **PID Control**: Integrated into `Code4.ino`, balancing stability with responsiveness.
- **Motor Diagnostics**: `Code3.ino` includes routines for vibration analysis and motor testing.

#### **Rover Code** (Python)
- GPIO and PWM-based motor control for navigation and obstacle avoidance.
- Wireless integration for remote operations.

#### **Transformation Code** (Arduino)
- Servo-controlled positional adjustments for mode transitions.

---

### **Project Deliverables**
1. **Documentation**:
   - Proposal: Objectives, scope, and initial plan.
   - Report: Detailed methodology, results, and analysis.
   - Presentations: Project walkthrough and progress highlights.

2. **Media**:
   - `Rover to drone conversion.mp4`: Demonstration of transformation mechanism.
   - `Team video.mp4`: Highlights team efforts and project milestones.

3. **Code**:
   - Comprehensive scripts for quadcopter, rover, and transformation mechanisms.

---

### **How to Use**
1. Clone the repository:
   ```bash
   git clone https://github.com/dineshsairallapalli/Hybrid-Rover-to-Drone-Transformation.git
   cd Hybrid-Rover-to-Drone-Transformation
   ```
2. Deploy the code to respective controllers:
   - Use Arduino IDE for Quadcopter and Transformation code.
   - Use Python environment for Rover code.

3. Run the modules:
   - **Quadcopter**: Upload and run the Arduino sketches for motor control and flight stabilization.
   - **Rover**: Execute `integratedcode.py` for motor navigation and obstacle avoidance.
   - **Transformation**: Upload `Servo.ino` to manage transitions.

---

### **Applications**
- **Disaster Response**: Navigate challenging terrains and take aerial surveillance when needed.
- **Search and Rescue**: Combines land mobility with aerial reconnaissance.
- **Robotics Research**: Demonstrates seamless integration of multiple robotic platforms.

---

### **Future Enhancements**
- Integrate SLAM (Simultaneous Localization and Mapping) for autonomous navigation.
- Add GPS for location-based operations.
- Optimize battery consumption for extended operational periods.
