"""
Module for showing how wikipedia library works
"""
import wikipedia


def func():
    """
    Testing function
    """
    for title in wikipedia.search(FIND, results=5, suggestion=True):
        print(title)

    print(wikipedia.suggest(WRONG))
    print(wikipedia.summary(FIND))

    wikipedia.set_lang(LANGUAGE)
    print(wikipedia.summary(FIND))

    print(wikipedia.summary(CITY))


if __name__ == "__main__":
    FIND = "Coronavirus"
    WRONG = 'Coronavir'
    CITY = "London"
    LANGUAGE = "uk"
    func()
