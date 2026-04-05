import json
from event import Event

class EventManager:

    FILE = "data.json"

    def load_events(self):
        try:
            with open(self.FILE, "r") as file:
                data = json.load(file)
                return data
        except:
            return []

    def save_events(self, events):
        with open(self.FILE, "w") as file:
            json.dump(events, file, indent=4)

    def create_event(self):
        events = self.load_events()

        event_id = len(events) + 1
        name = input("Event name: ")
        date = input("Event date: ")
        location = input("Location: ")
        description = input("Description: ")

        event = Event(event_id, name, date, location, description)

        events.append(event.to_dict())
        self.save_events(events)

        print("✅ Event created successfully!")

    def view_events(self):
        events = self.load_events()

        if not events:
            print("No events found.")
            return

        for event in events:
            print(event)

    def view_event_by_id(self):
        events = self.load_events()

        event_id = int(input("Enter Event ID: "))

        for event in events:
            if event["event_id"] == event_id:
                print(event)
                return

        print("Event not found.")

    def update_event(self):
        events = self.load_events()

        event_id = int(input("Enter Event ID to update: "))

        for event in events:
            if event["event_id"] == event_id:

                event["name"] = input("New name: ")
                event["date"] = input("New date: ")
                event["location"] = input("New location: ")
                event["description"] = input("New description: ")

                self.save_events(events)

                print("✅ Event updated successfully!")
                return

        print("Event not found.")

    def mark_status(self):
        events = self.load_events()

        event_id = int(input("Enter Event ID: "))

        for event in events:
            if event["event_id"] == event_id:

                status = input("Enter status (upcoming/completed): ")
                event["status"] = status

                self.save_events(events)

                print("✅ Status updated!")
                return

        print("Event not found.")

    def delete_event(self):
        events = self.load_events()

        event_id = int(input("Enter Event ID to delete: "))

        for event in events:
            if event["event_id"] == event_id:
                events.remove(event)

                self.save_events(events)

                print("🗑 Event deleted.")
                return

        print("Event not found.")