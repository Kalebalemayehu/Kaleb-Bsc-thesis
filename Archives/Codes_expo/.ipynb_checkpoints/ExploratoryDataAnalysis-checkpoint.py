# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:45:56 2020

@author: hwicaksono
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#sklimport numpy as np


# import dataset
df = pd.read_csv(r"D:\Jacobs\Lecture\PTM\Sources\2021\Exploratory Data Analysis and Preprocessing\datasets\customer.csv")

# === Box plot === #

boxplot = df.boxplot(column=['Balance'], by=['Geography', 'Gender'], figsize=(10, 10))
boxplot = df.boxplot(column=['Balance'], figsize=(10, 10))
#plt.show()
boxplot = df.boxplot(column=['Age'], by=['Geography'], figsize=(10, 10))


# === Correlation between variables  === #
df = pd.read_csv(r"D:\Jacobs\Lecture\PTM\Sources\2021\Exploratory Data Analysis and Preprocessing\datasets\winequality-red.csv")
# ==== pairplot ====
plt.figure(figsize=(10, 10))
sns.pairplot(df)
plt.show()

# ==== correlation plot ====
plt.figure(figsize=(10, 10))
sns.heatmap(df.corr(method='pearson'), annot=True)
plt.show()

plt.figure(figsize=(10, 10))
sns.heatmap(df.corr(method='spearman'), annot=True)
plt.show()

plt.figure(figsize=(10, 10))
sns.heatmap(df.corr(method='kendall'), annot=True)
plt.show()

res = df['fixed acidity'].corr(df['citric acid'], method='pearson')


# === line plot === #
df = pd.read_csv(r"D:\Jacobs\Lecture\PTM\Sources\2021\Exploratory Data Analysis and Preprocessing\datasets\covid19_confirmed_transposed.csv")
plt.figure(figsize=(20, 20))

#plot only for a specific column/country
plt.plot(df.Date, df.France, 'b.-')
plt.plot(df.Date, df.Germany, 'g.-')

# plot all columns/countries

for country in df:
    if country != 'Date':
        plt.plot(df['Date'], df[country], marker='.')

plt.xticks(rotation='vertical')
plt.legend()
plt.show()

