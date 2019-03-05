from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print("""Welcome to the Pathytje Met Wordcloud Generator!
This program creates a wordlcoud with the most used strings from a column in your data file. 
Please have your dataset ready in the working directory of this python file.
Next, follow the instructions and let the magic happen!
""")
dataset = input("Enter dataset name without quotation marks:")
column_name = input("Enter column name with strings in dataset without quotation marks:")
colour = input("Enter desired colour (blue, red, yellow and green avaialable) without quotation marks:")
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
        else:
            print("{} is not an available colour... Helaas pindakaas!".format(colour.capitalize()))
            exit()
        return("hsl({},100%%, %d%%)".format(col) % np.random.randint(20,90))

    stopwords = set(STOPWORDS)
    data = pd.read_csv(dataset)

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

make_wordcloud(dataset, column_name, colour)
print("""Good job! Thank you for using the Pathytje Met Wordcloud Generator!
Written by Tom van Zantvliet, Maarten Molenaar and Sebastiaan Grosscurt.""")