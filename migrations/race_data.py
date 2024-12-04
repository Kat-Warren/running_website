#from app import db
from models import Races
from datetime import datetime

# Define a list of race data
races = [
    {"name": "Marathon 2024", "date": datetime(2024, 4, 20), "description": "Annual city marathon", "competing": True},
    {"name": "Triathlon Summer Challenge", "date": datetime(2024, 6, 15), "description": "A summer triathlon event", "competing": False},
    {"name": "Night Run", "date": datetime(2024, 9, 1), "description": "Night-time fun run", "competing": True},
    {"name": "Spring Relay Race", "date": datetime(2024, 3, 25), "description": "Exciting relay race to welcome spring", "competing": True},
    {"name": "Ironman Competition", "date": datetime(2024, 7, 10), "description": "Extreme endurance triathlon", "competing": False},
    {"name": "Winter Charity Walk", "date": datetime(2024, 12, 15), "description": "Fundraiser charity walk", "competing": False},
    {"name": "Kids Fun Run", "date": datetime(2024, 5, 12), "description": "A short run for kids aged 6-12", "competing": True},
    {"name": "Halloween Haunted Dash", "date": datetime(2024, 10, 31), "description": "Spooky run on Halloween night", "competing": True},
    {"name": "Autumn Forest Trek", "date": datetime(2024, 11, 20), "description": "Scenic trek through the autumn forest", "competing": False},
    {"name": "New Year Resolution Run", "date": datetime(2025, 1, 1), "description": "Start the year with a healthy habit", "competing": True}
]

# Add races to the database
for race_data in races:
    race = Races(
        name=race_data["name"],
        date=race_data["date"],
        description=race_data["description"],
        competing=race_data["competing"]
    )
    db.session.add(race)

# Commit the session
db.session.commit()

print("Races table populated with sample data!")
