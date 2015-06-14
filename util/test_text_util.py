# This Python file uses the following encoding: utf-8

import unittest
from text_util import TextUtil

class TestTextUtil(unittest.TestCase):
    
    def test_to_utf8(self):
        one_string = u'la vita \u00E8 bella'
        self.assertEquals('la vita è bella', TextUtil.to_utf8(one_string))
        
    
    def test_unpack_list(self):
        l1 = ['a', 'b']
        l2 = 'stringa'
        l3 = ['one', 'two', 'three', ['d', 'f']]
        l4 = [11,25,3, ""]
        l5 = []
        l6 = None
        
        test_lists = [l1, l2, l3, l4, l5, l6]
        
        self.assertEquals('a,b,stringa,one,two,three,d,f,11,25,3,,', TextUtil.unpack_list(test_lists))
        self.assertEquals(l2+"," , TextUtil.unpack_list(l2))
        self.assertEquals('3,', TextUtil.unpack_list(3))
        
    def test_to_lower_case(self):
        self.assertEquals('pizza', TextUtil.to_lower_case("PIZZA"))
        self.assertEquals('pizza', TextUtil.to_lower_case("PizZA"))
        self.assertEquals('pizza', TextUtil.to_lower_case("pizza"))
        
    
    def test_eliminate_punctuation(self):
        self.assertEquals('PIZZApizza', TextUtil.eliminate_punctuation("PIZZA.pizza"))
        self.assertEquals('PIZZApizza', TextUtil.eliminate_punctuation("PIZZApizza"))
        self.assertEquals('PIZZApizza', TextUtil.eliminate_punctuation(";;;;;.,,PIZZA;',;pizza"))
        
    def test_single_word_vectorizer(self):
        text = 'Then, call someone you love'
        text_vector = set(['Then', 'call', 'someon', 'love'])
        self.assertEquals(text_vector, TextUtil.single_word_vectorizer(text))
        
        text = 'Then, call someone you love Then call love, pizza'
        text_vector = set(['Then', 'call', 'someon', 'love', 'pizza'])
        self.assertEquals(text_vector, TextUtil.single_word_vectorizer(text))
        
    def test_make_lowercase_word_vector(self):
        text = 'Then, call someone you lovE then call love, pizza'
        text_vector = set(['then', 'call', 'someon', 'love', 'pizza'])
        self.assertEquals(text_vector, TextUtil.make_lowercase_word_vector(text))
        
        
        
        