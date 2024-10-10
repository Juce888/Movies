class Movie:
    def __init__(self, title, genre, director, year):
        # self.title = ['Frozen', 'Daddy Day Camp', 'Beauty And The Beast', 'Fast and Furious: Tokyo Drift']
        # Wasn't sure if you wanted me to pull from a pre-set list of movie titles or not
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year

    def check_for_title(self, title):
        if title == "":
            return "Movie Title cannot be empty."
        else:
            return title

    # def check_for_title(self, title):
    #     for title in self.title:
    #         if title != title:
    #             return "Movie Title cannot be empty."
    #         else:
    #             return title

