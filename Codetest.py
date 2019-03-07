from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print("""Welcome to the Pythatje Met Wordcloud Generator!
This program creates a wordlcoud with the most used strings from a column in your data file.
Please have your dataset ready in the working directory of this python file.
Next, follow the instructions and let the magic happen!
""")

def datasetinput():
    global dataset
    global data
    dataset = input("Enter dataset name without quotation marks:")
    try:
        open(dataset)
    except Exception:
        result = "Oops! {} does not exist in your directory! Try again!".format(dataset)
        print(result)
        datasetinput()
    data = pd.read_csv(dataset)
    dataset = data
    print("Dataset found, lets continue...")

def column_nameinput():
    global column_name
    column_name = input("Enter column name with strings in dataset without quotation marks:")
    if {column_name}.issubset(dataset.columns):
        print("Column exists, let's continue...")
    else:
        print("Oops! {} is not a column in your dataset! Try again!".format(column_name))
        column_nameinput()

def colourinput():
    global colour
    colour = input("Enter desired colour (blue, red, yellow and green available) without quotation marks:")
    colour = colour.lower()
    if colour != "blue" and colour != "red" and colour != "yellow" and colour != "green":
        print("Oops! {} is not an available colour! Try again!".format(colour.capitalize()))
        colourinput()
    print("{} is a great choice! In a few moments your wordcloud will appear!".format(colour.capitalize()))

def make_wordcloud(dataset, column_name, colour):
    def colourchange(word, font_size, position,orientation,random_state=None, **kwargs):
        if colour == "blue":
            col = 245
        elif colour == "red":
            col = 0
        elif colour == "yellow":
            col = 50
        elif colour == "green":
            col = 110
        return("hsl({},100%%, %d%%)".format(col) % np.random.randint(20,90))
    stopwords = set(STOPWORDS)
    data = dataset
    wordcloud = WordCloud(
                              background_color='white',
                              stopwords=stopwords,
                              max_words=200,
                              max_font_size=60,
                              random_state=42
                             ).generate(str(data[column_name]))

    wordcloud.recolor(color_func = colourchange)
    print(wordcloud)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()


datasetinput()
column_nameinput()
colourinput()
make_wordcloud(dataset, column_name, colour)
print("""Good job! Thank you for using the Pythtje Met Wordcloud Generator!
Written by Tom van Zantvliet, Maarten Molenaar and Sebastiaan Grosscurt.
v1.0 as part of the LUC Programming Course""")