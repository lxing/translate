# PA7
# alexchia, lxing
#
import sys

def mt_transform(infile):
    fi = open(infile, "r");
    data = fi.readlines();
    fi.close();
    answer = []

    ADV = ['RB','RBR','RBS']
    ADJ = ['JJ','JJR','JJS']
    NOUNS = ['NN','NNS','NNP','NNPS']
    VERBS = ['VBD','VBG','VBN','VBP','VBZ']
    
    # transform sentence
    for sentence in data:
        sentence = [tuple(token.split('/')) for token in sentence.strip().split(' ')];
        
        # Reordering rules
        
        # 1. Delete repeated words
        # 2. Replace 'Word1/NN of/IN' with "word1's"
        # 3. (adj/adverb+number) directly after a noun - bring it
        #    before the previous preposition or the noun if the previous prep. is too far back
        
        result = []
        result_tags = []
        prevword = ""
        prevtag = ""

        for word, tag in sentence:
            no_append = False
            # 1. Delete repeated words
            if prevword == word:
                continue
                
            if word == 'of' and tag == 'IN':
                # 2. check if prev word is noun, don't append and add 's to prev word if so
                if prevtag in ['NN','NNP']:
                    result[-1] = result[-1] + "'s"
                    no_append = True
                elif prevtag in ['NNS', 'NNPS']:
                    result[-1] = result[-1] + "s'"
                    no_append = True
                    
            if tag == 'CD':
                # 3. check if right before a noun
                noun_before = False
                for j in range(1, len(result)+1):
                    if result_tags[-j] in NOUNS:
                        noun_before = True
                        break
                    # if not adverb or adj break
                    elif result_tags[-j] not in ADJ + ADV:
                        break
                
                if noun_before:
                    # bring everything after the noun to before the prev preposition / noun
                    prev_noun_pos = j
                    prev_prop_pos = -1
                    same_noun = True
                    for k in range(j+1, len(result)+1):
                        if same_noun and result_tags[-k] in NOUNS:
                            prev_noun_pos = k
                        else:
                            same_noun = False
                        if result_tags[-k] == 'IN':
                            prev_prop_pos = k
                            break
                        # too far back
                        if k - j + 1 > 4:
                            break
                    
                    if prev_prop_pos != -1:
                        k = prev_prop_pos
                    else:
                        k = prev_noun_pos
                    
                    # bring words to in front of that position k
                    for m in range(j-1):
                        old_r = result.pop()
                        old_tag = result_tags.pop()
                        result.insert(-k+m+1, old_r)
                        result_tags.insert(-k+m+1, old_tag)
                        
                    # finally append word to that position
                    result.insert(-k+m+1, word)
                    result_tags.insert(-k+m+1, tag)
                    no_append = True
            
            # 4. discard additional 'to' between verb and objects, eg 'kan dao ta' => 'saw to him' => 'saw him'
            OBJ = NOUNS + ADJ + ADV + ['CD']
            if tag in OBJ and len(result) > 1 and result_tags[-1] == 'TO' and result_tags[-2] in VERBS:
                result = result[:-1]
            
            # 5. remove verbs in a row, since these tend to be the product of one Chinese multi-char verb converted
            # to multiple English verbs. use the last verb in the sequence since this usually most semantically
            # meaningful
            if tag in VERBS and prevtag in VERBS:
                result = result[:-1]
                result_tags = result_tags[:-1]
            
            prevword = word
            prevtag = tag
            if not no_append:
                result.append(word)
                result_tags.append(tag)

        answer.append(' '.join(result))
    return answer

if __name__ == '__main__':
  for sentence in mt_transform(sys.argv[1]):
    print sentence + '\n'