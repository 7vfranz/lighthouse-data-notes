#### W02 - Weekend

* Regular expressions 
    * way of looking for matching text 
    * pattern matching for string of texts
    * define the pattern you are looking for 
    * regex101.com
    * most patterns use ASCII (american standard core for information interchange)
    * matches letters, digits, puncts, and other symbols 

    * some common  \d for digits \D for non-digit 
    * {} for amount of a letter, can specify a range {1,3} between 1 and 3 repeats but not more
        * can be paired with [] to specify amounts
        * paired with .{2,6} number of any characters 2-6
        * end with comma = 1 or more
        * '*' for 0 or more e.g. 'b*'
        * '+' for 1 or more 
        * ? for optionality - ab?c where b is optional must \? to match plain question mark
    * \. to match for period character
    * . alone is a wildcard to match anything 
    * [] for matching specific characters
        * [^] for not matching 
        * can specify a range [a-zA-Z0-9_] matches any for english text including underscore
        * [n-p] only match with letters from n to p

    * white spaces:
        * space (_)
        * tab (\t)
        * new line (\n_)
        * return (\r)
        * (\s) for any white space 
    
    * Starting and ending
        * (^) for starts with - not in square brackets
        * ($) for ending 
        * ^example$ - will only match with lines that start and end with 'example'
    
    * groups 
        * wrap with ()
        * useful for getting only specific extensions with diff filenames
        * e.g. ^(file.+)\.pdf$ 
        * for nested groups order of op is based on parenthesis which can be nested to capture specifcs. 
        * (\w+\s(\d+))
        * ((\d+)x(\d+)) capturing bordering digits around x

    * conditionals
        * (|) - use pipe
    
    * other special characters
        * \w+\b - matches full words, \b boundary between w and non-word - meta character
        * \0 for full matched text 
        * \1, \2 can be used for back referencing groups (\d+)-(\d+) can be reffed with \2-\1

-------

#### Regex in Python
* package 're'