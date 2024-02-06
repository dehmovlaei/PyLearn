import sqlite3
class Store:
    def show_menu(self):
        print('1- Add\n2- Edit\n3- Remove\n4- Search\n5- Show List\n6- Exit')
    def load_database(self):
        global con, cur
        con = sqlite3.connect("media.db")
        cur = con.cursor()

    def show_list(self):
        result = cur.execute("SELECT * FROM medias")
        medias = result.fetchall()
        for media in medias:
            print(media)

    def user_input(self):
        self.type = input("what kind of movie you want to add(film/series/documentary...")
        self.name = input("Enter name of movie ")
        self.director = input("Enter name of director  ")
        self.imdb_score = input("Enter imdb SCORE  ")
        self.url = input("Enter url for download  ")
        self.duration = input("Enter duration in minutes  ")
        self.casts = input("Enter casts  ")
    def add(self):
        self.user_input()
        cur.execute(f"INSERT INTO medias(type, name, director, imdb_score, url, duration, casts)"
                    f"VALUES('{self.type}','{self.name}','{self.director}','{self.imdb_score}','{self.url}','{self.duration}','{self.casts}')")
        con.commit()
        print("successfully added...")

    def edit(self):
        id = input("Enter movie id  ")
        self.user_input()
        cur.execute(f"UPDATE medias SET type='{self.type}', name='{self.name}', director='{self.director}', imdb_score='{self.imdb_score}',"
                    f"url='{self.url}', duration='{self.duration}', casts='{self.casts}' WHERE id={id}")
        con.commit()
        print("successfully edited...")
        self.show_list()

    def remove(self):
        id = input("Enter movie id  ")
        cur.execute(f"DELETE FROM medias WHERE id='{id}'")
        con.commit()
        print("successfully deleted...")
        self.show_list()

    def search(self):
        t1 = input("Enter minimum duration of movie ")
        t2 = input("Enter maximum duration of movie ")
        result = cur.execute(f"SELECT * FROM medias WHERE duration>'{t1}' and duration<'{t2}'")
        medias = result.fetchall()
        for media in medias:
            print(media)

store = Store()
store.load_database()

while True:
    print('========================================================')
    print('WELCOME TO MOVIE STORE')
    store.show_menu()
    user_select = int(input('HOW CAN I HELP YOU?\n'))
    print('========================================================')

    match user_select:
        case 1:
            store.add()
        case 2:
            store.edit()
        case 3:
            store.remove()
        case 4:
            store.search()
        case 5:
            store.show_list()
        case 6:
            exit(0)