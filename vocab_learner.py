import random
from readfile.formatting import *
from readfile.read_file import *

file, target = ReadFile.get_info()

class VocabLearning:
    def __init__(self, file = file, target = target):
        self.file = file
        self.target = target     
        
    def learning(self,file,target):

        def generate_wordlist(list_word):
            random_list = []
            while len(list_word) > 0:
                random_index = random.randint(0, len(list_word) - 1)
                random_list.append(list_word[random_index])
                list_word.pop(random_index)
            return (random_list)

        
        words = Formatting.word_list_processing(self.file)
        words = Formatting.trim_space(words)

        def remove_word(learned_vocab, words):
            for idx, w in enumerate(words):
                if str(learned_vocab) in w:
                    del words[idx]
            return words

        while True:
            # print(words)
            if len(words) == 0:
                txt3 = '\nHola, Bucket Done!!!\n'
                print(txt3.center(100,' '))
                break
            random_wordlist = generate_wordlist(list(range(0, len(words))))
            for random_index in random_wordlist:
                # print(words[random_index])
                words[random_index][5] += 1        
                input_ans = input('Meaning of ' + str(words[random_index][3]) +  ' is : ')
                if input_ans == words[random_index][0]:
                    words[random_index][4] += 1
                    count = words[random_index][4]
                    print ('Correct! '+ str(words[random_index][0]) + ' ' + str(words[random_index][4]) + '/' +  str(words[random_index][5]))
                    txt1 = str(words[random_index][1:3])
                    print('\n'+txt1.center(100,' ')+'\n')
                    if count == target:
                        txt2 = 'Congrats, '+ str(words[random_index][0]) + ' done!'
                        print('\n'+txt2.center(100, ' ')+'\n')
                        words = remove_word(words[random_index][0], words)
                        break
                else:
                    count = words[random_index][5]
                    print ('Incorrect => ' +  str(words[random_index][0]) + ' ' + str(words[random_index][4]) + '/' +  str(words[random_index][5]))
        

learn = VocabLearning(file,target)
learn.learning(file,target)

