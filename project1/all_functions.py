#from ast import pattern
import os
import nltk
import re
import spacy
import glob
from nltk.stem import WordNetLemmatizer
#nltk.download('all')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet') 
from nltk.corpus import wordnet
from nltk.tree import Tree
from commonregex import CommonRegex
import en_core_web_md


lst_of_stats = []
#print("Stats", stats_list)
nlp = en_core_web_md.load()

def all_redaction_input(files):
    
    full_data = []
    #list_filepaths =[]
    for evy_file in files:
        path_of_listfiles = [glob.glob(str(filename))for filename in evy_file]
    flatten_path_list = nltk.flatten(path_of_listfiles)
    for fp in flatten_path_list:
        fileopen = open(fp)
        file_data = fileopen.read()
        full_data.append(file_data)
        full_data.append('nxt')
        fileopen.close()
    
    full_data = str(full_data)
    #print(full_data)
    return str(full_data)


def all_genders(full_data):
    count = 0
    lst_all_genders = [' him','he', 'she',   'him', 'her', 'herself', 'boyfriend','girlfriend', 'husband', 'wife', 'sister', 'brother', 'son', 'daughter', 'girl','boy', 'male', 'female', 'man', 'men', 'woman', 'women', 'mother', 'father','male','female','wife','husband','feminine','masculine','father','brother','brother-in-law','sister','girl','boy','man','woman','women','men','actress','waitress','daughter','son','bride','groom','uncle','aunt','mom','mother','papa','niece','nephew','his', 'hers', 'himself']
    #full_data = full_data.split('  \n   ')
    #full_data = nltk.flatten(full_data)
    tokenized = nltk.word_tokenize(str(full_data))
    for every_word in tokenized:
        if every_word.lower() in lst_all_genders:
            full_data = str(full_data).replace( every_word,'\u2588'*len(every_word))
            count = count +1
        
    #print(full_data)
    string = "redaction_of_gender"
    get_stats(string,count)
    
    return full_data

def all_concept(full_data,concept):
        full_data = list(nltk.flatten(nltk.flatten(full_data)))
        synonyms_lst = []
        ccept_lst = []
        ccept_lst.append(concept)
        ccept_lst = nltk.flatten(ccept_lst)
        ccept_lst = nltk.flatten(ccept_lst)
        #ccept_lst = ','.join(concept_list)
        ccept_lst = str(ccept_lst)
        #
        # print(type(ccept_lst))
        #print("THIS IS PRINTING", ccept_lst)
        for element in ccept_lst:
            for syn in wordnet.synsets((ccept_lst)):
                for lemma in syn.hyponyms():
                    synm = lemma.lemma_names()
                    synonyms_lst.append(synm)

        full_synonyms = list(nltk.flatten(synonyms_lst))
        for i in concept:
            full_synonyms.append(i)
        
        redacting_lst = []
        for ele in full_data:
            doc = nlp(ele)
            for sents in doc.sents:
                for concept in full_synonyms:
                    if concept in str(sents):
                        
                        ele = ele.replace(str(sents),"\n"+ u"\u2588"*len(str(sents)))
                        
            redacting_lst.append(ele)


        
        #print(redacting_lst)
        string = "redaction_of_concept"
        get_stats(string, len(full_synonyms))
        return redacting_lst

def all_redaction_phone(full_data):
    full_data = str(full_data)
    matched_phones = []
    pattern = '(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}'
    matched_phones = re.findall(pattern, full_data)
    #print(matched_phones)
    for phones in matched_phones:
        for every_phone in phones:
            full_data = str(full_data).replace(every_phone, '\u2588'*len(every_phone))
    #print(full_data)
    
    string = "redaction_of_phones"
    get_stats(string, len(matched_phones))
    return full_data

def all_redaction_names(full_data):
    
    redact_of_names = []
    final_result = []
    for i in range(len(full_data)):
        #temp_file = full_data[i]
        tokenized_names = nltk.word_tokenize(full_data)
        pos_tokenized_names = nltk.pos_tag(tokenized_names)
        chunk_taggs = nltk.chunk.ne_chunk(pos_tokenized_names)
        for chk in chunk_taggs:
            if type(chk) == Tree:
                if chk.label() == 'PERSON':
                    for i in range(len(chk)):
                        redact_of_names.append(chk[i][0])
                    final_result.append(redact_of_names)
                    #print(redact_of_names)
    for names in final_result:
        for every_name in names:
            full_data = str(full_data).replace(every_name,'\u2588'*len(every_name))
    #print(full_data)
    string = "redaction_of_names"
    get_stats(string,len((names)))
    
    return full_data



def all_redaction_dates(full_data):
    full_data = str(full_data)
    matched_dates = []
    #pattern = r'^(?:(?:(?:0?[13578]|1[02])(\/|-|\.)31)\1|(?:(?:0?[1,3-9]|1[0-2])(\/|-|\.)(?:29|30)\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:0?2(\/|-|\.)29\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:(?:0?[1-9])|(?:1[0-2]))(\/|-|\.)(?:0?[1-9]|1\d|2[0-8])\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$'
    #matched_dates = re.findall(pattern, full_data)
    matched_dates = CommonRegex((full_data)).dates
    for dates in matched_dates:
        full_data = (full_data).replace(dates,'\u2588'*len(dates))
    #print(full_data)
    string = "redaction_of_dates"
    get_stats(string,len(str(matched_dates)))
    return full_data

def all_redaction_address(full_data):
    matched_address = []
    #pattern = r'[0-9]{1,3} .+, .+, [A-Z]{2} [0-9]{5}'
    pattern = r'\d{1,6}\s(?:[A-Za-z0-9#]+\s){0,7}(?:[A-Za-z0-9#]+,)\s*(?:[A-Za-z]+\s){0,3}(?:[A-Za-z]+,)\s*[A-Z]{2}\s*\d{5}'
    matched_address = re.findall(pattern, str(full_data))
    #print(matched_address)
    for address in matched_address:
        full_data = str(full_data).replace(address,'\u2588'*len(address))
        
    #print(full_data)
    string = "redacted_of_address"
    get_stats(string, len(str(matched_address)))
    return (full_data)




def w_stats(lst_of_stats=lst_of_stats):

    p = ('./stderr/stderr.txt')
    #if not os.path.exists('./docs/stderr.txt/%s' % p):
    #os.makedirs('./docs/stderr./%s' % p) 
    file = open(p, "w", encoding="utf-8")
    for i in range(len(lst_of_stats)):
        file.write(lst_of_stats[i])
        file.write("\n")
    file.close()
    return lst_of_stats



def get_stats(redacted_type= 'none', count=0):
    #print("PRINTING",lst_of_stats)
    final_count = "The " + redacted_type + " has a count of : " + str(count)
    lst_of_stats.append(final_count)
    return lst_of_stats

def all_redaction_output(files,full_data,final_out_path):
    
        #print("THIS IS PRINTING", input_data)
        ech_fl = str(full_data).rsplit('nxt')
        # print("************ PRINTING", ech_file[0])
        names_of_files =[]
        files_ = nltk.flatten(files)
        for i in range(len(files_)):
            files = glob.glob(files_[i])
        
            for j in range(len(files)):
                if '.txt' in  files[j]:
                    files[j] = files[j].replace(".txt", ".redacted")
                if '.md' in files[j]:
                    files[j] = files[j].replace(".md", ".redacted")
            
                names_of_files.append(files[j])

        for i in range(len(ech_fl)):
            for j in range(len(names_of_files)):
                if i==j:
                    file_data = ech_fl[i]
                    
                    first_path = (os.getcwd())
            
                    second_path = (final_out_path+'/'+names_of_files[j])
                    #print("**************",path2)
                    fldr_path = os.path.join(first_path,final_out_path)
                    final_path = os.path.join(first_path,second_path)
                    if os.path.isdir(fldr_path):
                        final_file = open(final_path, "w" ,encoding="utf-8")
                    else:
                        os.mkdir(fldr_path)
                        final_file = open(final_path, "w" ,encoding="utf-8")
                    
                    final_file.write(file_data)
                    final_file.close()
                    
        return len(names_of_files)

    
        
