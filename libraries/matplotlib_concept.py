import matplotlib.pyplot as plt

# x=['Mon', 'Tue', 'Wed', 'Thur', 'Fri'] # x-axis
# y=[15,20,10,22,17]                      #y-axis
# plt.plot(x,y)
# plt.title('Sugar sales of this Week..')
# plt.xlabel('Days of Week')
# plt.ylabel('Sales per day')
# plt.show()

# months=[1,2,3,4]
# deaths=[700,400,1100,600]
# plt.plot(months,deaths, marker='o', linestyle='--', color='red', linewidth=4, label='Deaths')
# plt.xlabel('Months')
# plt.ylabel('Deaths per month')
# plt.title('Report of deaths per month.!')
# plt.legend(loc='upper left', fontsize=10)
# plt.grid(color='black', linestyle=':',linewidth=1)
# plt.xlim(1,4)
# plt.ylim(300,1200)
# plt.xticks([1,2,3,4], ['Mon1', 'Mon2', 'Mon3', 'Mon4'])
# plt.show()

#**********Bar chart ***************
# product=['A', 'B', 'C', 'D']
# sales=[500,700,1000,300]
# plt.bar(product, sales, color='pink', label='Sales-2025') #we can use plt.barh for horizontal bar
# plt.xlabel('Products')
# plt.ylabel('Sales')
# plt.title('Sales per product !')
# plt.legend()
# plt.show()

#*********Pie chart*************
# regions=['North', 'South', 'East', 'West']
# revenue=[5000,2500,4000,1500]
# plt.pie(revenue, labels=regions, autopct='%1.1f%%', colors=['gold','lightgreen','brown','lightblue'])
# plt.title('Sales according to Regions.!')
# plt.show()


#********Histogram *************--> range
# marks=[76,54,59,66,97,56,38,100,82,78,69,90,81,55,49,89,69,63,94,82]
# plt.hist(marks, bins=5, color='lightgreen', edgecolor='purple')
# plt.xlabel('Marks range')
# plt.ylabel('No. of students')
# plt.title('Score distribution of Students')
# plt.show()

#*******Scatter plot******** -->use to find correaltion between 2 variables
# plt.scatter([1,2,3],[60,65,70], color='red', marker='o', label='Class A')
# plt.scatter([1,2,3],[70,75,80], color='blue', marker='o', label='Class B')
# plt.title('Comparison of 2 Classes')
# plt.xlabel('Hours of study')
# plt.ylabel('Exam Scores')
# plt.legend()
# plt.grid(linestyle=':')
# plt.show()


#*********Subplot **************

x=[1,2,3,4]
y=[10,20,15,25]

plt.subplot(1,2,1)   #--> (fig has 1 row, have 2 columns, and this plot is the first plot)
plt.plot(x,y, color='r')
plt.title('Line chart')

plt.subplot(1,2,2)
plt.bar(x,y)
plt.title('Bar chart')

plt.suptitle('These are subplots')
plt.tight_layout() #--> adjust figures automatically exactly to the window, used exactly before plt.show()
plt.show()

