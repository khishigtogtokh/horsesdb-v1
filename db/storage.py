import os, json

DATA_DIR = "horsesdata"

def ensure_data():
    os.makedirs(DATA_DIR, exist_ok=True)

def create_table(name, columns):
    ensure_data()
    path = os.path.join(DATA_DIR, f"{name}.json")

    if os.path.exists(path): 
        print(f"Table '{name}' already exists.")
        return

    schema = {}
    for col in columns: 
        if ":" in col: 
            cname, ctype = col.split(":")
            schema[cname.strip()] = ctype.strip()
        else: 
            schema[cname.strip()] = "str"

    table_data = {
        "_schema": {"columns": schema},
        "rows": []
    }

    with open(path, "w", encoding="utf-8") as f: 
        json.dump(table_data, f, indent=2)

    print(f"Table '{name}' created with columns: '{columns}'")
