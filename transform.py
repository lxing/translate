# PA7
# alexchia, lxing
#
import sys

def mt_transform(infile):
    fi = open(infile, "r");
    data = fi.readlines();
    fi.close();
    answer = []
    
    # transform sentence
    for sentence in data:
        sentence = [tuple(token.split('/')) for token in sentence.strip().split(' ')];
        
        # Reordering rules
        
        # 1. Delete repeated words
        # 2. Replace 'Word1/NN of/IN' with "word1's"
        # 3. (adj/adverb+number) directly after a noun - bring it before the previous preposition
        
        result = []
        prevword = ""
        prevtag = ""
        for word, tag in sentence:
            no_append = False
            # Delete repeated words
            if prevword == word:
                continue
                
            if word == 'of' and tag == 'IN':
                # check if prev word is noun
                if prevtag == 'NN' or prevtag == 'NNP':
                    result[-1] = result[-1] + "'s"
                    no_append = True
                elif prevtag == 'NNS' or prevtag == 'NNPS':
                    result[-1] = result[-1] + "s'"
                    no_append = True
                    
            
            
            prevword = word
            prevtag = tag
            if not no_append:
                result.append(word)
        answer.append(' '.join(result))
    return answer

if __name__ == '__main__':
  print mt_transform(sys.argv[1])