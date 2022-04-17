class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages_count = photos_count // 4
        if photos_count % 4 != 0:
            pages_count += 1
        return cls(pages_count)

    def add_photo(self, label: str):
        for index, current_page in enumerate(self.photos):
            if len(current_page) < 4:
                current_page.append(label)
                return f"{label} photo added successfully on page {index + 1} slot {len(current_page)}"
        return "No more free slots"

    def display(self):
        matrix = []
        for row in self.photos:
            current_sheet = []
            for col in row:
                current_sheet.append(str([]))
            matrix.append(' '.join(current_sheet))

        result = []

        result.append("-----------")

        for row in matrix:
            result.append(row)
            result.append("-----------")

        return '\n'.join(result)

