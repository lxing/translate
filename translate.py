import sys, string, os

space = ' '
outfilename = 'translated_data'
tagfilename = 'tagged_data'

def translate_file(fname):
  space = ' '

  dictionary = {}
  dictfile = open('dictionary')
  for entry in dictfile.readlines():
    zh = entry.split(' ')[0]
    en = space.join(entry.split(' ')[1:]).strip()
    dictionary[zh] = en

  infile = open(fname)
  outfile = open(outfilename, 'w')
  for sentence in infile.readlines():
    outsent = []
    for word in sentence.split(' '):
      word = word.strip()
      if word in dictionary:
        outsent.append(dictionary[word])
      else:
        print word, 'not found in dictionary'
        outsent.append(word)
    outfile.write(space.join(outsent) + ' .\n')

if __name__ == '__main__':
  translate_file(sys.argv[1])
  os.chdir('tagger')
  print os.getcwd()
  os.system('./stanford-postagger.sh models/english-bidirectional-distsim.tagger ../translated_data > ../tagged_data')