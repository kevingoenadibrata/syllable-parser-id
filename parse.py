

def encode_sp(word):
  if len(word) < 2:
    return word

  newword = ""
  i = 0
  while i < len(word)-1:
    if word[i]+word[i+1] in sp_dict.keys():
      newword = newword + sp_dict[word[i] + word[i+1]]
      i = i + 2
    else:
      newword = newword + word[i]
      i = i + 1

  if i < len(word):
    newword = newword + word[-1]

  return newword

def parse_syl(word):
  a = []
  tex = ""
  for i in word:
    if i in vowels:
      if tex is not "":
        a.append(tex)
        tex = ""

      a.append(i)
    else:
      tex = tex + i
  if tex is not "":
    a.append(tex)
  return a

def define_type(a):
  typ = []
  for i in range(0, len(a)):
    # a[i] is a vowel
    if a[i] in vowels:
      typ.append(1)

    else:
      if i == 0 or i == len(a)-1:
        typ.append(0)
      else:
        typ.append(2)
  return typ

def cut_word(a, typ):
    for i in range(0, len(typ)):
        if typ[i] == 0:
            continue
        elif typ[i] == 1:
            if i-1 >= 0:
                if typ[i-1] == 1:
                    a[i] = "/" + a[i]
        elif typ[i] == 2:
            if len(a[i]) == 1:
                a[i] = "/" + a[i]
            else:
                a[i] = a[i][0] + "/" + a[i][1:]
    return "".join(a)


def decode_sp(word):
  decoded = ""
  for i in word:
    isSp = False
    for k,v in sp_dict.items():
      if v == i:
        decoded = decoded + k
        isSp = True

    if not isSp:
      decoded = decoded + i
  return decoded



def syllabize(word):
    print(word)
    spword = encode_sp(word)
    print(spword)
    arr =  parse_syl(spword)
    print(arr)
    typ = define_type(arr)
    print(typ)
    result = cut_word(arr, typ)
    print(result)
    decoded = decode_sp(result)
    print(decoded)
    return decoded

def singleinput():
  www = input("Word: ")
  syllabize(www)

def complete_file():
  f = open('kbbi_data.csv', 'r')
  w = open('kbbi.csv', 'w')
  l = f.readline()
  while l:
    word = l.split(",")[0].split("\t")[1].strip()
    vo = ""
    syll = syllabize(word)
    for c in word:
      if c in vowels:
        vo = vo + c

    w.write(word + "," + syll + "," + vo + "\n")
    l = f.readline()



vowels = ['a','i','u','e','o', '%', '^', '&', '*' ]
sp_dict = {}
sp_dict["ng"] = "!"
sp_dict["kh"] = "@"
sp_dict["ny"] = "#"
sp_dict["sy"] = "$"

sp_dict["ai"] = "%"
sp_dict["au"] = "^"
sp_dict["ei"] = "&"
sp_dict["oi"] = "*"

complete_file()
