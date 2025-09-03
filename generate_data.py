import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)

# Sample cities (can expand)
cities = [
    {"city": "Lagos", "lat": 6.5244, "lon": 3.3792},
    {"city": "Abuja", "lat": 9.0765, "lon": 7.3986},
    {"city": "Kano", "lat": 12.0022, "lon": 8.5919},
    {"city": "Port Harcourt", "lat": 4.8156, "lon": 7.0498},
    {"city": "Ibadan", "lat": 7.3775, "lon": 3.9470},
]

regions = ["North", "South", "East", "West"]
statuses = ["Pending", "In Transit", "Delivered"]
priorities = ["Low", "Medium", "High"]

def generate_dataset(n=1000):
    rows = []
    base_date = datetime(2024, 1, 1)

    for i in range(n):
        city_info = random.choice(cities)
        city, base_lat, base_lon = city_info["city"], city_info["lat"], city_info["lon"]

        order_id = f"ORD{i+1:05d}"
        order_date = base_date + timedelta(days=random.randint(0, 200))
        region = random.choice(regions)

        # Customer location (jitter around city)
        cust_lat = base_lat + np.random.uniform(-0.1, 0.1)
        cust_lon = base_lon + np.random.uniform(-0.1, 0.1)

        # Depot info
        depot_id = f"DEP{random.randint(1,5)}"
        depot_lat = base_lat + np.random.uniform(-0.2, 0.2)
        depot_lon = base_lon + np.random.uniform(-0.2, 0.2)

        vehicle_id = f"VEH{random.randint(1,50)}"
        priority = random.choice(priorities)
        weight = round(np.random.uniform(0.5, 50.0), 2)
        service_time = random.randint(5, 30)

        start_hour = random.randint(6, 18)
        time_window_start = f"{start_hour:02d}:00:00"
        time_window_end = f"{start_hour+2:02d}:00:00"

        dist = round(np.random.uniform(2, 100), 2)
        traffic = round(np.random.uniform(0.8, 1.5), 2)
        travel_time = round(dist / 40 * 60 * traffic, 1)  # avg 40km/h
        delivery_time = travel_time + service_time

        delivered_late = random.random() < 0.15  # ~15% late
        fuel_cost = round(dist * 0.6, 2)  # assume $0.6/km
        co2 = round(dist * 0.25, 2)       # assume 0.25 kg/km
        status = random.choice(statuses)

        rows.append([
            order_id, order_date.date(), region, city,
            cust_lat, cust_lon,
            depot_id, depot_lat, depot_lon,
            vehicle_id, priority, weight, service_time,
            time_window_start, time_window_end,
            dist, traffic, travel_time, delivery_time,
            delivered_late, fuel_cost, co2, status
        ])

    cols = [
        "order_id","order_date","region","city",
        "customer_lat","customer_lon","depot_id","depot_lat","depot_lon",
        "vehicle_id_planned","priority","package_weight_kg","service_time_min",
        "time_window_start","time_window_end","distance_km_est","traffic_factor",
        "travel_time_min_est","delivery_duration_min_est","delivered_late",
        "fuel_cost_est","co2_kg_est","status"
    ]

    return pd.DataFrame(rows, columns=cols)

if __name__ == "__main__":
    df = generate_dataset(5000)
    df.to_csv("logistics_deliveries.csv", index=False)
    print("✅ logistics_deliveries.csv generated with", len(df), "rows")
