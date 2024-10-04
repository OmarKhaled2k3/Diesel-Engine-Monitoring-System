
# Diesel Engine Monitoring System

## Overview
This project is a real-time monitoring solution for diesel engines, utilizing various sensors to track temperature and vibrations. The sensors are connected to an Arduino Mega 2560, which sends data to a Python script on a PC via serial communication. The data is logged, visualized, and analyzed using AI to determine the operational health of the engine and identify potential issues.

## Features
- **Sensors Used**: MAX6675 thermocouples, vibration sensors, and a piezo vibration sensor.
- **Arduino Mega 2560**: The Arduino is used to read data from all sensors and transmit it to the PC via serial communication.
- **Data Logging**: Continuously logs sensor data and stores it for offline analysis.
- **Real-Time Visualization**: Plots temperature and vibration data using Matplotlib in real time, allowing instant insight into engine performance.
- **AI Analysis**: Generates a report from collected data to feed into an AI model, which assesses engine health and detects anomalies.

## Components
1. **MAX6675 K-Thermocouple- to-Digital Converter (0C to +1024C)**: Measures temperature of different engine components.
2. **Vibration Sensors Module (801S)**: Detect irregularities in engine movement.
3. **Piezo Vibration Sensor**: Provides detailed vibration profiles.
4. **Arduino Mega 2560**: Acts as the interface for reading sensor data and sending it to the Python script.

## System Architecture
1. **Data Collection**: Sensors are connected to the Arduino Mega 2560, which collects the data and sends it to a Python script on a PC using serial communication.
2. **Real-Time Visualization**: Matplotlib is used to provide visual feedback on engine conditions.
3. **Data Logging**: Recorded data is saved into a CSV file for later analysis.
4. **AI Failure Detection**: Data is fed into an AI model that classifies engine status as "Healthy" or "Faulty."

## Installation
1. **Clone the Repository**
   ```
   git clone https://github.com/OmarKhaled2k3/Diesel-Engine-Monitoring-System.git
   ```
2. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```
## Schematic
![Schematic_bb](https://github.com/user-attachments/assets/d5601a30-e711-4dda-805a-71bf78858b3d)

## Requirements
- Arduino Mega 2560
- Python 3.7+
- Libraries: `matplotlib`, `pandas`, `numpy`, `scipy`
- Serial communication library (e.g., `pyserial`)

## Usage
- **Real-Time Monitoring**: Visualize engine data while the engine is operating.
- **Failure Prediction**: Run the data through an AI model for fault detection and anomaly classification.

## Applications
- Predictive maintenance for diesel engines.
- Early detection of engine faults to prevent costly repairs.
- Performance monitoring and logging for further analysis.

## Data Collected Visualized View
![DataExtractedV3](https://github.com/user-attachments/assets/21bc4b03-f582-4edb-b49b-c7234a4c174f)

## Future Improvements
- Integrate wireless communication for remote monitoring.
- Add support for other sensor types.
- Expand AI capabilities to classify different types of engine faults.

## Contributing
Feel free to contribute by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT License](LICENSE)

## Acknowledgments
- Thanks to the open-source community for helpful tools and libraries.
- Special appreciation for resources on real-time data monitoring and AI-based fault detection.
