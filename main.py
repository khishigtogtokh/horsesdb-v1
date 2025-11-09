import sys
from db.storage import create_table 

def main(): 
    if len(sys.argv) < 3: 
        print(f"Usage: python main.py create_table <table_name> <col1,col2,col3>")
        return

    command = sys.argv[1]
    if command == "create_table":
        table_name = sys.argv[2]
        columns = sys.argv[3].split(",") if len(sys.argv) > 3 else []
        create_table(table_name, columns)
    else:
        print(f"Unknown command: '{command}'")

if __name__ == "__main__":    
    main()
