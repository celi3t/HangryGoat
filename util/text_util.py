

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

