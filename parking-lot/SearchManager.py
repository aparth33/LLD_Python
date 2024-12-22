class SearchManager:
    def __init__(self):
        """
        Initialize the search manager.
        """
        self.cache = {}

    def search_vehicle(self, vehicle_number: str, ticket_id: str) -> str:
        """
        Search for a vehicle.

        :param vehicle_number: Vehicle number.
        :param ticket_id: Ticket ID.
        :return: ParkingResult indicating the result of the search.
        """
        if vehicle_number.strip():
            return self.cache.get(vehicle_number)
        if ticket_id.strip():
            return self.cache.get(ticket_id)
        return ""

    def index(self, spot_id, vehicle_number, ticket_id):
        self.cache[vehicle_number] = spot_id
        self.cache[ticket_id] = spot_id
