from stopwords import allStopWords
import re

def getAuthors(line):
    authors = line.split("::")
    return authors

def cleanTitle(row_title):
    title = row_title.split(" ")
    for t in title:
        re.sub('^A-Za-z0-9]+', '', t)
    for k in allStopWords.keys():
        if k in title:
            title.remove(k)
    return title

def count(authors, terms):
    author = {}
    for au in authors:
        for term in terms:
            if not au in author.keys():
                author[au] = {}
            if not term in author[au].keys():
                author[au][term] = 1
            else:
                author[au][term] += 1
    return author