class Comics:
    all_comics= []
    def __init__(self, title, issue_number, genre, authors):
        self.title = title
        self.isn = issue_number
        self.genre = genre
        self.authors = authors
        self.version = 1
        Comics.all_comics.append(self)

    def change_genre(self, genre):
        self.genre = genre

    def go_to_page(self, num):
        print(f'Going to page {num}')
    
    def version_change(self, version_number):
        self.version = version_number

    def print_comic(self):
        print(f'title = {self.title},\nissue_number = {self.isn},\ngenre = {self.genre},\nauthors = {self.authors},\nversion = {self.version}')

    @classmethod
    def print_all_comics(cls):
        for idhar in cls.all_comics:
            print('***************************************')
            idhar.print_comic()

godzilla = Comics('Godzilla', 5, 'Big Scary Dinasour', 'Japan')
spider_man = Comics('spider_man', 1, 'guy gets bit by spider', 'Stan Lee')
ironman = Comics('Iron Man',6,'action','Stan Lee')
# godzilla_dictionary = {
#         "title" : "Godzilla",
#         "issue_number":5,
#         "genre": "Big Scary Dinasour",
#         "authors": "Japan"
# }

# print(godzilla)
# print(godzilla_dictionary)
# godzilla.change_genre("Action")
# # print(godzilla.genre)
# # godzilla.go_to_page(49)
# godzilla.version_change(2)
# # print(godzilla.version)
# godzilla.print_comic()
# spider_man = Comics()
# dragon_ball_z = Comics()
# spider_man.read_comic()
Comics.print_all_comics()