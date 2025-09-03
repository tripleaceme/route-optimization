#### 📦 Logistics Route Optimization Dashboard



This project simulates a logistics company struggling with **delivery delays, rising fuel costs, and inefficient routing**. We generate synthetic data (5,000 deliveries), store it in **MySQL**, and build a **3-page Streamlit dashboard** to analyze operations, simulate routes, and generate actionable recommendations.


---

#### 🎯 Case Study – Problem Statement

**Business context:**
A logistics company has been receiving complaints about **late deliveries** and **high fuel consumption**. Management wants to understand:

* Which **cities and depots** face the most delivery challenges?
* How can we **visualize and optimize routes**?
* What **operational improvements** could reduce cost and CO₂ emissions?

**Our goal:**
Build an **interactive dashboard** that ingests delivery data, highlights key issues, simulates routing, and recommends optimizations.

---

#### 🛠️ Tech Stack

* **Python** – Data generation & preprocessing
* **Pandas** – Analysis
* **MySQL** – Data storage
* **SQLAlchemy + PyMySQL** – Database connectivity
* **Streamlit** – Interactive dashboard
* **dotenv** – Secure connection management

---

#### 📂 Project Structure

```
logistics_route_opt_project/
│
├── generate_data.py           # Script to generate 5000 deliveries dataset
├── logistics_deliveries.csv   # Synthetic dataset (generated)
├── schema.sql                 # MySQL schema
├── upload_to_mysql.py         # Upload CSV to MySQL
├── requirements.txt           # Dependencies
├── README.md                  # This file
│
└── app/
    ├── Home.py                # Main app entry
    └── pages/
        ├── 1_Overview.py
        ├── 2_Routing_Simulator.py
        └── 3_Insights_Recommendations.py
```

---

#### 📊 Dataset

Generated with `generate_data.py` (\~5,000 rows).

Each row represents a delivery order with:

* **Order details**: order\_id, date, region, city
* **Geolocation**: depot & customer lat/lon
* **Operational metrics**: distance, service time, traffic factor, vehicle id
* **Cost & environment**: fuel cost, CO₂ estimate
* **Performance outcome**: delivered\_late (yes/no), status

---

#### 🚀 How to Run the Project

##### 1. Clone & install requirements

```bash
git clone https://github.com/tripleaceme/route-optimization.git
cd route-optimization
pip install -r requirements.txt
```

##### 2. Generate synthetic dataset

```bash
python generate_data.py
```

This creates `logistics_deliveries.csv` (5,000 rows).

##### 3. (Optional) Upload to MySQL

1. Create a new MySQL database, e.g.:

   ```sql
   CREATE DATABASE logistics_db;
   ```
2. Run:

   ```bash
   python upload_to_mysql.py
   ```

##### 4. Run the Streamlit app

```bash
cd app
streamlit run home.py
```

---

#### 📑 Dashboard Pages

##### **1. Overview**

* Delivery KPIs (total orders, avg distance, late delivery rate, fuel costs).
* Data quality preview.
* Quick filters for city/region.

##### **2. Routing Simulator**

* Select an order date and view delivery locations on a map.
* Explore potential inefficiencies by visualizing depot vs. customer spread.
* (Extensible: integrate OR-Tools for real route optimization).

##### **3. Insights & Recommendations**

* Top 10 cities with highest late delivery rates.
* Recommendations for operations:

  * Deploy more vehicles in delay-prone zones.
  * Prioritize high-value deliveries during off-peak.
  * Introduce micro-depots for dense cities.
  * Improve route optimization with solver libraries.

---

#### 📌 Next Steps


* Replace synthetic data with **real delivery APIs** (e.g., OpenStreetMap).
* Add **predictive modeling**: which deliveries are most likely to be late?