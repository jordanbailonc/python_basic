class Counter_vowels():
    def __init__(self,sentence) -> None:
        self.sentence=sentence

    def do_strip(self):
        aux= self.sentence
        aux=aux.casefold()
        free_text= aux.replace(" ","")
        return free_text

    def get_results(self):
        aux=['a','e','i','o','u']
        my_source= self.do_strip()
        counts = {i:0 for i in aux}
        for char in my_source:
            if char in counts:
                counts[char] +=1

        for x,y in counts.items():
            print(x,y)

    
try:
    words = input('Write the sentence to count the  vowels:\t')
    my_counter=Counter_vowels(words)
    clean_content = my_counter.do_strip()
    my_len= len(clean_content)
    my_counter.get_results()
except Exception as ex:
    print(ex)