from media import *
import actor
import clip
import documentary
import film
import series


class Database:
    def read(self):
        data = open('12\database.txt', 'r')
        for line in data:
            detail = line.split(',')
            my_obj = Media(
                detail[0],
                detail[1],
                detail[2],
                detail[3],
                detail[4],
                detail[5],
                detail[6],
            )
            MEDIA_LIST.append(my_obj)
        data.close()

    def write(self):
        data = open('12\database.txt', 'w')
        for obj in MEDIA_LIST:
            result = f'{obj.type},{obj.name},{obj.director},{obj.imdb_score},{obj.url},{obj.duration},{obj.casts}'
            data.write(result)


class Store:

    @staticmethod
    def show_menu():
        print('1- Add')
        print('2- Edit')
        print('3- Remove')
        print('4- Search')
        print('5- Show List')
        print('6- Show Info')
        print('7- Download')
        print('8- Exit')

    @staticmethod
    def add():
        type = input('media type: ')
        name = input('media name: ')
        director = input('director name: ')
        imdb_score = input('imdb score: ')
        url = input('url address: ')
        duration = input('duration time: ')
        casts = input('casts list: ')
        new_media = Media(type, name, director, imdb_score, url, duration, casts)
        MEDIA_LIST.append(new_media)
        print('your media successfully added')

    def edit(self,cur_name, new_name):
        for obj in MEDIA_LIST:
            if obj.name == cur_name:
                obj.name = new_name

    @staticmethod
    def remove(media_name):
        i = 0
        for obj in MEDIA_LIST:
            if obj.name == media_name:
                obj.pop(i)
                print('successfully removed')
            else:
                i += 1
        else:
            print('not found!!!')

    @staticmethod
    def search(search_value):
        for obj in MEDIA_LIST:
            if (obj.name == search_value):
                print(f'type: {obj.type}\nname: {obj.name}\nDirector: {obj.director}\nImdb_score: {obj.imdb_score}\nUrl: {obj.url}\nDuration: {obj.duration}\ncasts: {obj.casts}\n========================================================\n')
        else:
            print('Media not found...!')

    @staticmethod
    def show_list():
        for obj in MEDIA_LIST:
            print(f'type: {obj.type}\nname: {obj.name}\nDirector: {obj.director}\nImdb_score: {obj.imdb_score}\nUrl: {obj.url}\nDuration: {obj.duration}\ncasts: {obj.casts}\n========================================================\n')


print('WELCOME TO MOVIE STORE')
db = Database()
db.read()
store = Store()

while True:
    print('========================================================')
    Store.show_menu()
    user_select = int(input('HOW CAN I HELP YOU?\n'))
    print('========================================================')

    match user_select:
        case 1:
            Store.add()

        case 2:
            cur_name = input('current name:\n')
            new_name = input('new name:\n')
            store.edit(cur_name, new_name)

        case 3:
            media_name = input('name of movie that you want to remove:\n')
            store.remove(media_name)

        case 4:
            search_value = input('name of movie that you want to find:\n')
            store.search(search_value)

        case 5:
            Store.show_list()

        case 6:
            media_name = input('name of movie that you want to show:\n')
            Media.show_info(media_name)

        case 7:
            media_name = input('name of movie that you want to download:\n')
            Media.download(media_name)

        case 8:
            db.write()
            exit(0)