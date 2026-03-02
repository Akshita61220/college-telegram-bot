from database import insert_college

sample_data = [
    {
        "name": "IIT Bombay",
        "location": "Mumbai",
        "ranking": 1,
        "description": "Top engineering institute in India.",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/0/00/IIT_Bombay_Logo.svg"
    },
    {
        "name": "IIT Delhi",
        "location": "Delhi",
        "ranking": 2,
        "description": "Premier technical institute.",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/8/86/IIT_Delhi_Logo.svg"
    }
]

for college in sample_data:
    insert_college(college)

print("Sample data inserted successfully!")