import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn.decomposition import PCA
from sklearn import metrics
from sklearn.metrics import confusion_matrix as cf
from sklearn.cross_validation import cross_val_score

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier


# Partitioning data to input and target variable
train_data = pd.read_csv('datasets/train.csv')
test_data = pd.read_csv('datasets/test.csv')

train_pts = train_data.drop('Activity', axis=1)
train_labels = train_data['Activity']

test_pts = test_data.drop('Activity', axis=1)
test_labels = test_data['Activity']


# Classifying and plotting after applying PCA
pca = PCA(n_components=200)
train_pca = pca.fit_transform(train_pts, y=train_labels)
# print(pca.explained_variance_ratio_)
test_pca = pca.transform(test_pts)
# print(pca.explained_variance_ratio_)


def classify(train, train_labels, test, test_labels, method):
    k_range = list(range(1, 31, 2))
    k_scores_train = []
    k_scores_test = []
    k_scores_cv_train = []
    for k in k_range:
        clf = KNeighborsClassifier(n_neighbors=k)
        clf.fit(train, train_labels)

        # scores_train = clf.score(train, train_labels)
        # k_scores_train.append(scores_train)

        # scores_test = clf.score(test, test_labels)
        # k_scores_test.append(scores_test)

        scores_cv_train = cross_val_score(clf, train, train_labels, cv=100, scoring='accuracy')
        k_scores_cv_train.append(scores_cv_train.mean())

    return k_scores_cv_train


k_scores_test = [0.79877841873091282, 0.80692229385816083, 0.80963691890057687, 0.80726162198846285, 0.80726162198846285, 0.81099423142178484, 0.81167288768238888, 0.81506616898540885, 0.81303020020359684, 0.81506616898540885, 0.81438751272480492, 0.81642348150661692, 0.81336952833389886, 0.81438751272480492, 0.8120122158126909]

k_scores_train = [1.0, 0.99632752992383022, 0.98898258977149078, 0.98394994559303595, 0.97946137105549513, 0.97701305767138191, 0.97361262241566926, 0.97102829162132753, 0.96721980413492925, 0.96354733405875947, 0.96300326441784545, 0.96150707290533188, 0.96069096844396085, 0.9575625680087051, 0.95620239390642003]

k_scores_cv_train = classify(train_pca, train_labels, test_pca, test_labels, method)

plt.plot(k_range, k_scores_train, label="Train Accuracy")
plt.plot(k_range, k_scores_test, label="Test Accuracy")
plt.plot(k_range, k_scores_cv_train, label="Cross validation Accuracy")
plt.xlabel("Value of K for KNN")
plt.ylabel("KNN Accuracy")
plt.title("Accuracy V/S no of neighbors")
plt.legend(loc='best')
plt.show()
