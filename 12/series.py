from media import Media

class Series(Media):
    def __init__(self, type, name, director, imdb_score, url, duration, casts, part_no):
        super().__init__(type, name, director, imdb_score, url, duration, casts)
        self.part_no = part_no 