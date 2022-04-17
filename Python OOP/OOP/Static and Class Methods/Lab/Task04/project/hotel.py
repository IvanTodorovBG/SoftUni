from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        new_name = f"{stars_count} stars Hotel"
        return cls(new_name)

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for current_room in self.rooms:
            if current_room.number == room_number:
                result = current_room.take_room(people)
                if not result:
                    self.guests += people

    def free_room(self, room_number):
        for current_room in self.rooms:
            if current_room.number == room_number:
                self.guests = 0
                current_room.free_room()

    def status(self):
        free_rooms = [str(current_room.number) for current_room in self.rooms if not current_room.is_taken]
        taken_rooms = [str(current_room.number) for current_room in self.rooms if current_room.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" +\
            f"Free rooms: {', '.join(free_rooms)}\n" +\
            f"Taken rooms: {', '.join(taken_rooms)}"






