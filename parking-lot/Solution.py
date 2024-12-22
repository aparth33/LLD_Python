from ParkingFloor import ParkingFloor
from SearchManager import SearchManager
class Solution:
    
    def init(self, helper, parking: list):
        """
        Initialize the parking lot.

        :param helper: Helper for logging and utility functions.
        :param parking: 3D list representing the parking structure.
        """
        self.helper = helper
        #self.helper.println(f"solution class initialized, number of floors {len(parking)}")
        self.vehicle_types = [2, 4]
        self.floors = [ParkingFloor(i, parking[i], self.vehicle_types, helper) for i in range(len(parking))]
        self.search_manager = SearchManager()

    def park(self, vehicle_type: int, vehicle_number: str, ticket_id: str) -> str:
        """
        Assign an empty parking spot to a vehicle.

        :param vehicle_type: Type of the vehicle (2 or 4 for 2-wheeler or 4-wheeler).
        :param vehicle_number: Vehicle number.
        :param ticket_id: Ticket ID.
        :return: spot_id assigned to the vehicle
        """
        for floor in self.floors:
            result_spot_id = floor.park(vehicle_type, vehicle_number, ticket_id)
            if  result_spot_id != "" :
                self.search_manager.index( result_spot_id, vehicle_number, ticket_id)
                #print(f"vehicle parked {vehicle_number} in spot {result_spot_id}")
                return result_spot_id
        return ""

    def remove_vehicle(self, spot_id: str, vehicle_number: str, ticket_id: str) -> int:
        """
        Un-park a vehicle.

        :param spot_id: Spot ID of the vehicle.
        :param vehicle_number: Vehicle number.
        :param ticket_id: Ticket ID.
        :return: Status code indicating the result of the operation.
        """
        search_spot_id = spot_id if spot_id != "" else self.search_vehicle(vehicle_number, ticket_id)
        if search_spot_id == "" :
            return 404
            
        location = self.helper.get_spot_location(search_spot_id)
        if location[0]<0:
            return 404
        floor, row, col = location[0], location[1], location[2]
        removed= self.floors[floor].remove_vehicle(row, col)
        #print(f"vehicle {vehicle_number}, {ticket_id} removed from {search_spot_id}")
        return removed

    def get_free_spots_count(self, floor: int, vehicle_type: int) -> int:
        """
        Get the count of free spots for a specific vehicle type on a specific floor.

        :param floor: Floor number (0-indexed).
        :param vehicle_type: Type of the vehicle (2 or 4 for 2-wheeler or 4-wheeler).
        :return: Count of free spots.
        """
        if floor < 0 or floor >= len(self.floors):
            return 0
        return self.floors[floor].get_free_spots_count(vehicle_type)

    def search_vehicle(self, vehicle_number: str, ticket_id: str) -> str:
        """
        Search for a vehicle.

        :param spot_id: Spot ID of the vehicle.
        :param vehicle_number: Vehicle number.
        :param ticket_id: Ticket ID.
        :return: returns spot id for vehicle_number or ticket_id, (keeps and returns past spot_id record even after vehicle is removed)
        """
        return self.search_manager.search_vehicle(vehicle_number, ticket_id)
