import datetime


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        split_date = date.split(".")
        year = int(split_date[2])
        month = int(split_date[1])
        day = int(split_date[0])
        time = datetime.datetime(year, month, day)
        year = time.strftime("%Y")
        month = time.strftime("%B")
        day = time.strftime("%d")
        return cls(name, id, int(year), month, age_restriction)

    def __repr__(self):
        if self.is_rented:
            status = "rented"
        else:
            status = "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})" \
               f" has age restriction {self.age_restriction}. Status: {status}"

