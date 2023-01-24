# Smooth-Curve-Fitting-Problem-GeneticAlg

About the problem:
Curve fitting is the process of constructing a curve, or mathematical function (polynomial equation) that has the best fit to a series of data points, possibly subject to constraints. In smooth curve fitting, the function is constructed to approximately fit the data. Given a set of points, we would like to fit a curve to them using a polynomial equation.

What you are required to do:
Write a genetic algorithm to find the best coefficients that would make the distance between the polynomial function and the points minimum. (A solved example is provided in lab 2)


Important remarks:
1. The first thing you need to do is to think about how you will encode the solution
in your chromosome and what the objective function will be.
2. You should use a floating-point representation of the chromosome.
3. You can try different population sizes to see how this will affect your results. The maximum number of generations is up to you.
4. Initialize the genes such that their values are in the range [-10,10].
5. Implement tournament selection, 2-point crossover, non-uniform mutation, and elitist replacement.
6. You must read the input from the given file and write the output to a file. The output should consist of the dataset index, the coefficients of the polynomial function, and its mean square error.
