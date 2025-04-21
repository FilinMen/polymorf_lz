import pandas as pd

class Processing:

    def data(self):
        df = pd.read_csv('var3.csv')
        

        df1 = df[df['Сумма операции'] < 1000]    # строки, удовлетворяющие условию
        df2 = df[df['Сумма операции'] >= 1000]    # строки, не удовлетворяющие условию

        df1.to_csv('file1.csv') #до 1000
        df2.to_csv('file2.csv') # больше 1000

        self.duplicates1 = df1.duplicated()
        self.duplicates2 = df2.duplicated()

    def __invert__(self):
          
        self.num_duplicates1 = self.duplicates1.sum()
        self.num_duplicates2 = self.duplicates2.sum()
        num = self.num_duplicates1 + self.num_duplicates2
        print(num)
    
    def __del__(self):
        print("DEL")

def main(): 

    pro = Processing()
    pro.data()
    ~pro

if __name__ == "__main__":
    main()