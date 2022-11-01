{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "11df3d27-1cf5-4f3c-aab1-717a8e24518f",
   "metadata": {
    "tags": []
   },
   "source": [
    "# Pandas - Series"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a50afb04-5592-4b45-b8e2-ccb18e272e07",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ec3c86cd-0180-48e0-9f01-612c03bd5427",
   "metadata": {
    "jp-MarkdownHeadingCollapsed": true,
    "tags": []
   },
   "source": [
    "### Creating straight from ndarray. No index passed, creates own\n",
    "* scalar data must have an index that matches the length\n",
    "* series works like ndarray - can do similar slciing with it, and np functions on it\n",
    "* can use Series.to_numpy() to convert to an actual ndarray\n",
    "* can be named"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "3be9ba74-072e-402b-97bc-39b6309868ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "s = pd.Series(np.random.randn(5), index=[1,2,3,4,5], name='myseries')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "cf860163-f3bb-461c-9a6c-0e2e87aab984",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1   -1.347644\n",
       "2    1.486419\n",
       "3   -2.639468\n",
       "4   -0.137392\n",
       "5   -0.752758\n",
       "dtype: float64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "4984929a-0452-4870-b750-04202a092c62",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'myseries'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "337b4113-aeea-4c0c-894d-0d324e0ee5be",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Int64Index([1, 2, 3, 4, 5], dtype='int64')"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.index"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "57df8dff-7519-4c9f-ade7-1d23a1e87568",
   "metadata": {
    "jp-MarkdownHeadingCollapsed": true,
    "tags": []
   },
   "source": [
    "### Creating from a dict\n",
    "* can call values through key like dictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b3bf9739-c569-4f46-a8ae-13ac9b71c7a7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "b    1\n",
       "a    0\n",
       "c    2\n",
       "dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d = {'b': 1, 'a': 0, 'c':2}\n",
    "pd.Series(d)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7be20f50-ece0-498a-892d-6e7d25b6fb22",
   "metadata": {
    "jp-MarkdownHeadingCollapsed": true,
    "tags": []
   },
   "source": [
    "### Vectorized operations\n",
    "* can be added, multiplied, numpy functions. \n",
    "* **MAIN diff series vs ndarray - series auto aligns data on the label, don't have to consider having the same labels**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7cd4146e-db1b-4e9f-b730-62a26fc1348d",
   "metadata": {
    "tags": []
   },
   "source": [
    "# Pandas - Data Frame"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cb3a9f0a-d9bf-4ec4-9ccd-3b3cc78f48d6",
   "metadata": {},
   "source": [
    "### From series or dictionary\n",
    "* creates columns from keys, and fills with series based on index\n",
    "* note missing when not specified on missing index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "16ed0606-5439-41eb-9877-500095e572ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),\n",
    "         'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "750c32f3-b932-4802-a36a-25239c82f516",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "3f1e8cdb-ce67-46ae-bd90-f3a48ac6d3bb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>one</th>\n",
       "      <th>two</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>b</th>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c</th>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>d</th>\n",
       "      <td>NaN</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   one  two\n",
       "a  1.0  1.0\n",
       "b  2.0  2.0\n",
       "c  3.0  3.0\n",
       "d  NaN  4.0"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "5086ee5c-2174-4c76-980b-98be6bb0735e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>one</th>\n",
       "      <th>two</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>b</th>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   one  two\n",
       "a  1.0  1.0\n",
       "b  2.0  2.0"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.DataFrame(d, index=['a','b'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "30f2f5d3-eccf-41e9-b227-a94642343ff0",
   "metadata": {},
   "source": [
    "### From Dictionary of ndarrays or lists\n",
    "* will auto create index as incrementing ints\n",
    "* pd.DataFrame(d, index=['a', 'b', 'c', 'd']) to set index name\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "2e3ad0b2-ea44-4334-8965-e57134250c83",
   "metadata": {},
   "outputs": [],
   "source": [
    "e = {'one': [1., 2., 3., 4.],\n",
    "         'two': [4., 3., 2., 1.]}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "73464955-0ddf-4e75-bf1e-bf0f7814e018",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>one</th>\n",
       "      <th>two</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.0</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   one  two\n",
       "0  1.0  4.0\n",
       "1  2.0  3.0\n",
       "2  3.0  2.0\n",
       "3  4.0  1.0"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.DataFrame(e)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "edb4e887-ce5f-4e3e-ab32-18c0a4035c42",
   "metadata": {},
   "source": [
    "### From a series"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eec9f287-a1c4-4646-ac76-dbb17246dff1",
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.DataFrame(pd.Series(np.random.randn(5), name='something'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c1f93880-b2b9-4171-a3c9-e0bccc028c8c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "0bc8e8c6-354c-4da3-97bd-5ac1cc031e8e",
   "metadata": {
    "jp-MarkdownHeadingCollapsed": true,
    "tags": []
   },
   "source": [
    "## Column selection, addition, deletion\n",
    "* df is dictionary of like-indexed series, works the same as a dictionary\n",
    "* e.g. \n",
    "    * df['one']\n",
    "    * df['three'] = df['one'] * df['two']\n",
    "* del df['two']\n",
    "* df['foo'] = 'bar'\n",
    "    * autopopulates column foo with bar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "317adfbb-3e84-44cb-ac84-72d645e68606",
   "metadata": {},
   "outputs": [],
   "source": [
    "# if index is not the same it will be conformed to data frame\n",
    "# df['one_trunc'] = df['one'][:2] \n",
    "# will take first two values and NaN for the rest on that one_trunc "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6bd91819-8a98-4b43-9573-a10a4794134c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# can do complete operations on a df \n",
    "# e.g. 1/df, df ** 4, etc. \n",
    "# boolean operators can be vectorized - 0,1,1 turned to True/False by setting dtype=bool"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b5d39653-f6bc-4d72-8d12-d06065333064",
   "metadata": {
    "tags": []
   },
   "source": [
    "## dtypes\n",
    "* categorical, integer, strings, boolean, any (object)\n",
    "* object catch all for everything \n",
    "* df.dtypes for all columns/Series\n",
    "* df['a'].dtype # for a specific column\n",
    "* strings can be object or string\n",
    "* .astype() - changes the type of columns\n",
    "\n",
    "* changing multiple column types at once:\n",
    "    * dft1 = dft1.astype({'a': np.bool, 'c': np.float64})"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e00de635-021f-4012-be05-14a19a1dcc10",
   "metadata": {},
   "source": [
    "# Pandas Basics"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "028fa1ea-3723-4ba6-8928-fa95780fc0ea",
   "metadata": {},
   "source": [
    "* turning columns to lower: df.columns = [x.lower() for x in df.columns]\n",
    "* .shape, .index, .columns\n",
    "* objects either index, series, or dataframe \n",
    "* to access contents of column df.a.array \n",
    "* df.value_counts() or df.mode() create histogram for 1D array of values\n",
    "\n",
    "\n",
    "#### Altering labels\n",
    "* df.reindex([a,b,c]) - reorders the data on new index, puts missing where not labeled/specified\n",
    "* sharing objects or reindex from a different index rs=s.reindex(df.index)\n",
    "* used for aligning data \n",
    "* for rows and columns at the same time: df.reindex(index=['c', 'f', 'b'], columns=['three', 'two', 'one'])\n",
    "* specify axis keyword for row or column, 'index' or 'column'\n",
    "\n",
    "#### Dropping labels from an axis\n",
    "* .drop(['a'], axis=0 or axis=1) 0 = row, and 1 = column\n",
    "\n",
    "#### Renaming\n",
    "* df.rename(columns={'one': 'foo', 'two': 'bar'},index={'a': 'apple', 'b': 'banana', 'd': 'durian'})\n",
    "* use dictionary with old name to newname \n",
    "* or specify axis =\"columns\" or \"index\" \n",
    "\n",
    "#### .dt and str accessors\n",
    "* .dt for changing to datetime.. df.dt.second to extract second etc. (day, dayofweek) \n",
    "* dt.tz_localize('US/Eastern') to change timezone\n",
    "* chaining to convert s.dt.tz_localize('UTC').dt.tz_convert('US/Eastern')\n",
    "\n",
    "* .str - S.str.lower() - used to lower case all the strings in that series. \n",
    "\n",
    "#### Sort\n",
    "* .sort_index(), ascending=False, axis=1 or 0\n",
    "* .sort_values(by='column') \n",
    "* can be done to multiple columns df1[['one', 'two', 'three']].sort_values(by=['one', 'two'])\n",
    "* argument: na_position='first' will put first, otherwise will be last. \n",
    "* can .sort_values on column and an index "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7f950552-c221-4d9e-a678-5cc1aa381fc8",
   "metadata": {},
   "source": [
    "------------------------"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c1aaa125-c8c2-4d72-aa76-a00e69b026ab",
   "metadata": {},
   "source": [
    "## SQL environemnts "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "faec4b7a-da09-47c6-9118-84fefb8db065",
   "metadata": {},
   "source": [
    "* often linked to specific database system: mysql, pgadmin, sqlite\n",
    "* IDES that work: eclipse, datagrip, SQLworkbenchj, vscode\n",
    "\n",
    "### Connecting to Databases\n",
    "* OBDC or JDBC \n",
    "* DBMS = Database Management Systems\n",
    "\n",
    "#### __ODBC__\n",
    "* open database connectivity \n",
    "* defines and performs the work to be done\n",
    "* access database without needing to recompile\n",
    "* allow applications to use SQL to access DBMS and data easily\n",
    "* DBMS connects to database\n",
    "* ODBC driver - process ODB function calls\n",
    "    * converts SQL syntax to be read by the DBMS\n",
    "* inserts a \"client driver\" - converts app queries to something the DBMS understands. \n",
    "\n",
    "#### __JDBC__\n",
    "* JAVA database connectivity \n",
    "* allows Java apps to connecto a relational database. e.g. mysql \n",
    "* advantage: provides access to various databases - wtihout needing to develop code for different databases - build own custom SQL statements (standardizes everything?).\n",
    "* supports ANSI SQL 2003\n",
    "* supports large number of databases\n",
    "* Driver - provides link from Java App to database, converts the calls for the databases\n",
    "* Driver Manager - connect app based on connection string, auto loaded based on the JDBC classpath\n",
    "    * usually 4.0 but legacy 3.0 with diff syntax\n",
    "* API - java.sql and javax.sql\n",
    "<br> \n",
    "* Development Process:\n",
    "* connect to db -> create statement object -> execute SQL query -> process result set\n",
    "<br>\n",
    "* Getting a connection:\n",
    "    * jdbc:driver protocol:driver connection details\n",
    "    * e.g. jdbc:odbc:DemoDSN jdbc:mysql://localhost:3306/demodb \n",
    "* Create a statement object:\n",
    "    * Statement myStmt = myConn.createStatement(); \n",
    "    * used later to exequte the SQL query\n",
    "* Execute SQL query\n",
    "    * ReultSet myRs = myStmt.executeQuery(\"select * from employees\");\n",
    "    * could pass a string that was build before\n",
    "* Process the result set\n",
    "    * ResultSet.next() \n",
    "        * moves forward one row, return true, if more rows to process\n",
    "    * to loop:\n",
    "        * while(myRs.next()) { // read data from each row }\n",
    "    * can use 'get' for reading data\n",
    "        * getXX(columnName) or getXX(columnIndex)\n",
    "        * e.g. println(myRs.getString('first_name')); println(myRs.getString('last_name'))\n",
    "        * prints the columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60755b88-2284-4d54-8b48-908e539730db",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:lhl_env38] *",
   "language": "python",
   "name": "conda-env-lhl_env38-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
