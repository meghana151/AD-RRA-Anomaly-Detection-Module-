# AD-RRA: Anomaly Detection Module
This project implements a real-time anomaly detection pipeline for spacecraft telemetry using an ensemble model of Autoencoder (AE) + Isolation Forest (IF), adaptive thresholding, and false-positive smoothing techniques. It is suitable for space-grade deployment scenarios where low-latency, accurate anomaly detection is essential.

## 📂 Project Structure
```
space-anomaly-detection/
├── data/
│ └── segments.csv                     # Sample telemetry data
├── models/
│ ├── autoencoder.py                   # Autoencoder model
│ ├── isolation_forest.py              # Isolation Forest
│ └── ensemble.py                      # Fusion of models
├── preprocessing/
│ ├── windowing.py                     # Sliding window logic
│ └── normalize.py                     # Data normalization
├── demo/
│ ├── realtime_demo.py                 # End-to-end demo script
│ └── visualize.py                     # Plotting utilities
├── evaluation/
│ ├── metrics.py                       # F1, confusion matrix, precision, recall
│ └── fpr_reduction.py                 # Adaptive thresholding, smoothing
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

To set up the project locally:
1. Clone the Repository
```bash
git clone https://github.com/your-username/space-anomaly-detection.git
cd space-anomaly-detection
```
2. Install dependencies
```bash
   pip install -r requirements.txt
```
3. How to Run the Demo
```bash
  python demo/realtime_demo.py
```
Make sure the segments.csv is placed inside the data/ folder.

## Performance Considerations for Space-Grade Deployment
Low latency: Sliding window + pre-trained models enable real-time inference.  

Lightweight: Isolation Forest and CNN-based AE are efficient for edge deployment.  

False positives: Handled via adaptive thresholding & temporal smoothing.

Modularity: Easily extendable to include TCNs, LSTMs, or onboard compression.

## Future Enhancements
Integrate a TCN-based classifier

Add hardware-aware deployment benchmarks

Apply to multi-channel data fusion

Onboard anomaly alert + logging system
   
