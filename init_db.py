"""
Database initialization script for Vercel deployment.
Run this once after setting up Vercel Postgres to create tables.

Usage:
    python init_db.py
"""

from app import app, db

def init_database():
    """Create all database tables."""
    with app.app_context():
        try:
            # Create all tables
            db.create_all()
            print("✅ Database tables created successfully!")
            print("\nTables created:")
            print("  - user")
            print("  - course")
            print("\nYou can now use the application.")
        except Exception as e:
            print(f"❌ Error creating database tables: {e}")
            raise

if __name__ == '__main__':
    init_database()
