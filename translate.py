import sys, urllib2, json

# note the api key is 412ca
translate_url = 'http://api.wordreference.com/412ca/json/zhen/'

# Translate a chinese character to the nearest english word
def translate_char(char):
  response = urllib2.urlopen(translate_url + char)
  raw_data = response.read()
  print raw_data
  data = json.loads(raw_data)

  top_term = data['term0']
  if top_term.has_key('PrincipalTranslations'):
    translation = top_term['PrincipalTranslations']['0']['FirstTranslation']['term]']
  elif top_term.has_key('Entries'):
    translation = top_term['Entries']['0']['FirstTranslation']['term']
  elif top_term.has_key('OtherSideEntries'):
    translation = top_term['OtherSideEntries']['0']['OriginalTerm']['term']

  return translation.split(',')[0]

def tag_word()

if __name__ == '__main__':
  print translate_char(sys.argv[1])