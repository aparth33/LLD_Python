from ParkingSpot import ParkingSpot
class ParkingFloor:
    def __init__(self, floor: int, parking_floor: list, vehicle_types: list, helper):
        """
        Initialize a parking floor.

        :param floor: Floor number.
        :param parking_floor: 2D list representing the parking floor.
        :param vehicle_types: List of vehicle types.
        :param helper: Helper for logging and utility functions.
        """
        self.parking_spots = [[None for _ in range(len(parking_floor[0]))] for _ in range(len(parking_floor))]
        self.free_spots_count = {vehicle_type: 0 for vehicle_type in vehicle_types}

        for row in range(len(parking_floor)):
            for col in range(len(parking_floor[row])):
                if parking_floor[row][col].endswith("1"):
                    vehicle_type = int(parking_floor[row][col].split("-")[0])
                    self.parking_spots[row][col] = ParkingSpot(helper.get_spot_id(floor, row, col), vehicle_type)
                    self.free_spots_count[vehicle_type] += 1

    def get_free_spots_count(self, vehicle_type: int) -> int:
        """
        Get the count of free spots for a specific vehicle type.

        :param vehicle_type: Type of the vehicle.
        :return: Count of free spots.
        """
        return self.free_spots_count.get(vehicle_type, 0)

    def remove_vehicle(self, row: int, col: int) -> int:
        """
        Un-park a vehicle.

        :param row: Row number.
        :param col: Column number.
        :return: Status code indicating the result of the operation.
        """
        if row < 0 or row >= len(self.parking_spots) or col < 0 or col >= len(self.parking_spots[0]) or not self.parking_spots[row][col].is_parked():
            return 404
        vehicle_type=self.parking_spots[row][col].get_vehicle_type()    
        self.parking_spots[row][col].remove_vehicle()
        self.free_spots_count[vehicle_type] += 1
        return 201

    def park(self, vehicle_type: int, vehicle_number: str, ticket_id: str) -> str:
        """
        Assign an empty parking spot to a vehicle.

        :param vehicle_type: Type of the vehicle.
        :param vehicle_number: Vehicle number.
        :param ticket_id: Ticket ID.
        :return: ParkingResult indicating the status of the operation.
        """
        if self.free_spots_count.get(vehicle_type, 0) == 0:
            return ""
        for row in self.parking_spots:
            for spot in row:
                if spot is not None and not spot.is_parked() and spot.get_vehicle_type() == vehicle_type:
                    self.free_spots_count[vehicle_type] -= 1
                    spot.park_vehicle()
                    return spot.get_spot_id()
        return ""
