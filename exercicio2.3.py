import mincemeat, glob

text_files = glob.glob('db/*')

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()

source = dict((file_name, file_contents(file_name)) for file_name in text_files)

def mapfn(k, v):
    import functions
    for line in v.splitlines():
        row = line.split(":::")
        authors = functions.getAuthors(row[1])
        terms = functions.cleanTitle(row[2])
        for author in authors:
            yield author, terms

def reducefn(author, terms):
    import functions
    list = functions.count(author, terms)
    if author in ['Grzegorz Rozenberg','Philip S. Yu']:
        print(author)
        print(list)
    return list

s = mincemeat.Server()
s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results =  s.run_server(password="nosql")
for k, v in results.items():
    print(k)
    print(v)
