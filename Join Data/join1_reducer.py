# -*- coding: utf-8 -*-
"""Join1_reducer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mREEMR1JKZWdT_3sv9gOD92B29027BB7
"""

import sys

#Reducer for INNER JOIN 
months = ['Jan','Feb','Mar','Apr','Jun','Jul','Aug','Sep','Nov','Dec'] #place holder for monthname, this list is used to check wether the line is from table a or not
current_word = '' #variable to put word that being checked   
total_word_count = 0 #variable to hold value(total word count) from table b

#load data from system standard input
for line in sys.stdin:
  #split the input to key and value
  line_split = line.split('\t')
  key = line_split[0]
  value = line_split[1]

  #check wether the line is from table a or not
  if value[0:3] not in months:
    #if from table b then mark the key as current_word variable and value as total_word_count
    current_word = key
    total_word_count = value
  else:
    #if from table a then check wether the key is same with the current word 
    if key == current_word :
      daily_value = value.split()
      print('{0} {1} {2} {3}'.format(current_word, daily_value[0],daily_value[1], total_word_count))