try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import os
import json

topic = 'Array'
base = ''  # os.path.dirname(os.path.abspath(__file__))
html = open(os.path.join(base, '{}.html'.format(topic)))
soup = BeautifulSoup(html, 'html.parser')
filter = open(os.path.join(base, 'neverDoAgain.txt'))
filterIds = ""
for line in filter:
    filterIds += line

filterIds = set(filterIds.split(","))

# print(filterIds)
filter.close()
ttt = soup.body.find('table')

res = []
skip = True

tl = ttt.findAll('tr')
for trow in tl:

    if skip:
        skip = False
        continue
    link = trow.findAll("a")[0]['href']
    link = link.split("/")[-1]
    res.append(link)
    #print('"{}",'.format(link))
with open("{}.json".format(topic), "w") as write_file:
    json.dump(res, write_file)
"""
# %%

skip = True
for tr in tl:
    if skip:
        skip = False
        continue
    td = tr.findAll('td')
    level = td[4].text
    id_ = td[1].text
    id_ = "".join(id_.split())
    problem = td[2].text
    problem = " ".join(problem.split())
    if id_ not in filterIds:
        res.append("## {} {} [{}]\n\n```\n\n```\n---\n".format(id_, problem, level))

file = open('{}.md'.format(topic), 'w')  # write to file
file.write('# {}\n\n'.format(topic))
for line in res:
    file.write(line)

file.close()  # close file
html.close()
"""
