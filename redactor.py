import argparse
from project1 import all_functions
import os


if __name__ == "__main__":
    

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--input",type = str, required = True, help = "--input contains the input files", nargs = "*", action = "append" )
    args_parser.add_argument("--concept", type = str, required = False, help = "--concept redacts all the mentioned concepts and synonyms of that from the input file", action = "append")
    args_parser.add_argument("--phones", required = False, help = "--phones redacts all the phone numebrs from the input file", action = "store_true")
    args_parser.add_argument("--address",required = False, help = "--names redacts all the names from the input file", action = "store_true")
    args_parser.add_argument("--dates", required = False, help = "--dates redacts all the dates from the input file", action = "store_true")
    args_parser.add_argument("--genders", required = False, help = "--genders redacts all the genders from the input file", action = "store_true")
    args_parser.add_argument("--names", required = False, help = "--names redacts all the names from the input file", action = "store_true")
    args_parser.add_argument("--output", type = str, required = True, help = "--output contains the output file")
    args_parser.add_argument("--stats", type = str, required = False, help = "Provide the statistics of the redacted file")
    
    args = args_parser.parse_args()
    
    full_data = all_functions.all_redaction_input(args.input)
    lst_of_stats = all_functions.get_stats()
    
    if args.concept:
        full_data = all_functions.all_concept(full_data, args.concept)
    if args.phones:
        full_data = all_functions.all_redaction_phone(full_data)
    if args.address:
        full_data = all_functions.all_redaction_address(full_data)
    if args.dates:
        full_data = all_functions.all_redaction_dates(full_data)
    if args.genders:
        full_data = all_functions.all_genders(full_data)
    if args.names:
        full_data = all_functions.all_redaction_names(full_data)
    if args.output:
        all_functions.all_redaction_output(args.input, full_data, args.output)
    if args.stats:
        all_functions.w_stats(args.stats, lst_of_stats)
