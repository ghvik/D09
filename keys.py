"""
Write three functions:
sort1(langauges)
sort2(languages)
sort3(langauges)
Goal: Print exactly the below w/ three functions:
1:
    Arabic
    English
    Koine Greek
    Latin
    Romanian
    C++
    JavaScript
    Python
    R
2:
    R
    C++
    Latin
    Arabic
    Python
    English
    Romanian
    JavaScript
    Koine Greek
3:
    JavaScript
    R
    Latin
    Python
    Romanian
    Koine Greek
    English
    Arabic
    C++
"""
languages = {'JavaScript': 'P',
             'Arabic': 'N',
             'R': 'P',
             'Python': 'P',
             'C++': 'P',
             'Koine Greek': 'N',
             'Latin': 'N',
             'Romanian': 'N',
             'English': 'N'}
print(sorted(languages))
# __getitem__ returns the value of d[key]
print(sorted(sorted(languages), key=languages.__getitem__))
print(sorted(languages, key=len))

def sort1b(d):
    import operator
    # itemgetter acts on a list of tuples
    lst = sorted(sorted(d.items()), key=operator.itemgetter(1))
    print("1:")
    for language,t in lst:
        print("\t"+language)

#def last_letter(item):
#   pass
    #return item[-1]
sort1b(languages)
