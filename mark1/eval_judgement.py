import re

file_in = ['../'+i for i in filter(bool, open("in").read().split("\n"))]
words_list = filter(bool, open("in1").read().split("\n"))

essay_x = open('essay-x', 'w+')
essay_y = open('essay-y', 'w+')

l = []
for file_name in file_in:
    try:
        m = [0 for i in range(len(words_list))]
        f =  open(file_name).read().replace('\r', ' ').lower().replace('\n', ' ').replace('.',' ').replace('-', ' ').replace(',',' ').replace(":", " ").replace('`', ' ').replace('=',' ').replace('(', ' ').replace(')', ' ')
        for i in range(10):
            f = f.replace(str(i), '') 

        
        for index, word in enumerate(words_list):
            m[index] = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(' '+word+' '), f)) 

        l.append(m)
        essay_x.write(file_name)
        essay_x.write('\n')

    except:
        print file_name
        pass


for i in l:
    for j in i:
        essay_y.write(str(j))
        essay_y.write(' ')
    essay_y.write('\n')        

essay_x.close()
essay_y.close()
