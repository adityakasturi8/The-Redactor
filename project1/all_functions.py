#from ast import pattern
from importlib.resources import path
from itertools import count
import os
import sys
import nltk
import re
from numpy import full
from pyparsing import nums
import spacy
import glob
from nltk.stem import WordNetLemmatizer
from sympy import prime
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')
nltk.download('all')
from nltk.corpus import wordnet
from nltk.tree import Tree
from commonregex import CommonRegex
import en_core_web_md



lst_of_stats = []
#print("Stats", stats_list)
nlp = en_core_web_md.load()

def all_redaction_input(files):
    
    full_data = ''
    for evy_file in files:
        path_of_listfiles = [glob.glob(str(filename))for filename in evy_file]
    flatten_path_list = nltk.flatten(path_of_listfiles)
    for fp in flatten_path_list:
        fileopen = open(fp)
        file_data = fileopen.read()
        file_data = file_data + '&&%#&*&'    
        full_data = ''.join([full_data, file_data])
        fileopen.close()
    return str(full_data)


def all_genders(full_data):
    count = 0
    lst_all_genders = ['Agender', 'Androgyne', 'Actor','Actress','Transgender','Androgynous', 'Bigender', 'Cis', 'Cisgender', 'Cis', 'Female', 'Cis', 'Male', 'Cis', 'Man', 'Cis', 'Woman', 'Cisgender', 'Female', 'Cisgender', 'Male', 'Cisgender', 'Man', 'Cisgenderhe', 'she', 'him', 'her', 'his', 'hers', 'male', 'female', 'man', 'woman', 'men', 'women', 'He', 'She', 'Him', 'Her', 'His', 'Hers', 'Male', 'Female', 'Man', 'Woman', 'Men', 'Women', 'HE', 'SHE', 'HIM', 'HER', 'HIS', 'HERS', 'MALE', 'FEMALE', 'MAN', 'WOMAN', 'MEN', 'WOMEN', 'he,', 'she,', 'him,', 'her,', 'his,', 'hers,', 'male,', 'female,', 'man,', 'woman,', 'men,', 'women,', 'He,', 'She,', 'Him,', 'Her,', 'His,', 'Hers,', 'Male,', 'Female,', 'Man,', 'Woman,', 'Men,', 'Women,', 'HE,', 'SHE,', 'HIM,', 'HER,', 'HIS,', 'HERS,', 'MALE,', 'FEMALE,', 'MAN,', 'WOMAN,', 'MEN,', 'WOMEN', 'new', 'line', 'he', 'she', 'him', 'her', 'his', 'hers', 'male', 'female', 'man', 'woman', 'men', 'women', 'He', 'She', 'Him', 'Her', 'His', 'Hers', 'Male', 'Female', 'Man', 'Woman', 'Men', 'Women', 'HE', 'SHE', 'HIM', 'HER', 'HIS', 'HERS', 'MALE', 'FEMALE', 'MAN', 'WOMAN', 'MEN', 'WOMEN','HE', 'SHE',	'HIM', 'HER', 'HIS', 'HERS', 'HIMSELF', 'HERSELF', 'BOYFRIEND','GIRLFRIEND', 'HUSBAND', 'WIFE', 'SISTER', 'BROTHER', 'SON', 'DAUGHTER', 'GIRL','BOY', 'MALE', 'FEMALE', 'MAN', 'MEN', 'WOMAN', 'WOMEN', 'MOTHER', 'FATHER', 'actress','boy', 'boyfriend', 'boyfriends', 'boys', 'bride', 'brother', 'brothers', 'chairman', 'chairwoman', 'dad', 'dads', 'daughter','princess', 'queens', 'she', "she's", 'sister', 'sisters', 'son','sons', 'spokesman', 'spokeswoman', 'uncle', 'uncles', 'waiter', 'waitress', 'widow', 'widower', 'widowers', 'widows', 'wife', 'wives', 'woman', 'women', "women's", 'daughters', 'dude', 'father', 'fathers', 'female', 'fiance', 'fiancee', 'gentleman', 'gentlemen', 'girl', 'girlfriend', 'girlfriends', 'girls', 'god','goddess', 'granddaughter', 'grandfather', 'grandma', 'grandmother', 'grandpa', 'grandson', 'aunt', 'aunts',  'groom', 'guy', 'he', "he's", 'her', 'heroine', 'herself', 'him','himself', 'his', 'husband', 'husbands', 'king', 'ladies', 'lady', 'lady', 'male', 'man', 'men', "men's", 'mom', 'moms', 'mother', 'mothers', 'mr','mrs', 'ms', 'nephew', 'nephews', 'niece', 'nieces', 'priest', 'priestess', 'prince','WOMAN','MEN','WOMEN']
    tokenized = nltk.word_tokenize((full_data))
    for every_word in tokenized:
        if every_word.lower() in lst_all_genders:
            full_data = re.sub("\\b{}\\b".format(every_word), '\u2588'*len(every_word), full_data)
            count = count +1
    string = "redaction_of_gender"
    get_stats(string,count)
    return full_data

def all_concept(full_data,concept):
    nums = 0
    synonyms_lst = []
    ccept_lst = []
    ccept_lst.append(concept)

    for element in ccept_lst[0]:
        for syn in wordnet.synsets((element)):
            for l in syn.lemmas():
                symns = l.name()
                synonyms_lst.append(symns)                   

            for lemma in syn.hyponyms():
                synm = lemma.lemma_names()
                synonyms_lst.extend(synm)
                    

    full_synonyms = synonyms_lst

    full_data1 = full_data.replace("\n",". ")
    full_data1 = full_data1.split(". ")
    res = []
    for val in full_data1:
        if val != None and val != '':
            res.append(val)
                
    for every_snt in res:
        for el in full_synonyms:
                #print(el)
            rg_fnd = re.findall(el, every_snt, flags=re.I)
            
            
            if len(rg_fnd) > 0:
                full_data,num = re.subn("\\b{}\\b".format(el), '\u2588'*len(el), full_data, count=0)
                nums = nums + num
                
                
    
    string = "redaction_of_concept"
    get_stats(string, nums)                   
    return full_data
    

def all_redaction_phone(full_data):
    #full_data = str(full_data)
    matched_phones = []
    #pattern = '(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}'
    
    pattern = '(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})'
    #pattern ='((?:\+|00)[17](?: |\-)?|(?:\+|00)[1-9]\d{0,2}(?: |\-)?|(?:\+|00)1\-\d{3}(?: |\-)?)?(0\d|\([0-9]{3}\)|[1-9]{0,3})(?:((?: |\-)[0-9]{2}){4}|((?:[0-9]{2}){4})|((?: |\-)[0-9]{3}(?: |\-)[0-9]{4})|([0-9]{7}))'
    matched_phones = re.findall(pattern, full_data)
    for phones in matched_phones:
        for every_phone in phones:
            #full_data = (full_data).replace(every_phone, '\u2588'*len(every_phone))
            full_data = re.sub("\\b{}\\b".format(every_phone), '\u2588'*len(every_phone), full_data)
    
    string = "redaction_of_phones"
    get_stats(string, len(phones))
    return full_data

def all_redaction_names(full_data):
    final_result = []
    doc = nlp(full_data)            
    final_result =  [ent.text for ent in doc.ents if ent.label_ == 'PERSON' ]
    for names in final_result:
            full_data = (full_data).replace(names,'\u2588'*len(names))
    string = "redaction_of_names"
    get_stats(string,len((final_result)))
    return full_data



def all_redaction_dates(full_data):
    full_data = str(full_data)
    matched_dates = []
    #pattern = r'^(?:(?:(?:0?[13578]|1[02])(\/|-|\.)31)\1|(?:(?:0?[1,3-9]|1[0-2])(\/|-|\.)(?:29|30)\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:0?2(\/|-|\.)29\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:(?:0?[1-9])|(?:1[0-2]))(\/|-|\.)(?:0?[1-9]|1\d|2[0-8])\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$'
    matched_dates = CommonRegex((full_data)).dates
    for dates in matched_dates:
        full_data = re.sub("\\b{}\\b".format(dates), '\u2588'*len(dates), full_data)
    string = "redaction_of_dates"
    get_stats(string,len((matched_dates)))
    return full_data

def all_redaction_address(full_data):
    matched_address = []
    pattern = '(\d{1,6}[A-Za-z]?\s(?:[A-Za-z0-9#]+\s){0,7}(?:[A-Za-z0-9#]+,*)\s*(?:[A-Za-z]+\s){0,3}(?:[A-Za-z]+,*)\s([A-Z]{2})\s(\d{4,5}))'
    matched_address = re.findall(pattern, (full_data))
    for address in matched_address:
        full_data = re.sub(address[0], '\u2588'*len(address[0]), full_data)
    
    string = "redacted_of_address"
    get_stats(string, len((matched_address)))
    return (full_data)



def get_stats(redacted_type = 'None', count = 0):
    #print("PRINTING",lst_of_stats)
    final_count = "The " + redacted_type + " has a count of : " + str(count)
    lst_of_stats.append(final_count)
    return lst_of_stats

def w_stats(path_to_file, lst_of_stats):
    
    if(path_to_file != 'stdout' and path_to_file !='stderr'):
        file = open(path_to_file, "w", encoding="utf-8")
        for i in lst_of_stats:
            
            file.write(i)
            file.write("\n")
        file.close()
    else:
        for i in lst_of_stats:
            if path_to_file == 'stdout':
                sys.stdout.write(i)
                sys.stdout.write("\n")
            if path_to_file == 'stderr':
                sys.stderr.write(i)
                sys.stderr.write("\n")
        
def all_redaction_output(files,full_data,final_out_path):
    
        
        ech_fl = (full_data).split('&&%#&*&')        
        
        names_of_files =[]
        
        files_ = nltk.flatten(files)
        for i in range(len(files_)):
            files = glob.glob(files_[i])
        
            for j in range(len(files)):
                if os.path.basename(files[j]):
                    files[j] = files[j] + '.redacted'
                names_of_files.append(files[j])

        for i in range(len(ech_fl)):
            for j in range(len(names_of_files)):
                if i==j:
                    file_data = ech_fl[i]
                    
                    first_path = (os.getcwd())
                    third_path = (os.path.join(first_path, 'project1'))
                    second_path = ("project1" + '/' +final_out_path+'/' + names_of_files[j])
                    
                    fldr_path = os.path.join(third_path,final_out_path)
                    final_path = os.path.join(first_path,second_path)
                    if os.path.isdir(fldr_path):
                        final_file = open(final_path, "w" ,encoding="utf-8")
                    else:
                        os.mkdir(fldr_path)
                        final_file = open(final_path, "w" ,encoding="utf-8")
                    
                    final_file.write(file_data)
                    final_file.close()
        
        return len(names_of_files)

    
        
