#Changes

__Missing/No Features Found- Names__ : I have changed the method  ```all_redaction_names```; It is now able to find and redact the names properly.
__Small amount of Features Found - Gender__ : I have made some modifications to the  function  ```all_genders```; Instead of .replace(), I am using re.sub() and adding ``` "\\b{}\\b" ``` to make it take the requried features of genders.
__Missing/No Features Found- Phone Number__ : I have made some modifications to the  function ```all_redaction_phone```; I have added a new regex pattern and Instead of .replace(), I am using re.sub() and adding ``` "\\b{}\\b" ``` which will take the phone numbers and redact them.
__Small amount of Features Found - Concept__ : I have made some modifications to the  function  ```all_concept```; Changed the structure, Now this function will take all the features which was mentioned from the user, it will also redact the whole sentence of it. 
__Moderate amount of Features Found -Dates__ : I have made some modifications to the  function  ```all_redaction_dates```; Instead of .replace(), I am using re.sub() and adding ``` "\\b{}\\b" ``` to make it take the requried features of dates.
__Missing/No Features - Addresses__ : I have made some modifications to the  function ```all_redaction_address```; I have added a new regex pattern and Instead of .replace(), I am using re.sub()  which will take the address and redact them.
__Missing Stats__: I have made some modifications to the  function  ```w_stats```; It is now able to print ```stderr``` and ```stdout``` in the command line, and if any other file name is given by the user, it will create the file name and print the output in the file. Please make sure to give the directory if you would like to create a file in a specific directory. 
__File names not re-assigned correctly__: I have made some modifications to the function ```all_redaction_output```; I have made sure that whichever the file format is given it will change the file name to {filename}.{fileformat}.redacted Example: file1.txt.redacted

__Errors Running Test__: Test functions are running properly. 
__Output files not stored in respective folder__: The output files will be stored to the correct folder. It will be stored in the \project1 folder. Example: \project1\files\example1.txt.redacted

__Other Changes__: 
- Updated Collaborators file
- Updated Test Functions 
- Made Overall modifications to the redactor.py file 