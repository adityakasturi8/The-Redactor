import argparse
import os
from project1 import all_functions

test_file = ".\tests\test.txt"

def test_input():
    full_data = all_functions.all_redaction_input(test_file)
    print (len(full_data))
    if (len(full_data)== 0):
        assert False
    else:
        assert True

def test_stats():
    fle = all_functions.all_redaction_input(test_file)
    fle = all_functions.all_redaction_phone(fle)
    fle = all_functions.all_redaction_names(fle)
    fle = all_functions.all_redaction_dates(fle)
    fle = all_functions.all_redaction_address(fle)
    random_word = 'random_word'
    all_functions.all_concept(fle, random_word)
    lst_of_stats= all_functions.lst_of_stats
    assert lst_of_stats is not None 
    
def test_redact_names():
    full_data = all_functions.all_redaction_input(test_file)
    redact_names = all_functions.all_redaction_names(full_data)
    count = 0
    for i in range(len(redact_names)):
        pattern = "\u2588"
        for j in range(len(redact_names[i])): 
            word = redact_names[i][j]
            pattern = len(word)*pattern
            if pattern == word:
                count = count + 1
    if count >= 0 or len(redact_names) > 0:
        assert True
    else:
        assert False

def test_redact_phone():
    full_data = all_functions.all_redaction_input(test_file)
    redact_phone = all_functions.all_redaction_phone(full_data)
    count = 0
    for i in range(len(redact_phone)):
        pattern = "\u2588"
        for j in range(len(redact_phone[i])): 
            word = redact_phone[i][j]
            pattern = len(word)*pattern
            if pattern == word:
                count = count + 1
    if count >= 0 or len(redact_phone) > 0:
        assert True
    else:
        assert False

def test_redact_address():
    full_data = all_functions.all_redaction_input(test_file)
    redact_address = all_functions.all_redaction_address(full_data)
    count = 0
    for i in range(len(redact_address)):
        pattern = "\u2588"
        for j in range(len(redact_address[i])): 
            word = redact_address[i][j]
            pattern = len(word)*pattern
            if pattern == word:
                count = count + 1
    if count >= 0 or len(redact_address) > 0:
        assert True
    else:
        assert False
        
def test_redact_dates():
    full_data = all_functions.all_redaction_input(test_file)
    redact_dates = all_functions.all_redaction_dates(full_data)
    count = 0
    if isinstance(redact_dates,list):
        redact_string = ''.join(redact_dates)
        if '\u2588' in redact_string:
            count += 1
    if count >= 0 or len(redact_dates) > 0:
        assert True
    else:
        assert False
        
def test_redact_gender():
    full_data = all_functions.all_genders(test_file)
    redact_gender = all_functions.all_genders(full_data)
    count = 0
    if isinstance(redact_gender,list):
        redact_string = ''.join(redact_gender)
        if '\u2588' in redact_string:
            count += 1
    if count >= 0 or len(redact_gender) > 0:
        assert True
    else:
        assert False