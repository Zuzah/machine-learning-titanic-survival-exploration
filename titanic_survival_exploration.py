
# coding: utf-8

# # Lab: Titanic Survival Exploration with Decision Trees

# ## Getting Started
# In this lab, you will see how decision trees work by implementing a decision tree in sklearn.
# 
# We'll start by loading the dataset and displaying some of its rows.

# In[ ]:


# Import libraries necessary for this project
import numpy as np
import pandas as pd
from IPython.display import display # Allows the use of display() for DataFrames

# Pretty display for notebooks
get_ipython().run_line_magic('matplotlib', 'inline')

# Set a random seed
import random
random.seed(42)

# Load the dataset
in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)

# Print the first few entries of the RMS Titanic data
display(full_data.head())


# Recall that these are the various features present for each passenger on the ship:
# - **Survived**: Outcome of survival (0 = No; 1 = Yes)
# - **Pclass**: Socio-economic class (1 = Upper class; 2 = Middle class; 3 = Lower class)
# - **Name**: Name of passenger
# - **Sex**: Sex of the passenger
# - **Age**: Age of the passenger (Some entries contain `NaN`)
# - **SibSp**: Number of siblings and spouses of the passenger aboard
# - **Parch**: Number of parents and children of the passenger aboard
# - **Ticket**: Ticket number of the passenger
# - **Fare**: Fare paid by the passenger
# - **Cabin** Cabin number of the passenger (Some entries contain `NaN`)
# - **Embarked**: Port of embarkation of the passenger (C = Cherbourg; Q = Queenstown; S = Southampton)
# 
# Since we're interested in the outcome of survival for each passenger or crew member, we can remove the **Survived** feature from this dataset and store it as its own separate variable `outcomes`. We will use these outcomes as our prediction targets.  
# Run the code cell below to remove **Survived** as a feature of the dataset and store it in `outcomes`.

# In[ ]:


# Store the 'Survived' feature in a new variable and remove it from the dataset
outcomes = full_data['Survived']
features_raw = full_data.drop('Survived', axis = 1)

# Show the new dataset with 'Survived' removed
display(features_raw.head())


# The very same sample of the RMS Titanic data now shows the **Survived** feature removed from the DataFrame. Note that `data` (the passenger data) and `outcomes` (the outcomes of survival) are now *paired*. That means for any passenger `data.loc[i]`, they have the survival outcome `outcomes[i]`.
# 
# ## Preprocessing the data
# 
# Now, let's do some data preprocessing. First, we'll one-hot encode the features.

# In[ ]:


features = pd.get_dummies(features_raw)


# And now we'll fill in any blanks with zeroes.

# In[ ]:


features = features.fillna(0.0)
display(features.head())


# ## (TODO) Training the model
# 
# Now we're ready to train a model in sklearn. First, let's split the data into training and testing sets. Then we'll train the model on the training set.

# In[ ]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, outcomes, test_size=0.2, random_state=42)


# In[ ]:


# Import the classifier from sklearn
from sklearn.tree import DecisionTreeClassifier

# TODO: Define the classifier, and fit it to the data
model = DecisionTreeClassifier()
model.fit(X_train, y_train)


# ## Testing the model
# Now, let's see how our model does, let's calculate the accuracy over both the training and the testing set.

# In[ ]:


# Making predictions
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Calculate the accuracy
from sklearn.metrics import accuracy_score
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)
print('The training accuracy is', train_accuracy)
print('The test accuracy is', test_accuracy)


# # Exercise: Improving the model
# 
# Ok, high training accuracy and a lower testing accuracy. We may be overfitting a bit.
# 
# So now it's your turn to shine! Train a new model, and try to specify some parameters in order to improve the testing accuracy, such as:
# - `max_depth`
# - `min_samples_leaf`
# - `min_samples_split`
# 
# You can use your intuition, trial and error, or even better, feel free to use Grid Search!
# 
# **Challenge:** Try to get to 85% accuracy on the testing set. If you'd like a hint, take a look at the solutions notebook next.

# In[ ]:


# TODO: Train the model
model = DecisionTreeClassifier(max_depth=6, min_samples_leaf=6, min_samples_split=10)
model.fit(X_train, y_train)

# TODO: Make predictions
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# TODO: Calculate the accuracy
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)

print('The training accuracy is', train_accuracy)
print('The test accuracy is', test_accuracy)

