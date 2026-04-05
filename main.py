from event_manager import EventManager

manager = EventManager()

def menu():
    print("""
==== EVENT PLANNER CLI ====

1. Create Event
2. View All Events
3. View Event By ID
4. Update Event
5. Mark Event Status
6. Delete Event
7. Exit
""")

while True:

    menu()

    choice = input("Choose an option: ")

    if choice == "1":
        manager.create_event()

    elif choice == "2":
        manager.view_events()

    elif choice == "3":
        manager.view_event_by_id()

    elif choice == "4":
        manager.update_event()

    elif choice == "5":
        manager.mark_status()

    elif choice == "6":
        manager.delete_event()

    elif choice == "7":
        print("Goodbye 👋")
        break

    else:
        print("Invalid option")