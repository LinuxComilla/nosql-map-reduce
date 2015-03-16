from stopwords import allStopWords
import re

def getAuthors(line):
    authors = line.split("::")
    return authors

def cleanTitle(row_title):
    titles = row_title.split(" ")
    for index, title in enumerate(titles):
        titles[index] =  re.sub('[^A-Za-z0-9]+', '', title)
    for word in allStopWords.keys():
        if word in titles:
            titles.remove(word)
    return titles

def count(author, terms, countable = {}):
    if (isinstance(terms[0], list)):
        for term in terms:
            count(author, term)
    else:
        if not author in countable.keys():
            countable[author] = {}
        for term in terms:
            if not term in countable[author].keys():
                countable[author][term] = 1
            else:
                countable[author][term] += 1
    return countable[author]