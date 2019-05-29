#with open('text.txt', 'w', encoding = 'utf-8') as f:
#    f.write('ывапбтлт лтлотлчп  длтдлчтдлпа\n khkl;lk\n')
with open('referat.txt', 'r', encoding = 'utf-8') as f:
#    text = f.read()
#    words = len(text.split(' '))
#    print(len(text), words)
    for l in f:
        l = l.replace('.', '!')
        with open('referat2.txt', 'a', encoding = 'utf-8') as ref2:
            ref2 .write(l)