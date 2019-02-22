import pandas

data_of_csv = pandas.read_csv("./definiciones.csv" , encoding='UTF-8')
print("Print the obtained Data from the CSV \n " , data_of_csv)

data_to_dataframe = pandas.DataFrame(data_of_csv)
print("Print the Obtained Data NOW in a PandasDataFrame \n " , data_to_dataframe)

# I only want the Words that are before the ':' so do the Process
list_of_words = []

for index, data in data_to_dataframe.iterrows():
    word = ""
    if ":" in data["Definicion"]:
        #Because CSV has Column 'Definicion'
        word =  data["Definicion"].split(':')[0]
        list_of_words.append(word)
print("Print the list of words \n " , list_of_words)

words_dataframe = pandas.DataFrame(list_of_words)
words_dataframe.columns = ["Definicion"]
print("Print of the new DataFrame with only the needed words " ,  words_dataframe)
words_dataframe.to_csv('palabras_de_definiciones.csv' , encoding="UTF-8" , index=False)