class ReadFile:
    def __init__(self,file :str, number: int):
        file = self.file
        number = self.number
        
    def get_info():
        """Ask users set their goal before learning
        file: a csv file containing vocabulary and meaning
        number: a number of correct answers per word 
        """

        def input_file(file):        
            try:
                input_file = input(file)
                return input_file
            except Exception:
                print(f"Input your vocabulary file name!")
                return input_file(file)

        def set_goal(number):        
            try:
                input_number = int(input(number))
                return input_number
            except Exception:
                print(f"Set your target for number of correct answers!")
                return set_goal(number)

        file = input_file("Set your Vocab list: ")
        target = set_goal("Set your Target correct answer: ")

        return file,target

    def input_vocab_file(file):
        f = open(file + '.csv', encoding='utf-8-sig')
        words = f.read()
        f.close()
        return words
