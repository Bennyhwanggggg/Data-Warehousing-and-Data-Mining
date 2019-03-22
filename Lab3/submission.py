import numpy as np

def logistic_regression(data, labels, weights, num_epochs, learning_rate): # do not change the heading of the function
	data = np.hstack((np.ones((data.shape[0], 1)), data))
	for epoch in range(num_epochs):
		p = 1/(1+np.exp(-1*np.dot(data, weights)))
		errors = labels-p
		sse = np.sum(np.square(errors))
		gradient = np.dot(errors, data)
		weights = weights + learning_rate*gradient
	return weights


