from stopwords import allStopWords
import mincemeat, glob, re

text_files = glob.glob('db/*')

autor = {}
info = {}
title = {}

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()

source = dict((file_name, file_contents(file_name)) for file_name in text_files)

def getAutores(line):
    autores = line.split("::")
    return autores; 

def cleanTitle(row_title):
    title = row_title.split(" ")
    for t in title:
        re.sub('^A-Za-z0-9]+', '', t)
    for k in allStopWords.keys():
        if k in title:
            title.remove(k)
    return title

def countTerms(autores, terms):
    for au in autores:
        for term in terms:
            if not au in autor.keys():
                autor[au] = {}
            if not term in autor[au].keys():
                autor[au][term] = 1
            else:
                autor[au][term] += 1

def mapfn(k, v):
    row = v.split(":::")
    info = row[0]
    title = row[2]
    autores = getAutores(row[1])
    terms = cleanTitle(title)


    countTerms(autores, terms)
    print autor

def reducefn(k, v):
    return null

for x,y in source.items():
    mapfn(x, y)

"""
s = mincemeat.server()
s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn


results = s.run_server(password="pass")
for k, v in resutls.items():
    print 'key: ' + k + 'value: ' + v
"""
