# Cloud-Based Linux Server Performance Monitoring

## 📖 Overview
This project provides a remote dashboard to monitor cloud-based Linux servers. It includes an API for collecting system metrics and a dashboard for real-time visualization.

## 🛠️ Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/cloud-server-monitoring.git
cd Unix-Project-Cloud-Server-monitoring
```

### 2️⃣ Install Dependencies
```bash
cd api && pip install -r requirements.txt
cd ../dashboard && pip install -r requirements.txt
```

### 3️⃣ Start the API
```bash
python3 api/monitoring_api.py
```
This starts the monitoring API, which collects system performance data.

### 4️⃣ Start the Dashboard
```bash
python3 dashboard/dashboard.py
```
The dashboard provides a web-based interface to view system metrics.

## 📂 Project Structure
```
cloud-server-monitoring/
│── api/                   # API to collect system metrics
│   ├── monitoring_api.py  # Main API script
│   ├── requirements.txt   # Dependencies for the API
│
│── dashboard/             # Web-based dashboard
│   ├── dashboard.py       # Main dashboard script
│   ├── requirements.txt   # Dependencies for the dashboard
│
│── docs/                  # Documentation
│   ├── README.md          # Project documentation
│   ├── report.docx        # Additional reports (if applicable)
│
│── scripts/               # Shell scripts for automation
│   ├── restart-check.sh   # Script to check and restart services
│   ├── stress-test.sh     # Script to test system stress handling
│
│── systemd/               # Systemd service files
│   ├── stress-test.service # Systemd service file for automation
│
│── LICENSE                # License file
│── README.md              # Project documentation
```

## 🖥️ Features
- 📊 **Live Server Performance Metrics**: Track CPU, Memory, and Disk usage.
- 🌐 **Web Dashboard**: View performance data remotely.
- ⚙️ **Automated Monitoring**: Systemd services for stress testing and recovery.
- 🛠️ **Custom Scripts**: Scripts for service restart and stress testing.

## 🚀 Future Enhancements
- 📈 Add support for logging and historical data.
- 🔒 Implement authentication for secure access.
- ☁️ Cloud integration (AWS, Azure, etc.).

## 📝 License
This project is licensed under the MIT License.
