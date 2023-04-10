# ML-Codes
This Readme file is for the Forest Fire Prediction Project.
In this problem the data had a few nan values. These values needed to be removed so I drpped them.
Next I also dropped the day month and year column as some of their dtype was object and dropping them did not hamper the accuracy of the model much.
Then I assigned features and labels and also splitted by train data to create a set of validation data.
I fitted my train data in the model and then checke dthe score for the validation data.
Next I predicted the values for the test data and stored them in a csv file.
