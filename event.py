class Event:
    def __init__(self, event_id, name, date, location, description, status="upcoming"):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.location = location
        self.description = description
        self.status = status

    def to_dict(self):
        return {
            "event_id": self.event_id,
            "name": self.name,
            "date": self.date,
            "location": self.location,
            "description": self.description,
            "status": self.status
        }

    def __str__(self):
        return f"""
Event ID: {self.event_id}
Name: {self.name}
Date: {self.date}
Location: {self.location}
Description: {self.description}
Status: {self.status}
"""