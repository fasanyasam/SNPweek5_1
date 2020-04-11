my_list  = ["cat", "dog", "bean", "ace", "heart"]

#A funtion that accepts a list and the length of words to be extracted from the list 
def right_words(the_list,number):
   #A nested function to help filter the list 
   def my_filter(item):
      #return the length of the items on the list that is equal to the number given 
      return len(item)==number
      #print the filtered items out in a list by giving the ...
      # ...parameters of the function my_filter and the_list and passing it list
   print(list (filter(my_filter,the_list)))



right_words(["cat", "dog", "bean", "ace", "heart"],3)
right_words(["cat", "dog", "bean", "ace", "heart"],5)
right_words([],4)
