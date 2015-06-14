from stemming.porter2 import stem
import string

class TextUtil():
    
    
    @staticmethod
    def to_utf8(string):
        return string.encode('utf-8', 'replace')


    @staticmethod
    def unpack_list(l, ):
        if l == None:
            return ""
        elif isinstance(l, basestring):
            return TextUtil.to_utf8(l) + ','
        elif isinstance(l, list):
            temporary = ""
            for element in l:
                temporary += TextUtil.unpack_list(element) 
            return temporary
        else:
            return str(l) + ','
        
            
    @staticmethod
    def to_lower_case(string):
        return string.lower()
        
        
    @staticmethod
    def eliminate_punctuation(one_string):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in one_string if ch not in exclude)
    
      
    @staticmethod
    def single_word_vectorizer(string, unique = True, stemming = True):  
        words_vector = list()
        for line in string.split('\n'):
            for subline in line.split(','):
                for word in subline.split(' '):
                    if len(word) > 3:
                        if stemming:
                            word = stem(word)
                        words_vector.append(word)
        if unique:
            return set(words_vector)
        else:
            return words_vector

    
    @staticmethod
    def list_contains(word, food_words_set):
        return word in food_words_set
        
        
    @staticmethod    
    def make_lowercase_word_vector(string):
        #string = TextUtil.to_utf8(string)
        string = TextUtil.to_lower_case(string)
        string = TextUtil.eliminate_punctuation(string)
        words = TextUtil.single_word_vectorizer(string)
        print "tot parsed words: ", len(words)
        return words
    

                
if __name__ == '__main__':
    l1 = ['a', 'b']
    l2 = 'stringa'
    l3 = ['one', 'two', 'three', ['d', 'f']]
    l4 = [11,25,3, ""]
    l5 = []
    l6 = None
    
    test_lists = [l1, l2, l3, l4, l5, l6]
    print TextUtil.unpack_list(test_lists)
    print TextUtil.unpack_list(l2)
    print TextUtil.unpack_list(3)
    
    # some_text = open('/Users/celi/Desktop/foods.txt', 'r').read()
    # TextUtil.make_lowercase_word_vector((some_text)

