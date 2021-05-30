######################## Cleaning The Tweets ##########################
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
filename = 'train.csv'
df = pd.read_csv(filename)
stop = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

df['tweet'] = df['tweet'].apply(lambda x: p.clean(re.sub('#', '',x))) #Tweet Cleaner
df['tweet'] = df['tweet'].apply(lambda x: x.lower()) #Lower Casing
df['tweet'] = df['tweet'].str.replace('[^\w\s]','') #Removing Punctuations
df['tweet'] = df['tweet'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))#STopwords Removal
df['tweet'] = df['tweet'].apply(lambda x: " ".join([lemmatizer.lemmatize(word) for word in x.split()]))

df.to_csv('clean_'+str(filename))