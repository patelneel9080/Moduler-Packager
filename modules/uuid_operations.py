# modules/uuid_operations.py
import uuid

def generate_uuid1():
    uuid1 = uuid.uuid1()
    print("Generated UUID1:", uuid1)
    print("UUID1 Details:")
    print(f"Time Low: {uuid1.time_low}")
    print(f"Time Mid: {uuid1.time_mid}")
    print(f"Time Hi Version: {uuid1.time_hi_version}")
    print(f"Clock Sequence: {uuid1.clock_seq}")
    print(f"Node: {uuid1.node}")

def generate_uuid4():
    uuid4 = uuid.uuid4()
    print("Generated UUID4:", uuid4)
    print("Note: UUID4 is completely random and contains no network/hardware info")

def generate_custom_uuid():
    print("UUID Namespace Options:")
    print("1. DNS Namespace")
    print("2. URL Namespace")
    print("3. OID Namespace")
    print("4. X500 Namespace")
    
    try:
        choice = int(input("Enter namespace choice: "))
        name = input("Enter a name for the UUID: ")
        
        namespaces = {
            1: uuid.NAMESPACE_DNS,
            2: uuid.NAMESPACE_URL,
            3: uuid.NAMESPACE_OID,
            4: uuid.NAMESPACE_X500
        }
        
        if choice in namespaces:
            custom_uuid = uuid.uuid5(namespaces[choice], name)
            print("Generated Custom UUID:", custom_uuid)
        else:
            print("Invalid namespace choice.")
    except ValueError:
        print("Please enter a valid choice.")

def uuid_menu():
    while True:
        print("\n--- Generate Unique Identifiers (UUID) ---")
        print("1. Generate UUID1 (timestamp and MAC)")
        print("2. Generate UUID4 (random)")
        print("3. Generate Custom UUID")
        print("4. Back to Main Menu")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                generate_uuid1()
            elif choice == 2:
                generate_uuid4()
            elif choice == 3:
                generate_custom_uuid()
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")
        
        except ValueError:
            print("Please enter a valid number.")