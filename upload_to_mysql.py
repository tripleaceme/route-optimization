import argparse
import os
import pandas as pd
from sqlalchemy import create_engine, text



def get_engine():
    host =  "localhost"
    port = 3306
    user = "superset"
    pwd = "superset"
    db = "route_optimization_db"
    url = f"mysql+pymysql://{user}:{pwd}@{host}:{port}/{db}"
    return create_engine(url)

def ensure_schema(engine):
    schema = open("route-optimization/schema.sql", "r").read()
    with engine.begin() as conn:
        for statement in schema.split(";"):
            stmt = statement.strip()
            if stmt:
                conn.execute(text(stmt))

def main():
    df = pd.read_csv("route-optimization/logistics_deliveries.csv")
    engine = get_engine()
    ensure_schema(engine)
    df.to_sql("logistics_deliveries", con=engine, if_exists="replace", index=False, chunksize=1000, method="multi")
    print("Upload complete.")

if __name__ == "__main__":
    main()
