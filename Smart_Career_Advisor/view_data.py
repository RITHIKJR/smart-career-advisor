import sqlite3
import pandas as pd

def view_database():
    """View all data in the database"""
    conn = sqlite3.connect('users.db')
    
    print("=" * 80)
    print("SMART CAREER ADVISOR - DATABASE VIEWER")
    print("=" * 80)
    
    # Get all table names
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    print(f"\n📊 Found {len(tables)} tables in database\n")
    
    # Display each table
    for table in tables:
        table_name = table[0]
        print(f"\n{'='*80}")
        print(f"📋 TABLE: {table_name.upper()}")
        print(f"{'='*80}")
        
        # Get data from table
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        
        if len(df) == 0:
            print("   (No data yet)")
        else:
            print(f"\n   Total Records: {len(df)}")
            print(f"\n{df.to_string()}\n")
    
    conn.close()
    print("\n" + "="*80)
    print("✅ Database view complete!")
    print("="*80)

if __name__ == "__main__":
    view_database()
