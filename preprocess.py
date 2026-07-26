import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

def trans_SMS(SMS):
    SMS = SMS.lower()    # Covert SMS in Lower case
    SMS = nltk.word_tokenize(SMS)    # Create list of words in SMS
    new_sms = []    
    for i in SMS:
        if i.isalnum():    # Removing Special Characters
            new_sms.append(i)

    SMS = new_sms[:]
    new_sms.clear()
    for i in SMS:
        if i not in stopwords.words('english') and i not in string.punctuation:    # Removing punctuation and stopword
            new_sms.append(i)
    
    SMS = new_sms[:]
    new_sms.clear()
    ps = PorterStemmer()
    for i in SMS:
        new_sms.append(ps.stem(i))

        
    return ' '.join(new_sms)
