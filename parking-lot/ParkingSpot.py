class ParkingSpot:
    def __init__(self, spot_id: str, vehicle_type: int):
        """
        Initialize a parking spot.

        :param spot_id: Spot ID.
        :param vehicle_type: Type of the vehicle.
        """
        self.spot_id = spot_id
        self.vehicle_type = vehicle_type
        self.is_spot_parked = False

    def is_parked(self) -> bool:
        """
        Check if a vehicle is parked in this spot.

        :return: True if a vehicle is parked, False otherwise.
        """
        return self.is_spot_parked

    def park_vehicle(self):
        """
        Park a vehicle in this spot.
        """
        self.is_spot_parked = True

    def remove_vehicle(self):
        """
        Remove a vehicle from this spot.
        """
        self.is_spot_parked = False

    def get_spot_id(self) -> str:
        """
        Get the spot ID.

        :return: Spot ID.
        """
        return self.spot_id

    def get_vehicle_type(self) -> int:
        """
        Get the vehicle type.

        :return: Vehicle type.
        """
        return self.vehicle_type
