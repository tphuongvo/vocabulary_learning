import random

def get_info():
    """Ask the user set their goal before learning
    file: csv file contains vocabulary and meaning
    number: the number of correct answers each word 
    """

    def input_file(file):        
        try:
            input_file = input(file)
            return input_file
        except Exception:
            print(f"Input your vocabulary file name!")
            return vocab_learning.set_goal(file)

    def set_goal(number):        
        try:
            input_number = int(input(number))
            return input_number
        except Exception:
            print(f"Set your target correct answer!")
            return set_goal(number)

    file = input_file("Set your Vocab list: ")
    target = set_goal("Set your Target correct answer: ")

    return file,target

file, target = get_info()

class vocab_learning:
    def __init__(self, file = file, target = target):
        self.file = file
        self.target = target        
 
    def input_vocab_file(self, file):
        f = open(file + '.csv')
        words = f.read()
        f.close()
        return words

    def learning(self,file,target):

        def word_list_processing(file):
            words_file = self.input_vocab_file(self.file).split('\n')
            words_file = [word.split(',') + [0, 0] for word in words_file]    
            return words_file

        def generate_wordlist(list_word):
            random_list = []
            while len(list_word) > 0:
                random_index = random.randint(0, len(list_word) - 1)
                random_list.append(list_word[random_index])
                list_word.pop(random_index)
            return (random_list)

        
        words = word_list_processing(self.file)

        def remove_word(learned_vocab, words):
            for idx, w in enumerate(words):
                if str(learned_vocab) in w:
                    del words[idx]
            return words


        while True:
            random_permutation = generate_wordlist(list(range(0, len(words))))
            for random_index in random_permutation:
                # print(words[random_index])
                words[random_index][5] += 1        
                input_ans = input('Meaning of ' + str(words[random_index][3]) +  ' is : ')
                if input_ans == words[random_index][0]:
                    words[random_index][4] += 1
                    count = words[random_index][5]
                    print ('Correct! '+ str(words[random_index][0]) + ' ' + str(words[random_index][4]) + '/' +  str(words[random_index][5]))
                    txt1 = str(words[random_index][1:3])
                    print('\n'+txt1.center(100,' ')+'\n')
                    if count == target:
                        txt2 = 'Congrats, '+ str(words[random_index][0]) + ' done!'
                        print('\n'+txt2.center(100, ' ')+'\n')
                        words = remove_word(words[random_index][0], words)
                        if len(words) == 0:
                            txt3 = '\nHola, Bucket Done!!!\n'
                            print(txt3.center(100,' '))
                            break
                        continue           
                else:
                    count = words[random_index][5]
                    print ('Incorrect => ' +  str(words[random_index][0]) + ' ' + str(words[random_index][4]) + '/' +  str(words[random_index][5]))
        

learn = vocab_learning(file,target)
learn.learning(file,target)

