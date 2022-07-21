In Python, a string can be split on a delimiter.

#### Example:

a = "this is a string" <br/>
a = a.split(" ") # a is converted to a list of strings. <br/>
print a <br/>
['this', 'is', 'a', 'string'] <br/>

Joining a string is simple:

a = "-".join(a) <br/>
print a <br/>
this-is-a-string <br/>

#### Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

#### Function Description
Complete the split_and_join function in the editor below.
split_and_join has the following parameters:
string line: a string of space-separated words

#### Returns
string: the resulting string

#### Input Format
The one line contains a string consisting of space separated words.

#### Sample Input
this is a string   

#### Sample Output
this-is-a-string