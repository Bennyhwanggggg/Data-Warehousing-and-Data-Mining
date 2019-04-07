## import modules here 
from collections import Counter

################# Question 1 #################

def multinomial_nb(training_data, sms):# do not change the heading of the function
    
    def preprocess(preprocessed_data):
        processed_data = dict()
        for data in preprocessed_data:
            if data[1] not in processed_data:
                processed_data[data[1]] = data[0]
            else:
                processed_data[data[1]] = Counter(processed_data[data[1]])+Counter(data[0])
        return processed_data
    
    result, total_ham, total_spam = 1, 0, 0
    processed_data = preprocess(training_data)
    for data in training_data:
        if data[1] == 'ham':
            total_ham += 1
        elif data[1] == 'spam':
            total_spam += 1
    smoothing = set().union(processed_data['spam'].keys(), processed_data['ham'].keys())
    for msg in sms:
        if msg not in smoothing:
            continue
        n_ham = 1 + processed_data['ham'][msg] if msg in processed_data['ham'] else 1
        ham = n_ham / (len(smoothing) + sum(processed_data['ham'].values()))
        n_spam = 1 + processed_data['spam'][msg] if msg in processed_data['spam'] else 1
        spam = n_spam / (len(smoothing) + sum(processed_data['spam'].values()))
        result*=(spam/ham)
    return result*total_spam/total_ham
        
        
                                              
                                              
        