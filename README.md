# Email Spam Filter Using Supervised Learning and Naive Bayes Classification

This project is an email spam filter implemented in Python, utilizing supervised learning and Naive Bayes Classification to distinguish between spam and ham (non-spam) emails.

## Overview

This spam filter is based on a supervised learning method, meaning it requires training data to learn patterns and features that are typical of spam messages. Once trained, the filter can classify incoming emails as either spam or ham with a high degree of accuracy.

## Training

### Dataset
To train the spam filter, a large dataset of emails was used along with a document called `!truth.txt`. This document contains labels (OK/SPAM) for each email, indicating whether it is ham or spam.

### Data Structures
During the training stage, the spam filter maintains the following data structures:
- Two lists for email addresses (ham and spam).
- Two lists for links found in emails (ham and spam).
- Two dictionaries for words in ham and spam emails, where each word is a key and the value is the frequency of that word in the respective email type.

A predefined list of "gray words" (common words that are not useful for filtering) is ignored during training.

### Probability Calculation
At the end of the training stage, the word frequencies in the ham and spam dictionaries are converted into probabilities, representing the likelihood of encountering each word in ham or spam emails.

## Usage and Performance

### Classification
After training, the spam filter can classify emails based on the first 1000 unique words. Although this might seem like it limits the information used, it has been shown to be sufficient for accurate classification and improves performance, which is crucial for processing large volumes of emails.

Before processing the email's words, the spam filter checks if the email contains any links or addresses from the ham and spam lists. If a match is found, the email is classified accordingly.

### Scoring
During classification, two scores are maintained: `ham_score` and `spam_score`, which represent the probabilities of the email being ham or spam, respectively. These scores are calculated using Bayes’ Theorem. The email is classified based on the higher score.

### Quality Measurement
The quality of the spam filter can be evaluated using a large dataset and the following formula:
score = (tp + tn) / (tp + tn + 10 * fp + fn)
where:
- `tp` (true positives) is the number of messages correctly identified as ham.
- `tn` (true negatives) is the number of messages correctly identified as spam.
- `fp` (false positives) is the number of messages incorrectly identified as ham.
- `fn` (false negatives) is the number of messages incorrectly identified as spam.

## Results

This project was created as a final assignment for the course RPH (Solving Problems and Games) at CTU FEL OI. After submission, a competition was held among students' spam filters. This spam filter ranked 9th out of 71, achieving an average quality score of 88%.


