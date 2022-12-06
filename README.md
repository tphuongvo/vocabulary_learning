**Vocabulary list**  
Vocabulary is from three main resources:  
   + GRE Vocabulary Flashcards - Magoosh GRE  
   https://gre.magoosh.com/flashcards/vocabulary/decks
   + 1000 words Manhattan vocab list
   https://drive.google.com/drive/u/2/folders/1wehmxu7Ee5zqTGPiHdpeAw_Ib3iHvfyP
   + Words smart for the GRE (Princeton review) about 200 words (on hold)

**Dictionary Vocab**  
Dictionary crawls word's meaning on Cambridge dictionary by command line then storing them in an excel workbook.  
**Using**  
* Command line:  
```
python DictionaryVocab/Cambridge_vocab.py `your word to look up`
```  
* Searching `ubiquitous`  
```
python DictionaryVocab/Cambridge_vocab.py ubiquitous
```  
Return:  
```
Definition: seeming to be everywhere

                / juːˈbɪk.wɪ.təs /
```  

**Noted**: This workbook should be converted to *csv* format and eliminated "," (comma) before being used for the Vocab_learner.  

**Vocab Learner**  
A vocabulary checking helper for English learners  
*vocab_learner.py*  
**Using**  
* Command line:  
```
python vocab_learner.py
``` 
`Set your Vocab list:`  give your vocab list to learn  
`Set your Target correct answer:`  give number of correct answers you want to check  

**Vocab List**  
Each list.csv contains around 25 words from those 3 sources.  
   + list.csv is extracted from my Notion and Anki app:  
    List_1: https://deserted-english-9dd.notion.site/Common-Words-I-Magoosh-GRE-List-I-b1d65295f9f54a209183096405c27e47  
    List_2: https://deserted-english-9dd.notion.site/Common-Words-I-Magoosh-GRE-List-2-5bf1d2dd526f4001afb36b7b5160008a  
    List_3: https://deserted-english-9dd.notion.site/Common-Words-I-Magoosh-GRE-List-3-6b849b7f8ced494d989aceba3d776768  
    List_4: https://deserted-english-9dd.notion.site/Common-Words-I-Magoosh-GRE-List-4-94a3bc9364df4df891f36fb78aca5c81