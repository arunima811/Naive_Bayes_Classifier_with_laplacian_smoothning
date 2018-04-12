# Naive_Bayes_Classifier_with_laplacian_smoothning
The classifier gets trained from the given csv file and can be used to predict the outcome of new set of features.
The approach assume higher relative values for the more favourable conditions for the play. This approach, in my opinion would provide better real life outcomes even with the smaller dataset. I have provided an appropriate split ratio to separate the given .csv file into training data and test data. The training data is classified into dictionary of dictionary for the evaluation of conditional probability of each of the possible features according to a particular class. The accuracy function evaluates the average precision which is returning appropriate values given the limited data. The outcome of a new data provided, is resulting into quite appropriate values.  
main() 
	Assigns appropriate values for a tennis game: 
 Outlook: (Sunny/Overcast/Rainy) as (2/1/0) 
Temp: (Hot/Mild/Cool) as (0/1/2) 
Humidity: (High/Normal) as (0/1) 
Windy: (True/False) as (0/1) 
The Play takes values (1/0) for Play(Yes/No) 
      splitDataset(given_data_set, split_ratio) 
	Divides the given data into training and test set according to a specified ratio into training data and test data. 
    naïve_bayes(training_subset, training_outcomes, test_case, tot_attributes, laplacian_factor) 
	With the given training set 
-calculates individual class probabilities (calls occurences()) 
-calculates dictionary of conditional probabilities of each feature under likelihoods. 
(calls occurences_with_ls) 
- calculates the probability of individual class based on the given in test_sample given the set of features. 
 occurrences(outcome) 
	Probability calculation function without smoothning 
occurrences_with_ls(outcome, tot_outcomes, lf) 
	Probability calculation with smoothning 
 
Formulae Used: 
𝑝𝑟𝑜𝑏𝑎𝑏𝑖𝑙𝑖𝑡𝑦(𝑐𝑙𝑎𝑠𝑠) =    𝐻𝑜𝑤 𝑚𝑎𝑛𝑦  𝑡𝑖𝑚𝑒𝑠 𝑖𝑡 𝑎𝑝𝑝𝑒𝑎𝑟𝑠 𝑖𝑛 𝑐𝑜𝑙𝑢𝑚𝑛 
                         __________________________________________ 
                              𝑐𝑜𝑢𝑛𝑡 𝑜𝑓 𝑎𝑙𝑙 𝑐𝑙𝑎𝑠𝑠 𝑎𝑡𝑡𝑟𝑖𝑏𝑢𝑡e 
𝑃(𝑎𝑡𝑡𝑟𝑖𝑏𝑢𝑡𝑒|𝑐𝑙𝑎𝑠𝑠𝑑𝑎𝑡𝑎)  = 𝑘 + 𝑃(𝑎𝑡𝑡𝑟_𝑡𝑦𝑝𝑒   𝑐𝑙𝑎𝑠𝑠_𝑣𝑎𝑙𝑢𝑒) 
                          ________________________________________________ 
                                      𝑘. (𝑠𝑖𝑧𝑒 𝑜𝑓 𝑑𝑖𝑠𝑡𝑖𝑛𝑐𝑡 𝑎𝑡𝑡𝑟) + 𝑃(𝑐𝑙𝑎𝑠𝑠_𝑣𝑎𝑙𝑢𝑒) 

