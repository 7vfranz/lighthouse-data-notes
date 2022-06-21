# Week 2 - Day 2 Notes

* to convert to df to csv: 
    * df.to_csv('csv')
    * index=False # auto stops from assigning an index 
 
<br>

* reading a csv: 
    * pd.read_csv('csv')
    * header = 0  # to assign header as index 0
    * more than one row as header: header=[0,1,2]
    * names=['a','b','c'], header=1: to name columns as assign as new headers
    * other way is to set index=False and header=False, to then assign names via names=['a']
    * to use other separators other than commas: df_csv = pd.read_csv('csv_example', sep=":")

<br>

* setting row index: 
    * df_csv.set_index('age') 
    * pre-assign with: df_csv = pd.read_csv('csv_example', sep=":", __index_col=1__)
    * can also be a list index_col=[0,2]
    * if all rows are not required - can specify number of rows: pd.read_csv('csv_example', sep=":", nrows=3)
    * skip blank lines: skip_blank_lines=False