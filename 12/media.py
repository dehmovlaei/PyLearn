from pytube import YouTube

MEDIA_LIST = []


class Media:
    def __init__(self, type, name, director, imdb_score, url, duration, casts):
        self.type = type
        self.name = name
        self.director = director
        self.imdb_score = imdb_score
        self.url = url
        self.duration = duration
        self.casts = casts

    @staticmethod
    def show_info(media_name):
        for obj in MEDIA_LIST:
            if obj.name == media_name:
                print(
                    f'type: {obj.type}\nname: {obj.name}\nDirector: {obj.director}\nImdb_score: {obj.imdb_score}\nUrl: {obj.url}\nDuration: {obj.duration}\ncasts: {obj.casts}\n=======================\n'
                )
        else:
            print('Media not found...!')

    @staticmethod
    def download(media_name):
        for obj in MEDIA_LIST:
            if obj.name == media_name:
                link = obj.url
                first_stream = YouTube(link).streams.first()
                first_stream.download(output_path='./', filename=f'{obj.name}.mp4')