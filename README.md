# 🎤 AI Speech-to-Text System

> 🚀 Convert voice into text in real-time using scalable system design, distributed architecture, and AI-powered speech recognition.

---

## 🚀 Highlights

- Designed a **Kafka-based event-driven pipeline** for real-time speech processing  
- Built a **scalable distributed system** handling concurrent audio streams  
- Integrated **cloud-based AI speech recognition APIs**  
- Implemented **low-latency streaming using WebSockets**  
- Demonstrates **production-level backend and system design thinking**

---

## 🧠 Project Overview

This project is a **real-time Speech-to-Text system** designed to convert spoken audio into accurate text using modern AI and distributed system architecture.

Unlike basic implementations, this system is built with **scalability and performance in mind**, using event-driven architecture and streaming pipelines to handle multiple concurrent audio inputs efficiently.

---

## ⚡ Key Features

- 🎤 **Real-Time Speech Recognition**
- ⚡ **Event-Driven Architecture (Kafka-based)**
- 🔄 **Asynchronous Processing Pipeline**
- 🧵 **Multithreaded Consumer System**
- ☁️ **Cloud Speech APIs Integration**
- 📡 **Live Text Streaming via WebSockets**
- 📊 **Optimized for Low Latency & High Throughput**

---

## 🏗️ System Architecture

The system follows a **distributed event-driven architecture**:

1. 🎙️ Audio captured via browser (Web Audio API)  
2. 📤 Audio sent to backend (Spring Boot server)  
3. 📦 Audio pushed to Kafka topic  
4. ⚙️ Multithreaded consumers process audio  
5. 🤖 Speech-to-Text API generates transcript  
6. 📡 Results streamed back to client in real-time  

---

## 🛠 Tech Stack

### Backend
- Java (Spring Boot)
- Apache Kafka
- MongoDB

### Frontend
- HTML5, JavaScript
- Web Audio API
- WebSockets

### AI / Cloud
- Google Cloud Speech-to-Text API

--

## 🔗 How It Works

```mermaid
flowchart LR
A[User Speech] --> B[Web Audio API]
B --> C[Spring Boot Backend]
C --> D[Kafka Queue]
D --> E[Consumer Service]
E --> F[Speech-to-Text API]
F --> G[Transcript Output]
G --> H[Frontend Display]
```

## 🚀 Compilation & Setup Steps

### 1. Prerequisites
- **Python 3.8+**
- **Java 17+** (For Spring Boot Backend)
- **Apache Kafka** & **Zookeeper**
- **MongoDB**

### 2. Python Scripts Setup (Prototyping)
To run the Python speech-to-text scripts (`speechtotext.py` & `mictotextvosk.py`), install the required dependencies:

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
# On Windows use: venv\Scripts\activate
# On Linux/Mac use: source venv/bin/activate
venv\Scripts\activate

# Install dependencies
pip install SpeechRecognition sounddevice vosk
```

**Running the scripts:**
- **Vosk Mic to Text:** Download the appropriate Vosk model (e.g., `vosk-model-small-en-us-0.15`), extract it in the project root, and run:
  ```bash
  python mictotextvosk.py
  ```
- **Google Speech-to-Text (Audio File):** Ensure you have a `sample.wav` file in the project root and run:
  ```bash
  python speechtotext.py
  ```

### 3. Spring Boot Backend Setup
1. **Start Kafka and Zookeeper** locally or via Docker.
2. **Start MongoDB** and ensure it's running on the default port `27017`.
3. Navigate to the backend directory.
4. **Compile and Run** using Maven:
   ```bash
   ./mvnw clean install
   ./mvnw spring-boot:run
   ```

### 4. Frontend Setup
1. Serve the frontend folder using a local web server (e.g., Python's `http.server`):
   ```bash
   python -m http.server 8080
   ```
2. Open `http://localhost:8080` in your web browser to start using the application.
