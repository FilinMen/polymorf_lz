import pandas as pd

class Processing:

    def data():
        df = pd.read_csv('var3.csv')
        

        df1 = df[df['Сумма операции'] < 1000]    # строки, удовлетворяющие условию
        df2 = df[df['Сумма операции'] >= 1000]    # строки, не удовлетворяющие условию

        df1.to_csv('file1.csv') #до 1000
        df2.to_csv('file2.csv') # больше 1000

        duplicates1 = df1.duplicated()
        duplicates2 = df2.duplicated()

        # подсчет дубликатов
        num_duplicates1 = duplicates1.sum()
        num_duplicates2 = duplicates2.sum()
        num = num_duplicates1 + num_duplicates2

    def __add__():
          
        num_duplicates1 = duplicates1.sum()
        num_duplicates2 = duplicates2.sum()
        num = num_duplicates1 + num_duplicates2
        print(num)