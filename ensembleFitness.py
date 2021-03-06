def ensemble_fitness(weights, models, inputs, targets, value):
    import numpy as np
    import sklearn
    from sklearn import linear_model
    from sklearn import metrics
    from weightedEnsemble import weighted_ensemble

    fitness = []

    # Normalise weights
    weights = sklearn.preprocessing.normalize(weights, axis=1, norm='l1')

    for i in range(len(weights)):
        predictionsSum = weighted_ensemble(weights[i-1], models, inputs)

        # Calculating bias and variance for use in error if selected
        bias = (np.mean(predictionsSum)-np.mean(targets))**2
        variance = np.var(predictionsSum-targets)

        # Setting output fitness value
        if value == "mse":
            ensembleFit = metrics.mean_squared_error(predictionsSum, targets)
        elif value == "mae":
            ensembleFit = metrics.mean_absolute_error(predictionsSum, targets)
        elif value == "bias":
            ensembleFit = bias
        elif value == "variance":
            ensembleFit = variance
        elif value == "error":
            ensembleFit = bias+variance
        else:
            # If error with input then set it to mse as default
            ensembleFit = metrics.mean_squared_error(predictionsSum, targets)

        fitness.append(ensembleFit)

    # Returning fitness value to minimise
    return fitness
