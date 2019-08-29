

f = open('kbbi.csv', 'r')
inp = input("Cari suku kata apa")

l = f.readline()

while l:
  if l.split(',')[0].strip().endswith(inp):
    print(l.split(',')[0])
  l = f.readline()
