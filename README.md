
# Topsis

TOPSIS stands for Technique for Order of Preference by Similarity to Ideal Solution. It is a multi-criteria decision-making method used to determine the best option among a set of alternatives based on multiple criteria or attributes.

In TOPSIS, each alternative is evaluated against a set of criteria, and a score is assigned to each alternative for each criterion. The method then calculates the distance of each alternative from the ideal solution (which represents the best performance for each criterion) and the distance of each alternative from the worst solution (which represents the worst performance for each criterion).

Finally, TOPSIS ranks the alternatives based on their closeness to the ideal solution and their distance from the worst solution. The alternative with the highest score is considered the best choice.

TOPSIS is widely used in fields such as engineering, management, and economics to make complex decisions that involve multiple criteria.


## Documentation
The Documentation is available 
[here](https://pypi.org/project/Topsis-Maanya-102003366/).

This is a Python Package that can be used by installing the package as follows:

```
>> pip install Topsis-Maanya-102003366
```

#### How To Run:
```
>> python topsis data.csv "1,1,1,1" "+,+,-,+" result.csv
```

The input arguments are:
1) An input csv file (For eg. data.csv) that contains the input of certain attributes/features for each of the particular record. 
                                                               
                                                               
For example: If we are trying to find the best sample among 5 
samples on the basis of measures of central tendancy(mean,meadian,mode) and dispersion(range, standard deviation).     
To Run in commandline:

2) Input the weights for each input feature. Basically the weight determines the relative importance or priority of each criterion in a decision-making problem.

3) Input the impact for each input feature. The impact in TOPSIS determines the direction or positive/negative effect of each criterion on the decision-making problem.

4) The result file where the final result in form of a table will be stored with the corresponding rank of each record. It should be a csv file(For eg. result.csv)

#### Sample Input:

The decision matrix should be constructed with each row representing a Model alternative, and each column representing a criterion like Accuracy, R2, Root Mean Squared Error, Correlation, and many more.



Input Image:

![image](https://user-images.githubusercontent.com/74601983/223729422-621fe94e-535a-411c-92ca-5944f1bf7257.png)


#### Output Image: 

![image](https://user-images.githubusercontent.com/74601983/223729586-4e2716c8-4ef5-45c5-ba37-4bd5e71d6ec6.png)
