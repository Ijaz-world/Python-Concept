import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# print(sns.get_dataset_names())

penguins=sns.load_dataset('penguins')
print(penguins.head())
print(penguins['species'].value_counts())
print(penguins['island'].value_counts())

# sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g', hue='island', style='sex')
# plt.show()

# sns.histplot(data=penguins, x='body_mass_g', hue='sex', multiple='stack')
# plt.show()

# sns.regplot(data=penguins, x='body_mass_g', y='flipper_length_mm') #-->use to show relationship btw 2 var with line
# plt.show()

# sns.set_style('whitegrid')
# sns.lineplot(data=penguins, x='body_mass_g', y='flipper_length_mm', hue='sex')
# plt.show()

# sns.countplot(data=penguins, x='species', hue='island')
# plt.show()

# sns.barplot(data=penguins, x='species', y='body_mass_g', hue='sex', estimator= np.sum, palette=['skyblue', 'red'])
# plt.show()

# sns.boxplot(data=penguins, x='species', y='body_mass_g', hue='sex', palette='Set2') #-->show us median, 25%, 50% and 75%
# plt.show()       #-> violin plot is also same as box plot just change in shape

# sns.kdeplot(data=penguins, x='body_mass_g', hue='island', fill=True) --> same as histogram shows us using line
# plt.show()

columns=['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'] 
# sns.heatmap(data=penguins[columns].corr(), annot=True, cmap='Greens', linewidths='3', linecolor='Black')#-->show us correaltion
# plt.show()

sns.pairplot(data=penguins, hue='sex') #--> shows relationship btw numeric variables in one figure
plt.show()




