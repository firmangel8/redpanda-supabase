# 📦 Event-Driven Architecture with Redpanda & Supabase

## 🔍 Educational Demo Repository

This repository is designed for educational purposes only, demonstrating how to build an event-driven architecture using Redpanda (a Kafka-compatible streaming platform) in combination with Supabase, an open-source alternative to traditional database management systems.

## 🎯 Objective
To help developers, students, and educators understand the principles of real-time event streaming and data persistence using modern, open-source tools.

## 🔧 Tech Stack
Redpanda – Kafka-compatible event streaming platform for high-performance data pipelines.
Supabase – Backend-as-a-Service built on PostgreSQL, offering real-time subscriptions and RESTful APIs.
Python

## 🧪 Demonstrated Concepts
Publish/subscribe messaging with Redpanda topics
Event consumption and transformation
Data persistence into Supabase
Real-time data pipeline in a microservices-friendly setup

## ⚠️ Disclaimer
This project is intended strictly for educational and demonstration purposes. It is not optimized or secured for production environments.

## 🏁 Getting Started
Clone the repo, configure environment variables, and spin up the services with Docker to explore a working event-driven pipeline in action.
Make sure you already have redpanda docker-compose.yml.

## Installation
### Step 1: Clone the repository
```bash
git clone git@github.com:firmangel8/redpanda-supabase.git
cd redpanda-supabase
```

or clone with:
```bash
git clone https://github.com/firmangel8/redpanda-supabase.git
cd redpanda-supabase
```

### Step 2: Install depedencies
`pip install -r requirements.txt`

### Step 3: How to Use

1. **Start the Consumer**
   Run the following command to start the event consumer:
   ```bash
   python consumer.py
   ```

2. **Send a Message**
   Use the sender script to publish a message:
   ```bash
   python sender.py -m "your message"
   ```
