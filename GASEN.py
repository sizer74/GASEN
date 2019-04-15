# Genetic Algorithm Selection of Ensemble Networks
#
# This script uses a genetic algorithm to selection the optimum
# weighting of networks in an ensemble. The algorithm starts with random
# weights and then starts to minimise the selected value in the
# function ensemble_fitness.

import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as pyplot
from sklearn import linear_model

from loadData import load_data
from ensembleFitness import ensemble_fitness
from weightedEnsemble import weighted_ensemble
import GA

UPPER_BOUND = 1
LOWER_BOUND = 0

# Loading in data
data = pd.read_csv("student-mat.csv", sep=";")
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

# Predict field
predict = "G3"

# Dropping out the predicted field
x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

# Retrieve network objects from networks folder
models = load_data()

weights = [1, 2, 3, 4]

# Create objective function
objective_function = lambda w: ensemble_fitness(w, models, x_test, y_test, 'mse')

# Set Genetic Algorithm parameters

# Run Genetic Algorithm to optimise objective function
parent_, fitness_, history = GA.genetic_algorithm(weights, objective_function)

# Return weights

# Display optimised network ensemble accuracy details
results = weighted_ensemble(weights, models, x_test)
pyplot.scatter(results, y_test)
pyplot.show()
