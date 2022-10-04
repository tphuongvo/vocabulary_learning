from readfile.read_file import *

class Formatting:
    def __init__(self,data_list, file):
        data_list = self.df
        file = self.file

    def word_list_processing(file):
        words_file = ReadFile.input_vocab_file(file).split('\n')
        words_file = [word.split(',') + [0, 0] for word in words_file]    
        return words_file

    def trim_space(data_list):
        # print(data_list)
        for miner_list in range(0,len(data_list)):  
            # print(data_list[miner_list])
            for element in range(0,len(data_list[miner_list])-2):       
                if type(data_list[miner_list][element]) != 'int':   
                    # print(data_list[miner_list][element])
                    data_list[miner_list][element] = data_list[miner_list][element].strip()
                else:
                    pass

        return data_list
