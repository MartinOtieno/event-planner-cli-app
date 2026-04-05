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

    def display(self):
        print("\nEvent ID:", self.event_id)
        print("Name:", self.name)
        print("Date:", self.date)
        print("Location:", self.location)
        print("Description:", self.description)
        print("Status:", self.status)