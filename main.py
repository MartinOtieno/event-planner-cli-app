from event_manager import EventManager

manager = EventManager()


def menu():

    print("\n===== EVENT PLANNER CLI =====")

    print("1. Create Event")
    print("2. View All Events")
    print("3. View Event By ID")
    print("4. Update Event")
    print("5. Mark Event Status")
    print("6. Delete Event")
    print("7. Search Event")
    print("8. View Upcoming Events")
    print("9. Exit")


while True:

    menu()

    choice = input("Choose option: ")

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
        manager.search_event()

    elif choice == "8":
        manager.upcoming_events()

    elif choice == "9":
        print("Goodbye")
        break

    else:
        print("Invalid option")