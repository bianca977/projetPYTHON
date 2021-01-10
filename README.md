# projetPYTHON


Polish companies bankruptcy data Data Set

we had 5 datasets on Polish companies banrupcies named 1year, 2year,3year,4year and 5 year

- 1year : the data contains financial rates from 1st year of the forecasting period and corresponding class label that indicates bankruptcy status after 5 years. The data contains 7027 instances (financial statements), 271 represents bankrupted companies, 6756 firms that did not bankrupt in the forecasting period.
- 2year : the data contains financial rates from 2nd year of the forecasting period and corresponding class label that indicates bankruptcy status after 4 years. The data contains 10173 instances (financial statements), 400 represents bankrupted companies, 9773 firms that did not bankrupt in the forecasting period.
- 3year: the data contains financial rates from 3rd year of the forecasting period and corresponding class label that indicates bankruptcy status after 3 years. The data contains 10503 instances (financial statements), 495 represents bankrupted companies, 10008 firms that did not bankrupt in the forecasting period.
- 4year : the data contains financial rates from 4th year of the forecasting period and corresponding class label that indicates bankruptcy status after 2 years. The data contains 9792 instances (financial statements), 515 represents bankrupted companies, 9277 firms that did not bankrupt in the forecasting period.
- 5year : the data contains financial rates from 5th year of the forecasting period and corresponding class label that indicates bankruptcy status after 1 year. The data contains 5910 instances (financial statements), 410 represents bankrupted companies, 5500 firms that did not bankrupt in the forecasting period.



Each dataset is composed of 65 attributes with the 65th column containing the result
- 1 if the campany had a bankrupcy
- 0 if the campany did not have a bankrupcy

The file data_visualisation.ipynb contains graphs analysing the attributes and their links

The file Projet_Python-Question2.ipynb contains the modelisatin with scikit learn 

And the files app.py, model.pkl, model.pu, et index.html are to create the API
