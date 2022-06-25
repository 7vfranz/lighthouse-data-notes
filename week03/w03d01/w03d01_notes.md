#### Week 3 - Day 1 - Data Visualization

[best practices](https://www.gooddata.com/blog/5-data-visualization-best-practices/)

* best packages: matplotlib, seaborn, plotly

1. Matplotlib
* interactive figures using desktop-GUI toolkits like Qt and GTK
* MATLAB based
* can be functional approach (stateful) or object oriented (stateless)
<br>

* Functional Approach (Stateful)
    * plt.plot(x,y) - uses basic matplotlib command - to create a plot
    * plt.show() if not in ipynb
    * plt.xlabel(), .ylabel(), .title()
    * plt.subplot(1,2,1) - with nrows, ncols, plot_number - creates two plots on the same canvas
```python
plt.subplot(1,2,1)
plt.plot(x,y,'red')
```
    * plots a line 

* Object Oriented (Stateless)
    * create a figure "fig" call methods off of it using .figure or .subplots()
    * fig = plt.figure
    * ax = fig.add_axes([0,0,1,1]) - corresponding to left, bottom, width, height
    * ax.plot(x,y,'red')
    * ax.set_xlabel, ax.set_ylabel, ax.set_title()
    * fig, axes = plt.subplots(nrows=3, ncols=3)
    * plt.tight_layout() - separates graphs a bit better and further apart
    * plt.subplots() - automatically sets the axes, for plt.figure need to set .add_axes()
    * plt.subplot(311) - specifies , 3 rows, 1 column, plotting on 1st row 
    * useful: label (label), line color (c) linestyle(ls), linewidth (lw) marker (marker)
    * marker size (ms), marker colour (mfc), plotting order (zorder)
    * ax.axhline(0) - adds a zero line across the object
    * order not by appearance but by zorder

```python
# sample stateless matplotlib customization
ax.set_ylabel('Temperature\nAnomaly [$^o$C]', fontsize=20)
ax.set_xlabel('Year', fontsize=20)
ax.set_title('Yearly Temperature Anomaly Means for January and August', fontsize=24, y=1.05)
xticklabels = np.arange(1880, 2020, 10) 
# plot extends to year 2020 for extra white space on the right side
ax.xaxis.set_ticks(xticklabels)
ax.set_xticklabels(xticklabels, fontsize=15, rotation=45)
yticklabels = np.arange(-1.5, 2, 0.5)
ax.yaxis.set_ticks(yticklabels) #object ax also has attribute y or xaxis - tick locations/labels are managed
ax.set_yticklabels(yticklabels, fontsize=15)
ax.set_xlim([1880, 2020])
ax.set_ylim([-1.5, 1.5])
ax.grid()
leg.set_title(title='Month', prop = {'size':15})
fig.patch.set_facecolor('lightsteelblue')
```


<br>

* figsize - tuple width and height in inches
* dpi - dots/pixel per inch  vals
* line or bar

<br>

* fig.savefig('name.png')
* plt.imshow(mpimg.imred('name.png')) - to show the image from file 

<br>

* Decorating figures
* linewidth lw
* linestyle ls
* marker="o"
* markersize 

<br>

* other types:
    * .hist()
    * .plot() - lineplot
    * .scatter for scatterplot
    * .bar() 

* Work flow:
    * clean missing
    * .groupby()
    * sort
    * setting mean as a new column avg_gdp_percap = my_data.groupby([‘country’]).mean()[‘gdp_percap’]
    * isolate variable: china = my_data[my_data[‘country’] == ‘Macao SAR, China’]


<br>

* Plot Range
    * set_ylim([1,2]), set_xlim([1,2]) for min and max 

2. Plotly
* unique functionalities such as contour plots, dendrograms, and 3D charts,
* web based connect to API

3. Seaborn
* matplot based
* support numpy and pandas

4. ggplot
* grammar of graphics from r
* integrated with pandas

5. Altair 
* plotting handled automatically - after specifying only links between data columns
* minimal coding