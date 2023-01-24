from random import *
import matplotlib.pyplot as plt
import numpy as np
import random as rand
import pandas as pd
def solve(n_points,Degree,items_x_y):
    
    Population = []
    NumOfPopulation = 4  
    pop = PopGenerate(Degree,NumOfPopulation)    
    fit = FitnessCalc(pop,items_x_y,Degree, n_points)   
    selected = selection(fit, pop)
    offspring = crossover(selected,Degree)
    mutattion_list = nonunifrom_mutation(offspring)
    print(replacement(fit,pop,Degree,NumOfPopulation,items_x_y,n_points))
    
    print(display_output(pop,items_x_y,Degree,n_points),)
    return []

def read_test_case(file):
    n_points_Degree_list = file.readline().strip("\n").split(" ")
    n_points_Degree_list = list(map(int, n_points_Degree_list))
    n_points=n_points_Degree_list[0]
    Degree=n_points_Degree_list[1]
    items_x_y = []
    for item in range(n_points):
        item = file.readline().split(" ")
        for i in range(2):
            item[i] = float(item[i])
        items_x_y.append(item)
    
    return [n_points, Degree, items_x_y]


def read_test_cases(filename):
    file = open(filename, 'r')
    n_tests = int(file.readline())
    for i in range(n_tests):
        test_case = read_test_case(file)
        n_points = test_case[0]
        Degree = test_case[1]
        items_x_y = test_case[2]
        print("Dataset index=", i)
        print(solve(n_points, Degree, items_x_y))

    file.close()


def PopGenerate(Degree,NumOfPopulation):
    Population = []

    Population.clear()
    for i in range(NumOfPopulation):
        chromosome = []
        for j in range(Degree+1):
            chromosome.append(round(rand.uniform(-10, 10), 2))
        Population.append(chromosome)
    return Population



def FitnessCalc(pop,items_x_y, Degree, n_points):
    Population = pop
    ycalc = 0;
    x = 0

    # DP = [(1, 5), (2, 8), (3, 13), (4, 20)]
    s2 = 0
    s = 0
    s3 = 0
    s4 = 0
    arrDis = []

    fit = []
    for p in range(len(Population)):
        for j in range(n_points):
            x = items_x_y[j][0]
            yact = items_x_y[j][1]
            ytmp = 0
            for i in range(Degree):
                ycalc = 0
                ycalc += ((Population[p][i]) * pow(x, i))
                ytmp = ytmp + ycalc
                Distance = round(pow((ytmp - yact), 2), 2)
            arrDis.append(Distance)

        for m in range(0, int(((len(arrDis) / Degree))), 1):
            s = s + arrDis[m]
        mean1 = s / Degree
        for m2 in range(int(((len(arrDis) / Degree))), int(((len(arrDis) / (Degree / 2)))), 1):
            s2 = s2 + arrDis[m2]
        mean2 = s2 / Degree
        for m3 in range(int(((len(arrDis) / (Degree / 2)))), int(((len(arrDis) / (Degree / 3)))), 1):
            s3 = s3 + arrDis[m3]
        mean3 = s3 / Degree
        for m4 in range(int(((len(arrDis) / (Degree / 3)))), int(((len(arrDis) / (1)))), 1):
            s4 = s4 + arrDis[m4]
        mean4 = s4 / Degree
    if (mean1 != 0.0):
        fit.append(1 / mean1)
    else:
        fit.append(mean1)

    if (mean2 != 0.0):
        fit.append(1 / mean2)
    else:
        fit.append(mean2)
    if (mean3 != 0.0):
        fit.append(1 / mean3)
    else:
        fit.append(mean3)
    if (mean4 != 0.0):
        fit.append(1 / mean4)
    else:
        fit.append(mean4)

    return (fit)
def selection(fit, pop):
    selectedPop = pop
    selectedIndcies = []

    ftRand = rand.randint(0, len(fit) - 1)
    secRand = rand.randint(0, len(fit) - 1)
    tdRand = rand.randint(0, len(fit) - 1)
    frtRand = rand.randint(0, len(fit) - 1)
    if ftRand != secRand:
        for i in range(len(fit)):
            if fit[ftRand] <= fit[secRand]:
                selectedPop[i] = pop[ftRand]
                break
            else:
                continue
    else:
        ftRand = rand.randint(0, len(fit) - 1)
        secRand = rand.randint(0, len(fit) - 1)
        for i in range(len(fit)):
            if fit[ftRand] <= fit[secRand]:
                selectedPop[i] = pop[ftRand]
                break
            else:
                continue

    if tdRand != frtRand:
        for j in range(len(fit)):
            if fit[tdRand] <= fit[frtRand]:
                selectedPop[j] = pop[tdRand]
                break
            else:
                continue
    else:
        tdRand = rand.randint(0, len(fit) - 1)
        frtRand = rand.randint(0, len(fit) - 1)
        for j in range(len(fit)):
            if fit[tdRand] <= fit[frtRand]:
                selectedPop[j] = pop[tdRand]
                break
            else:
                continue

    selectedIndcies = [ftRand, tdRand]

   
    return selectedPop


def crossover(Population,Degree):
    csRate = rand.uniform(0, 1)
   

    if csRate >= 0.07:

        ftPoint = rand.randint(0, Degree)
        secPoint = rand.randint(1, Degree - 1)

        if ftPoint != secPoint:

            if secPoint >= ftPoint:
                secPoint == ftPoint, ftPoint == secPoint
          
                tmp1 = Population[0][ftPoint:secPoint]
                tmp2 = Population[1][ftPoint:secPoint]          

                tmp3 = Population[0][secPoint:]
                tmp4 = Population[1][secPoint:]
                print(tmp3, tmp4)
                Population[0] = Population[0][:ftPoint]
                Population[1] = Population[1][:ftPoint]
                Population[0].extend(tmp2)
                Population[1].extend(tmp1)
                Population[0].extend(tmp3)
                Population[1].extend(tmp4)
                
                return Population

            elif ftPoint > secPoint:

                x = ftPoint - secPoint
                secPoint = secPoint + x
                ftPoint = ftPoint - x
              
                tmp1 = Population[0][ftPoint:secPoint]
                tmp2 = Population[1][ftPoint:secPoint]
                print(tmp1, tmp2)

                tmp3 = Population[0][secPoint:]
                tmp4 = Population[1][secPoint:]
                print(tmp3, tmp4)
                Population[0] = Population[0][:ftPoint]
                Population[1] = Population[1][:ftPoint]
                Population[0].extend(tmp2)
                Population[1].extend(tmp1)
                Population[0].extend(tmp3)
                Population[1].extend(tmp4)
                
                return Population
            else:
                crossover(Population,Degree)

        else:
            crossover(Population,Degree)

    else:
       
        return Population


#
# ###################MUTATION########################################
def calc_delta_upper(offspring):
    pm=0.5
    delta_upper_list = []

    for i in range(len(offspring)):
        delta_upper = []

        for j in range(len(offspring[i])):
            rm = uniform(0,1)
            if rm <= pm:
                delta_upper.append(round(10 - offspring[i][j], 3))
            else :
                delta_upper.append(offspring[i][j])
        delta_upper_list.append(delta_upper)
    return  delta_upper_list


def calc_delta_lower(offspring):
    pm=0.5
    delta_lower_list = []

    for i in range(len(offspring)):
        delta_lower = []

        for j in range(len(offspring[i])):
            rm = uniform(0,1)
            if rm <= pm:
                delta_lower.append(round(offspring[i][j] - (-10), 3))
            else :
                 delta_lower.append(offspring[i][j])

        delta_lower_list.append(delta_lower)
    return  delta_lower_list

def calc_y_value(resulted_delta_lower,resulted_delta_upper):

    y=[]
    for i in range(len(resulted_delta_lower)):
        yvalue = []
        for k in range(len(resulted_delta_lower[i])):
            rhalf = uniform(0, 1)
            # print("random number ------", rhalf )
            if rhalf <= 0.5:
                yvalue.append(resulted_delta_lower[i][k])
            elif rhalf > 0.5:
                yvalue.append(resulted_delta_upper[i][k])
        y.append(yvalue)
    return  y

def calc_t_y (resulted_y):
    current_generation = 1
    max_generation = 5
    parameter_b = 1
    delta_t_y=[]
    for i in range(len(resulted_y)):
        ty_list = []

        for m in range(len(resulted_y[i])):
            r_delta_t_y = uniform(0, 1)
            ty_list.append(
                round(resulted_y[i][m] * (1 - r_delta_t_y ** ((1 - current_generation / max_generation) ** parameter_b)), 3))
        delta_t_y.append(ty_list)
    return delta_t_y

def nonunifrom_mutation(offspring):
    resulted_delta_upper = calc_delta_upper(offspring)
    resulted_delta_lower = calc_delta_lower(offspring)
    resulted_y = calc_y_value(resulted_delta_lower, resulted_delta_upper)
    resulted_delta_t_y = calc_t_y(resulted_y)
    for i in range(len(offspring)):
        for n in range(len(offspring[i])):
            if resulted_y[i][n] == resulted_delta_lower[i][n]:
                offspring[i][n] = round(offspring[i][n] - resulted_delta_t_y[i][n], 3)
            elif resulted_y == resulted_delta_upper[i][n]:
                offspring[i][n] = round(offspring[i][n] + resulted_delta_t_y[i][n], 3)
    return offspring

#
def replacement (fit,pop,Degree,NumOfPopulation,items_x_y,n_points):
    print("############################# Replacement  function######################################################")

    population = PopGenerate(Degree,NumOfPopulation)
    selected=selection(fit, pop)
    # print("Result of function selection :  ","\n", selected)
    fitness_0f_selected=FitnessCalc(selected,items_x_y,Degree, n_points)
    # print("Reslut of fitnness for selection : ","\n", fitness_0f_selected)
    offspring= offspring = crossover(selected,Degree)
    mutattion_list=nonunifrom_mutation(offspring)
    NewPopulation=[]

    for i in range(len(mutattion_list)):
        NewPopulation.append(mutattion_list[i])


    ##step 1 : TO selct best 2 of selected by fitnnes this dic for mapping for fitness by index
    nums={}
    for i in range(len(selected)):
        for j in range(len(selected[i])):
          nums[fitness_0f_selected[i]]=i
    sort_data = sorted(nums.items())
    sort_data_dict = dict(sort_data)
    # print("new dictionary fitness sorted by key ","\n" ,sort_data_dict)
    #####################Keep Best 2  of selected  in temp list####################
    temp=[]
    for key, value in sort_data_dict.items():
        temp.append(selected[value])
        if len(temp) == 2:
            break
    # print("temp of best 2 of selected  population ","\n" , temp)
    ##########Step 2 delete selected parents from popualtion
    NumOfPopulation=4
    for i in range(len(selected)):
        j = 0
        while j < NumOfPopulation:
            if selected[i] == population[j]:
                population.pop(j)
                NumOfPopulation -= 1

            else:
                j += 1
    # print("After deletion of selected parents,pop=","\n",population)
    #######step 3 Add result of mutation to population################################
    for i in range(len(NewPopulation)):
        population.append(NewPopulation[i])
    ##################Step 4 Remove-worst 2  from popualtion (higher fitness) index in dic map index of chromo in  population######
    FitnessOfNewPop = FitnessCalc(NewPopulation,items_x_y,Degree, n_points)
    DicOfNewFitness = {}
    for i in range(len(NewPopulation)):
        for j in range(len(NewPopulation[i])):
            DicOfNewFitness[FitnessOfNewPop[i]] = i
    sort_data_new = sorted(nums.items(), reverse=True)
    sort_data_dict_new = dict(sort_data_new)

    for key, value in sort_data_dict_new.items():
        NewPopulation.pop(value)
        if len(NewPopulation)==2:
            break

    NewPopulation.append(temp)
    return NewPopulation
#

def display_output(pop,items_x_y,Degree,n_points):
            idx=0

            pop = PopGenerate( Degree, 4)
            f = open("output.txt", "w")

            fit = FitnessCalc(pop, items_x_y, Degree, n_points)
            min_fit_value = min(fit);
            indexOfMinFit = fit.index(min_fit_value)
            coefficient = []
            coefficient .append(pop[indexOfMinFit])
            mean_square_error = []
            mean_square_error.append(fit[indexOfMinFit])
         
            f.write("\n coefficients =" + str(coefficient))
            f.write("\n mean square error = " + str(mean_square_error))
            f.close()
            f = open("output.txt", "r")
            print(f.read())
            f.close()




filename = "E:\Year_4_First_Term\Genetic Algorthim\Labs\curve_fitting_input.txt"
read_test_cases(filename)
