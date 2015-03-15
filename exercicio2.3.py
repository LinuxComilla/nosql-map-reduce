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
        authors = functions.count(authors, terms)
        yield authors, 1

def reducefn(k, v):
    print("reduce " + v)
    return v

s = mincemeat.Server()
s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results =  s.run_server(password="nosql")
for k, v in resutls.items():
    var = 'key: ' + k + 'value: ' + v
    print(var)
