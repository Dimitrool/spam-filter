# spam filter for e-mails based on Supervised Learning and Naive Bayes Classification in Python 

This spam filter is based on supervised learning method, which means that before usage it is needed to give 
it data, on which it will train and understand patterns, which occur in spam messages.

## Training
To train spam filter I used large amount of e-mails together with a document called !truth.txt, 
where for each e-mail (name of the file, where e-mail was stored) there was a label (OK / SPAM) 
characterizing type of the e-mail. During the training stage spam filter maintains following data 
structures:
* two lists for ham and spam addresses
* two list for ham and spam links
* two dictionaries for words from ham and words from spam e-mails, where word is a key
  and number of encounter of this word in an e-mail of particular type is a value

Also, I had a predefined list of so-called "gray words", which are the words which could 
not be useful in e-mail filtering. During the training stage, those words were ignored.

At the end of the training stage values of ham and spam maps will be recalculated to the probability of 
encountering a particular word in spam or ham e-mail.

## Practical usage and quality measurement 
After training stage we have obtained all information needed to distinguish spam e-mails from useful. 
Spam filter classifies the e-mail based on the first 1000 unique words. It seems like we are cutting off 
useful information, but during testing of spam filter it was discovered that 1000 is enough to classsify 
the e-mail. Moreover, it has increased performance of the algorithm, which is crucial in tasks
where it is needed to classify large amount of e-mails.
Before processing words of the e-mail, spam-filter checks, if it contains any links from ham and spam links 
list. If yes then it gives the e-mail an appropriate classification. Same thing with senders.
During actual testing of spam filter, it maintains two variables: ham_score and spam_score which are
depicting the probability of e-mail being spam or ham. It is calculated using the Bayes’ Theorem. 
At the end e-mail will be classified to the category with the highest probability score.

Also, it is possible to compute the quality of the spam filter using large amount of data using following
formula:
score = (tp + tn)/(tp + tn + 10*fp + fn), where
tp - amount of messages that were correctly marked as ham
tn - amount of messages that were correctly marked as spam
fp - amount of messages that were wrongly marked as ham
fn - amount of messages that were wrongly marked as spam

This project was created as a last homework assigment for subject RPH (solving problems 
and games) in CTU FEL OI.
After submitting the project there was a competition between students' spam-filter. 
This spam filter took 9/143 place with average quality score of 88%.




