class Airline:

    def __init__(self, flight, day, destination, airline, time, gate, terminal):
        self.flight_airline = flight
        self.day_airline = day
        self.destination_airline = destination
        self.airline_airline = airline
        self.time_airline = time
        self.gate_airline = gate
        self.terminal_airline = terminal

    def __repr__(self):
        return f'{self.flight_airline} {self.airline_airline} - {self.destination_airline}'

    def get_flight(self):
        return self.flight_airline

    def get_day(self):
        return self.day_airline

    def get_destination(self):
        return self.destination_airline

    def get_airline(self):
        return self.airline_airline

    def get_time(self):
        return self.time_airline

    def get_gate(self):
        return self.gate_airline

    def get_terminal(self):
        return self.terminal_airline

    def info(self):
        print(f'Flight: {self.get_flight()}')
        print(f'Day {self.get_day()}')
        print(f'Destination: {self.get_destination()}')
        print(f'Airline: {self.get_airline()}')
        print(f'Time: {self.get_time()}')
        print(f'Gate: {self.get_gate()}')
        print(f'Terminal: {self.get_terminal()}')
        print('')


class Airport:

    def __init__(self):
        self.__flights = []

    def show_all_flights(self):
        print(self.__flights)

    def add_flight(self, new_flight):
        self.__flights.append(new_flight)

    def search_destination_airline(self, destination_point):
        for item in self.__flights:
            if item.get_destination().lower() == destination_point.lower():
                item.info()

    def search_day_airline(self, day):
        for item in self.__flights:
            if item.get_day().lower() == day.lower():
                item.info()


if __name__ == '__main__':
    flights_data = [('LO 3906', 'sun', 'Bodrum', 'LOT Polish', '6:49', '11a', 'A'),
                    ('LH 1367', 'tue', 'Dubai', 'Lufthansa', '7:10', '33', 'D'),
                    ('OS 598', 'wed', 'Amsterdam', 'Austrian', '7:40', '5s', 'B'),
                    ('EZY 3816', 'mon', 'Pisa', 'EasyJet', '19:30', '3', 'C'),
                    ('TA 4556', 'fri', 'Istanbul', 'Turkish Airlines', '5:55', '1', 'A'),
                    ('EM 5936', 'sat', 'Bali', 'Emirates', '12:10', '14', 'F'),
                    ('QA 5229', 'thu', 'Kuala lumpur', 'Qatar Airways', '22:40', '21', 'G'),
                    ('DY 3561', 'sun', 'New York', 'Air Canada', '18;15', '41', 'B'),
                    ('GH 178', 'fri', 'Minsk', 'Aeroflot', '23:20', '24', 'C'),
                    ('E 3117', 'wed.', 'Kiev', 'Belavia', '00:45', '5', 'A'),
                    ('NN 1264', 'sat', 'Paris', 'British Airways', '4:35', '8', 'F'),
                    ('R 3715', 'sun', 'Busan', 'Korean Air', '8:50', '13c', 'B'),
                    ('BT 7412', 'mon', 'Dresden', 'Ryanair', '10:00', '18', 'G'),
                    ('DP 811', 'thu', 'Hong Kong', 'Air China', '11:45', '8', 'A')]

    airport = Airport()
    for flight in flights_data:
        airport.add_flight(Airline(*flight))

    airport.show_all_flights()

    airport.search_day_airline(input('Select day: \n'))
    airport.search_destination_airline(input('Select destination from: \n'))