# ML-Codes
This readme file is for the project Housing Prices.
In this project first of all I analysed the train data. This data required some processing as there were many columns that were not as good as to be used as features.
So I dropped the columns that had a high percentage of nan values.
Next there were also some columns that contained nan values but in low percentage.
so in order to remove these nan values I performed imputation and imputed mean and mode values in columns respectively.
After that the same operations needed to be performed on the test data as it was also not pre-processed.
Then I observed that a significant number of features had their dtype as object. This could not be fitted in the model directly. So encoding was required.
If normal encoding was done then there could have been an issue of averages which could later on lead to overfitting.
Therefore I used one-hot encoding in this. I also noticed that the test and train data had different categories in some columns. 
So to avoid any error at time of fitting and prediction it was required that the train and test data had same columns after encoding. 
So I conactenated the data row wise and after that applied one hot encoding.
Next I splitted the data in the original form.
I also splitted my train data in two parts to create some validation data.
Next I fitted the train data in the Random Forest Regressor model as this was a regression problem.
Then I used my validation data to check the score of the trained model.
Then I predicted the house prices of the test data and created a csv file separately for it.
