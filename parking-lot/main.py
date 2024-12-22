from Solution import Solution
from Helper import Helper

def main():
    # Initialize a helper instance
    helper = Helper()

    # Define the parking structure: 2 floors, each with a 2x2 grid
    parking_structure = [
        [["2-1", "2-1"], ["4-1", "4-1"]],  # Floor 0
        [["2-1", "4-1"], ["4-1", "2-1"]],  # Floor 1
    ]

    # Initialize the parking lot solution
    parking_lot = Solution()
    parking_lot.init(helper, parking_structure)

    # Test 1: Park a two-wheeler
    vehicle_type = 2
    vehicle_number = "TW1234"
    ticket_id = "T1"
    spot_id = parking_lot.park(vehicle_type, vehicle_number, ticket_id)
    print(f"Parked two-wheeler {vehicle_number} at spot: {spot_id}")

    # Test 2: Park a four-wheeler
    vehicle_type = 4
    vehicle_number = "FW5678"
    ticket_id = "T2"
    spot_id = parking_lot.park(vehicle_type, vehicle_number, ticket_id)
    print(f"Parked four-wheeler {vehicle_number} at spot: {spot_id}")

    # Test 3: Get the count of free spots for two-wheelers on floor 0
    free_spots = parking_lot.get_free_spots_count(0, 2)
    print(f"Free two-wheeler spots on floor 0: {free_spots}")

    # Test 4: Remove a vehicle
    remove_status = parking_lot.remove_vehicle(spot_id, "FW5678", "T2")
    print(f"Remove vehicle status: {remove_status}")

    # Test 5: Search for a vehicle
    searched_spot_id = parking_lot.search_vehicle("TW1234", "T1")
    print(f"Vehicle TW1234 found at spot: {searched_spot_id}")


if __name__ == "__main__":
    main()
