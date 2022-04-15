> # The Redactor
### Author : Aditya K Kasturi 

__About:__
- When classified information needs to be made available to the public, it must first be redacted. In this procedure, all sensitive names, locations, and other information are concealed. Documents containing sensitive information, such as incident reports, dispatch logs, and patient information, are often found. The process of redacting this information can be time-consuming and costly.To redact sensitive information included in .txt files,  in this project we will learn to use the redaction process for which we will use packages like NLTK, Spacy, and other things.

__Libraries and Packages Used:__
- os
- nltk
- spacy
- commonregex
- regex 
- glob
- argparse
- en_core_web_sm
- glob

### Assumptions 
- The NLTK package is being used to identify the names in the documents, and custom regex patterns are being used to identify the phone numbers, addresses, and genders in the documents. The commonregex library is being used to identify the various dates that are present in the documents in this particular project.
- The majority of the data associated with them can be identified and redacted using these approaches, but there may be edge circumstances in which regex patterns are unable to identify the dates, names, genders, addresses, and phone numbers, among other information.
- The documents that are supposed to be redacted are saved in the files folder by default, and this is where they will be found.
- The redactions are counted and saved in the stderr folder by the stats function.
- The only files that were used in this project were.txt files.

### Bugs
- A bug found in the count of redacted names was that the redaction of names is occurring quite accurately, but the stats count of the redacted names is much higher than usual. It also ignores a few names to redact.
Example: if redacted names were 6, the stats file shows 65490.

- The --names function is taking approximately 30 to 40 mins to execute.

- Another bug which needs to be mentioned is that, during the redaction of phone numbers, the regex is redacting most of the phone numbers and not redacting a few types of phone numbers. However, in a few cases, it is also redacting the spaces between phone numbers. But when we count the number of redactions in the stats file, it shows the correct redaction count.

- In text files, the redaction process also changes genders in words sometimes. Father, it is redacting the "her" in the father's word. 

- For concepts, the wordnet is unable to provide all the synonyms related to the given word. It redacts the word and sentences related to the word in some cases and does nothing in others. 

- For addresses, it can only redact US postal addresses and is unable to redact other kinds of addresses.



 ### Description

__How to install and use this packages:__
0. Require prior installation of python, pip and requirements 
1. Create a directory using ```mkdir``` and cd a ```project1```
2. gitclone my repository ```https://github.com/adityakasturi8/cs5293sp22-project1.git```
3. cd into the project directory ```cs5293sp22-project1/project1```
4. install python package pipenv by typing ```pip install pipenv```
5. run unit test using ```pipenv run python -m pytest```
6. run the redactor.py file using the below instructions

__Running the Program:__
- The program can be run by utilizing the commandline.
- To run the program, navigate to the project1 folder and run the redactor.py file 
- The redactor.py can be run by using the following command: 
  ```
  pipenv run python redactor.py --input '*.txt' \
                    --names --dates --phones --genders --address\
                    --concept 'kids' \
                    --output 'files/' \
                    --stats stderr
  ``` 
__Dataset:__
- For this project, the dataset has be acquired from Enron Email Dataset. 
- The dataset can be found on ```https://www.cs.cmu.edu/~enron/``` or can be directly downloaded using ```https://www.cs.cmu.edu/~enron/enron_mail_20150507.tar.gz```




__Result:__
- Printing all the data after redaction process by redacting all the sensitive data like names, gender, address, phone number, dates, and synonyms of a given word.
  
__Functions:__

- In the redactor.py file, There are nine functions:

0. __redactor.py__ :  The redactor.py file calls all the functions from all_functions.py and executes the flow of the project.
                  The redactor.py has all different funtions imported from the all_funtions.py, it contains the following functions
                  ```

                 all_redaction_input(args.input)

                  all_genders(full_data)
                  
                  all_concept(full_data, args.concept)
                  
                  all_redaction_phone(full_data)
                  
                  all_redaction_names(full_data)

                  all_redaction_dates(full_data)
                  
                  all_redaction_address(full_data)

                  all_redaction_output(args.input, full_data, args.output)

                  w_stats()
                  ```
1. __all_redaction_input(args.input)__ : The all_redaction_input(args.input) funtion takes the data that is extracted from all of the.txt files in the working directory by specifying the —input flag in the command line argument. The data is returned to redactor.py in a specific way. Additionally, it extracts the input file names or patterns to identify the input files using the arguments passed from the command line as parameters, which is accomplished through the use of the glob library.

2. __all_genders(full_data)__: This function takes the data returned by the previous functions, as well as the command line parameters, and redacts the gender-specific words. All of the detected gender words are replaced with block characters, and if the —genders flag is given from the command line, the method returns data that has been redacted. we use wordnet from nltk here.

3. __all_concept(full_data, args.concept)__: When the -concept flag is passed, this method takes input parameters and returns them. Additionally, the program redacts the entire sentence, identifying words that are similar to the concept word that was used as an argument. The method returns data that has been redacted, and all sentences that were recognized are replaced by block characters.

4. __all_redaction_phone(full_data)__:  Using the below regex pattern, this method uses input parameters from a file and a command line to redact phone numbers from data.  If --phone flag is specified, all identified phone numbers are replaced with block characters and redacted data is returned  
```(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}```
5. __all_redaction_names(full_data)__: When the –-names flag is specified in the command line, this function is called.
All_redaction_input(args.input) returns input data, which is then masked with the Unicode character by this method.
Using the spacy and nltk libraries, we identified items such as "PERSON," which are considered to be names, and more specifically proper nouns. 

6. __all_redaction_dates(full_data)__: The date values are redacted using the commonregex package by taking the data returned by the above and command line input parameters.  If --dates flag is specified, all identified dates are replaced with block characters and redacted data is returned 

7. __all_redaction_address(full_data)__:  Using the below regex pattern, this method uses input parameters from a file and a command line to redact address from data.  If --address flag is specified, all identified phone numbers are replaced with block characters and redacted data is returned  
```r'\d{1,6}\s(?:[A-Za-z0-9#]+\s){0,7}(?:[A-Za-z0-9#]+,)\s*(?:[A-Za-z]+\s){0,3}(?:[A-Za-z]+,)\s*[A-Z]{2}\s*\d{5}'```

8. __all_redaction_output(args.input, full_data, args.output)__:After all the redaction steps are completed, this method is used to write the output data into a file named .redacted in the output path. In the output path, .redacted files are created according to the input .txt files.

9. __w_stats()__: All statistics relating to redact type and numbers of words redacted are written to the stderr/stderr.txt file on the system's standard output. Therefore, whenever the –stats flag is used in the input, this method is invoked and the statistics are written to the stderr.txt file, which is hardcoded in the program.


__Test_Cases__:
- Every test funtion is tested with a passing case
1. for ```test_input()``` one passing case is tested with checking if the input file is returning or not 
2. for ```test_stats()```  one passing case is tested with the length of lst_of_stats is > 0. 
3. for ```test_redact_names()``` One passing case is tested by checking if the count or the length of the redacted name is satisfied 
4. for ```test_redact_phone()``` One passing case is tested by checking if the count or the length of the redacted phones is satisfied 
5. for ```test_redact_address()```  One passing case is tested by checking if the count or the length of the redacted address is satisfied 
6. for ```test_redact_dates()``` One passing case is tested by checking if the count or the length of the redacted dates is satisfied 
7. for ```test_redact_gender()``` One passing case is tested by checking if the count or the length of the redacted gender is satisfied 


