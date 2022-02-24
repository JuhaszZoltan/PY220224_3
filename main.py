import module as m

diakok = []

for sor in open("diakok.txt", encoding='utf-8'):
    diakok.append(m.Diak(sor))

print(diakok[0].nem)