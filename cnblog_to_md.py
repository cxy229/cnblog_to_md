from bs4 import BeautifulSoup
from fun import month_transform

with open('/home/cxy229/Desktop/2.xml', 'rt') as f:
    data = f.read()

soup = BeautifulSoup(data, "html.parser")

lItem = soup.find_all('item')
count = 0
for i in lItem:
    title = ''
    title3 = i.title.text
    lDate = i.pubdate.text.split(',')[1].split(' ')
    title0 = lDate[3]
    title1 = month_transform(lDate[2])
    title2 = lDate[1]
    title = title0 + '-' + title1 + '-' + title2 + '-' + title3 + '.md'
    content = i.description.text
    path = '/home/cxy229/Desktop/1/'+title
    with open(path, 'wt') as f:
        f.write(content)
    print(title)
    count += 1

print('一共导出 %r 篇文章' % count)
