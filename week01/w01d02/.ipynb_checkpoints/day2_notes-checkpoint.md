# Notes for Day 2

## Refreshers
### Dictionaries
[Refresher](https://code.tutsplus.com/tutorials/a-smooth-refresher-on-pythons-dictionaries--cms-25198)

* can chain index:
``` french_spanish[english_french['door']] ```

* copying a dictionary and assigning to another dictionary:
``` new_english_french = english_french.copy() ```

* can have nested dictionaries i.e. dictionary within a dictionary

* iterating with a for loop is not ordered, and will only give the keys
    * can use .iterkeys() or .itervalues() 

* create dictionaries using dict()
    * dict(key = 'value')
    * dict([('key','value')])
    * dict(zip(['key1','key2'],['value1,'value2']))

### Tuples

* written with () or without
* immutable
* can be nested 

Concatenate with +

Reptition with *

Search: tuple1.index(n)
Count: tuple1.count('value')
Index: same as a list
Sliced: tuple1[1:3]

### Conditional Statements
* if, elif, else
* or, and, not

### Loops
* while, for 

* statements used in while and for loops:
    * break - causes loop to terminate
    * continue - returns control back to the beginning of the loop and ignores anything coming after
    * pass - null statement not to do anything - place holder for something to put in.
    * else - command to run when loop exits

### Functions 
* numbers_list.insert(5, 8)
    * inserts 8 in index 5

* Lambda functions are anonymouse, defined without a name
    * can have multiple arguments but only one expression
    * using lambda f'n for efficiency
    * double = lambda x: x*2, x is the input and 
    * can be used with built-in functions like: filter(fn, list) or map(fn, list)
    * map creates a new list new_list = list(map(lambda x: x * 2 , my_list)) from the lambda output

---

## Coding Skills for Data Science
[Reading](https://dimensionless.in/is-programming-knowledge-required-to-pursue-data-science/)

---

## Sets
* all unique values
* make an empty set: x = set()
* defined with {}
* elements can be of different types, but must be immutable
    * tuples can be included but not lists or dictionaries
* can't be indexed or sliced

### Operators and Methods

#### Union
* to join two sets must use x1.union(x2) - will do even if one is not a set
* or bar operator x1 | x2 - will only join two sets
* useful for joining and getting only uniques 

#### Intersection
* x1.intersection(x2) - will return only the common elements in both sets
* x1.intersection(x2,x3,x4) can do with multiple sets


#### Difference
* x1.difference(x2) - returns elements in x1 that's not in x2
* x1 - x2 is the same
* can be used with multiple sets


#### Symmetric Difference
* a.symmetric_difference (b) - returns the set of all elements in either x1 or x2 but not both
    * (not middle of venn diagram) 
* x1 ^ x2 
* multiple sets can be done only with ^ but not symmetric_difference()


#### x1.isdisjoint(x2)
* determines whethere or not two sets have elements in common
* returns a bool, True - if none common, False - if 1+ in common
* no operator

#### x1.issubset(x2)
* x1 <= x2 - whether one set is a subset of another
* x1 < x2 - for proper subset, meaning a subset but not identifcal 
* a set is a subset of itself but not a proper subset


### x1.issuperset(x2)
* x1 >= x2
* opposite way - x1 contains all the elements of x2
* a set is considered a superset of itself
* x1 > x2 - for proper superset - same as superset but not identical

### Modifying a set
* x1.update(x2)
* x1 |= x2
* adds elements from x2 to x1 that x1 doesn't already have.

### x1.intersection_update(x2[, x3 ...])
* x1 &= x2
* updates x1 to only elements found in both x1 and x2 

### x1.difference_update(x2[, x3 ...])
* x1 -= x2
* updates x1 removes elements found in x2

### x1.symmetric_difference_update(x2)x5
* x1 ^= x2
* retains found in x1 or x2 but not both

### x.add(<elem>)
* adds an element
### x.remove(<elem>)
* removes elem, raise exception if not found
### x.discard(<elem>)
* removes elem, no exception if not found
### x.pop() 
* randomly deletes an element
### x.clear()
* clears the set 

## Frozen Sets
* an immutable set
* x = frozenset([1,2,3])
* no adds, no pop, clear
* can be reassigned

----------------------------------------
## Errors
* try, except, else, finally
    * except - when error occurs in try
    * else - if try block is error free
    * finally - executed irrespective of exception 
* raise 
    * raises if there's an exception, pair with bool


----------------------------------------
## Copy in Python
* can't just assign to new variable - changes in new will appear in old
* two ways: (1) Shallow and (2) Deep
* uses copy module
    * import copy
    * copy.copy(x)
    * copy.deepcopy(x)

### Shallow
* copy.copy(x) adding doesn't appear but changes to a nested object will
* they share the reference of same nested objects 
* only nested objects can be changed 
* base address is copied

### Deep
* creates an independent copy and all nested objects 
* does not share the same reference 
* changes to old_list even in nested objects not transferred to new_list
* recursively copies - all nested objects are also copied and become independent
* base address is not copied 

----------------------------------------
### Modules
* python scripts - preset

### Packages 
* sets of modules

### Collections 
[Collections](https://towardsdatascience.com/pythons-collections-module-high-performance-container-data-types-cb4187afb5fc)
[Collections2](https://stackabuse.com/introduction-to-pythons-collections-module/)

* built-in python module - implements specialized container datatypes - alternatives to built-in containers of dict, list, set and tuple

1. namedtuple() 
* gives tuples named fields, to improve readability of what each one means
```python
from collections import namedtuple
fruit = namedtuple('fruit','number variety color')
guava = fruit(number=2,variety='HoneyCrisp',color='green')
apple = fruit(number=5,variety='Granny Smith',color='red')
guava.color
'green'
```

* named_tuple._make([]) - creates a named tuple from named_tuple from a list
* named_tuple._asdict() - converts to a list of paired tuples 
* named_tuple._replace(age='14') - creates a new instance - doesn't change the value in the existing instance

* works like an immutable class dictionary
* declares the name of the namedtuple then assigns it to a given tuple



2. Counter
* dict subclass
* creates a dictionary that counts the number of iter elements in a list or dictionary
* from collections import Counter
```py
c = Counter('abcacdabcacd')
print(c)
Counter({'a': 4, 'c': 4, 'b': 2, 'd': 2})
```

* Methods:
    * elements() - returns list of elements with specified number unless 0
    * most_common(n) - returns list of most common elements and their counts, n is for how many to include.
    * .subtract(<dict>) - take away from the counts 
    * see link for more
    

3. defaultdict
* creates a key that isn't in the dictionary yet, when trying to access a key that's not defined 

4. OrderedDict
* by keys: OrderedDict(sorted(d.items(), key=lambda t: t[0]))
* by value: OrderedDict(sorted(d.items(), key=lambda t: t[1]))
* by length of key: OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
* note change in t 
* changes in value of key does not change the order 

5. ChainMap
* combines dictionaries and returns a list of dictionaries
* chain_map = ChainMap(dict1, dict2)
    * print(chain_map.maps)
* changes on on original dictionary gets transferred to ChainMap
* if same key appears in more than one dictionary - will only report the first 
* chain_map.new_child(dict3) - adds a new dictionary to the chain map


6. deque 
* for removing and inserting items
* deq = deque(list1) - converts list to a deque
* deq.appendleft('x') - adds to the beginning
* deq.popleft() - removes left
* .pop and .append work the same 
* .clear() - clears everything
* .count('x') - counts elements 
----------------------------------------
# Datetimes
* [datetime](https://www.dataquest.io/blog/python-datetime-tutorial/)
* datetime(year, month, day, hour, minute, second, microsecond), date(y,m,d), time(h,m,s,ms), timedelta, tzinfo (timezones)

```py
my_string = '2019-10-31'

# Create date object in given time format yyyy-mm-dd
my_date = datetime.strptime(my_string, "%Y-%m-%d")

my_date.month
my_date.year

my_date.weekday() #gives the number of the weekday 

# To get the weekday name
# 0 is monday and so on
import calendar
calendar.day_name[my_date.weekday()

```

* for times:
    * .hour
    * .minute

* for week number
    * .isocalendar - starts the count monday = 1, 2nd number is week number
    * output is: a tuple of (2019, 43, 5)

* converting to a timestamp
    * timestamp = datetime.timestamp(datetime.now()) - can assign now = datetime.now()
    * to reverse: dt_object = datetime(fromtimestamp(timestamp)

* timedelta
    * to calculate difference in time
    * subtracting two dates automatically gives you days and times 
    * d = timedelta(weeks = 2) - creates timedelta object with difference of 2 weeks 
    * to add: future_date_after_15days = now + timedelta(days = 15)
    * to subtract: two_weeks_ago = now - timedelta(weeks = 2)
    * diff = date1 - date2 - easier with datetime than just date
    * use ("t1 =", abs(t1))  for negative timedeltas 
    * t.total_seconds() to convert a time delta to seconds

## Formatting Dates 
* strftime() and strptime()
* strptime()
    * converts from string to datetime
    * time.strptime(string,format)
    * format is the format the string is in - and gets converted into a date_object 

* strftime()
    * converts from datetime to string
    * [strftime_patterns](https://strftime.org/)
    * date_time.strftime("%pattern")


## Timezones
* pytz module for conversions
* from pytz import timezone
* east = timezone('US/Eastern') - can assign a timezone to a variable 
* loc_dt = east.localize(my_datetime) - can then use to localize a datetime object
* au_tz = timezone('Australia/Sydney')
* loc_dt.astimezone(au_tz) - converts the loc_dt to australian timezone 


## Datetime in Pandas
* to_datetime() - converts string dates and time to datetime 
    * can even be complex strings e.g. date = pd.to_datetime("8th of sep, 2019")
* to_timedelta() - can be used to create a series of dates
    * using numpy - date_series = date + pd.to_timedelta(np.arange(12), 'D')
    * using pandas only - d.date_range('08/10/2019', periods = 12, freq ='D')
* to access year, month, day, hour, weekday, weekday_name, dayofyear
    * df['date'].dt.year - from a datetime column 
* can be converted to an index df.index = df.date



----------------------------------------

# Lecture
int and // both round down no matter what
round(x,y) rounds to nearest 

### Strings
* for string ''' multi-lined 
* doc strings """
* concat with + 
* strings function similarly to list
* .upper() .capitalize()

### Lists
list1.index('name') - gives the value of the index

large_animals[2:-1] indexes second to last, not the last item use : to do that

but [-1] will index the last item

large_animal[0:4] = 'Simon' # doesn't duplicate value but iterates over 'Simon' string 

.append()

del deletes

use + to concatenate

on a string can transform to a list based on a value.

c = a.split('s ') turns string a into a list splits based on 's ' 

### Tuple 
* more efficient/faster to find things

* x = ('var1', 'var2', 'var3')
* unpacking - var1, var2, var3 = x
* will assign each value in the tuple to separate variables
* combined with concat

### Dictionary
* x.items() #returns everything in that list as a tuple 
* can't have duplicate keys will reassign the value
* remember that dictionaries are not ordered and can't be indexed as such

can then be unpacked:
```
for key,value in x.items():
    print(str(key) + str(value))
```

### Sets
* limited use case, unordered, {}
* used can only contain unique values no duplicate entries
* if duplicate entries are saved, dupe is automatically removed
* also gets ordered - with uppercase before lowercase
* useful for finding unique entries and number of uniques
* no colons

### Booleans
and, or
True or False = True
False or False = False (only time it is false)

### Control structures or Control flow 
if, elif, else

### For loops
* definite iterations
* for [variable] in [iterable data structure (like a list)]:
   
    [what to do for each iteration]

* for key,value in dict1.items(): 

* for i in range(len(course_marks)): 
    * iterates over the range of the length
    * range is iterable - can be convered to a  list

* iterating through a dictionary
    * when not specified will iterate over the keys 
    * more readable: for x in dict1.keys():
    * iterate through values: for x in dict1.values()it
    * iterating through key,items: for key,item in course_marks.items():
    print(key,item)

### While loops
boolean expression evaluates true and false and will continue until stopped 

### Functions

* can have a default value def f(name='Name')


```py ``` formats the code block to python in discord 