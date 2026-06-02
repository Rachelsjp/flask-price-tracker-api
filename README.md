# 🌐 Flask Price Tracker API

## **Description**

This project demonstrates how to build REST APIs using **Flask** and integrate them with browser automation using **Playwright**.

The solution exposes an API endpoint that automatically launches a browser, collects product pricing information from an e-commerce website, generates a pricing report, and returns the results as a JSON response.

The project was created as a learning exercise to understand Flask fundamentals, API development, browser automation, and data extraction workflows.

---

## **Author**

**Rachel Purnima Johnpeter**

This project was developed as part of my learning journey in Python web development, API creation, browser automation, and data analytics.

---

## **Business Use Case**

Many organizations require automated data collection services that can be triggered through APIs.

This project demonstrates how browser automation can be exposed as a reusable API service that can support:

* Retail price monitoring
* Automated data collection
* Reporting workflows
* Integration with dashboards
* Backend automation services

---

## **Tech Stack**

* Python 3.x
* Flask
* Playwright
* Pandas
* REST APIs
* JSON Responses

---

## **Project Components**

### **1. Flask Fundamentals**

File:

```python
flask_structure.py
```

Purpose:

* Demonstrates Flask application structure
* Creates a simple web server
* Exposes a basic route
* Returns HTTP responses

Endpoint:

```text
http://127.0.0.1:5000/
```

Sample Response:

```text
Hello social eagles welcome to community!!
```

---

### **2. Flask Price Tracker API**

File:

```python
flask_price_tracker.py
```

Purpose:

* Exposes a REST API endpoint
* Launches browser automation using Playwright
* Extracts product prices
* Generates CSV reports
* Returns JSON responses

Endpoint:

```text
http://127.0.0.1:5000/scrape
```

---

## **Features**

* REST API development using Flask
* Browser automation using Playwright
* Product price extraction
* CSV report generation
* JSON API responses
* Integration between web services and automation workflows

---

## **How It Works**

### Step 1

Start the Flask application.

### Step 2

Call the API endpoint:

```text
http://127.0.0.1:5000/scrape
```

### Step 3

Playwright launches a browser session.

### Step 4

The application navigates to the target website.

### Step 5

Product prices are extracted automatically.

### Step 6

Results are stored in a Pandas DataFrame.

### Step 7

A CSV report is generated.

### Step 8

The API returns a JSON response containing the results.

---

## **Sample JSON Response**

```json
{
  "status": "success",
  "message": "Report generated successfully"
}
```

---

## **Project Structure**

```text
flask_demo_project/
│
├── flask_structure.py
├── flask_price_tracker.py
└── README.md
```

---

## **Installation**

### Install Dependencies

```bash
pip install flask
pip install playwright
pip install pandas
```

### Install Playwright Browser

```bash
playwright install
```

---

## **Run Flask Fundamentals Example**

```bash
python flask_structure.py
```

Open:

```text
http://127.0.0.1:5000/
```

---

## **Run Price Tracker API**

```bash
python flask_price_tracker.py
```

Open:

```text
http://127.0.0.1:5000/scrape
```

---

## **Learning Objectives**

This project helped in understanding:

* Flask application architecture
* REST API development
* HTTP requests and responses
* JSON response handling
* Browser automation integration
* Data extraction workflows
* Report generation automation

---

## **Future Enhancements**

* Multi-retailer support
* Database integration
* Scheduled data collection
* Authentication and authorization
* Dashboard integration
* Cloud deployment
* AI-powered pricing recommendations

---

## **Limitations**

* Designed primarily for learning purposes
* Limited retailer support
* No authentication mechanism
* Local file storage only
* No retry or monitoring framework

---

## **Disclaimer**

This project was developed for educational and learning purposes. It demonstrates Flask API development, browser automation, and automated reporting using Python.
