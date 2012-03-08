import sys

def transform_sentence(sentence):
  sentence = [token.split('/') for token in sentence.split(' ')]
  print sentence

def transform_file(filename):
  for line in open(filename).readlines():
    transform_sentence(line)

if __name__ == '__main__':
  transform_file(sys.argv[1])