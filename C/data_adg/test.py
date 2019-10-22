import pandas as pd

# List of Tuples
students = [('jack', 34, 'Sydeny', 'Australia'),
            ('Riti', 30, 'Delhi', 'India'),
            ('Vikas', 31, 'Mumbai', 'India'),
            ('Neelu', 32, 'Bangalore', 'India'),
            ('John', 16, 'New York', 'US'),
            ('Mike', 17, 'las vegas', 'US')]
# Create a DataFrame object
dfObj = pd.DataFrame(students, columns=['Name', 'Age', 'City', 'Country'], index=['a', 'b', 'c', 'd', 'e', 'f'])
modDfObj = dfObj.append({'Name' : 'Sahil' , 'Age' : 22} , ignore_index=True)
print(modDfObj)