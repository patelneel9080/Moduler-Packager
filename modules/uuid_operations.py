
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
        selection = int(input("Enter namespace choice: "))
        name = input("Enter a name for the UUID: ")
        
        namespaces = {
            1: uuid.NAMESPACE_DNS,
            2: uuid.NAMESPACE_URL,
            3: uuid.NAMESPACE_OID,
            4: uuid.NAMESPACE_X500
        }
        
        match selection:
            case 1 | 2 | 3 | 4:
                custom_uuid = uuid.uuid5(namespaces[selection], name)
                print("Generated Custom UUID:", custom_uuid)
            case _:
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
            selection = int(input("Enter your choice: "))
            
            match selection:
                case 1:
                    generate_uuid1()
                case 2:
                    generate_uuid4()
                case 3:
                    generate_custom_uuid()
                case 4:
                    break
                case _:
                    print("Invalid choice. Please try again.")
        
        except ValueError:
            print("Please enter a valid number.")
