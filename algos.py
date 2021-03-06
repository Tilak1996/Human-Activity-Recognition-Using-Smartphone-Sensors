import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn.decomposition import PCA
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix as cf
from sklearn.cross_validation import cross_val_score

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

train_data = pd.read_csv('newdatasets/train.csv')
test_data = pd.read_csv('newdatasets/test.csv')

train_data.dropna(inplace=True)
test_data.dropna(inplace=True)

train_pts = train_data.drop('Activity', axis=1)
train_labels = train_data['Activity']

test_pts = test_data.drop('Activity', axis=1)
test_labels = test_data['Activity']


pca = PCA(n_components=200,whiten=True)
train_pca = pca.fit_transform(train_pts, y=train_labels)
# print(pca.explained_variance_ratio_)
test_pca = pca.transform(test_pts)
print(pca.explained_variance_ratio_.sum())

# accuracy values on pca sets
# scores_train = [0.96028291621327533, 0.98027747551686617, 0.98531011969532101, 0.98762241566920561, 0.99020674646354734, 0.98966267682263331, 0.99075081610446136, 0.99265505984766045, 0.99143090315560389, 0.99319912948857458, 0.99306311207834608, 0.99211099020674642, 0.9934711643090316, 0.9936071817192601, 0.99279107725788907, 0.99387921653971711, 0.99319912948857458, 0.99387921653971711, 0.99306311207834608, 0.99292709466811757, 0.9936071817192601, 0.9936071817192601, 0.99265505984766045, 0.99428726877040263, 0.99319912948857458, 0.99387921653971711, 0.99333514689880309, 0.99333514689880309, 0.99415125136017413]

# scores_test = [0.84458771632168306, 0.88123515439429934, 0.88123515439429934, 0.88394977943671527, 0.8961655921275874, 0.90125551408211746, 0.8982015609093994, 0.89888021717000344, 0.89243298269426541, 0.90159484221241937, 0.90600610790634539, 0.90329148286392946, 0.90261282660332542, 0.89989820156090938, 0.90498812351543945, 0.90430946725483541, 0.90125551408211746, 0.90430946725483541, 0.90227349847302341, 0.90532745164574147, 0.90566677977604348, 0.90091618595181544, 0.90091618595181544, 0.90736342042755347, 0.90329148286392946, 0.90634543603664741, 0.90566677977604348, 0.90397013912453339, 0.90770274855785549]

# scores_cv_train = [0.87605015468140923, 0.90589959235680229, 0.91121056234935094, 0.90920489102244706, 0.91598393045429816, 0.91662176490529046, 0.91692868217377954, 0.91937647538876788, 0.91903629354454874]

# accuracy values on original sets

# scores_test = [0.91414998303359352, 0.91856124872751954, 0.91720393620631147, 0.90973871733966749, 0.92365117068204949, 0.92161520190023749, 0.91686460807600945, 0.92297251442144557, 0.92025788937902953, 0.92127587376993558, 0.92161520190023749, 0.92025788937902953, 0.92195453003053951, 0.92093654563963356, 0.92399049881235151, 0.92025788937902953, 0.92806243637597552, 0.92365117068204949, 0.92772310824567361, 0.92399049881235151, 0.92297251442144557, 0.92127587376993558, 0.92263318629114355, 0.92161520190023749, 0.92466915507295555, 0.92399049881235151, 0.92738378011537159, 0.92161520190023749, 0.92229385816084153]

# scores_train = [0.96028291621327533, 0.98027747551686617, 0.98531011969532101, 0.98762241566920561, 0.99020674646354734, 0.98966267682263331, 0.99075081610446136, 0.99265505984766045, 0.99143090315560389, 0.99319912948857458, 0.99306311207834608, 0.99211099020674642, 0.9934711643090316, 0.9936071817192601, 0.99279107725788907, 0.99387921653971711, 0.99319912948857458, 0.99387921653971711, 0.99306311207834608, 0.99292709466811757, 0.9936071817192601, 0.9936071817192601, 0.99265505984766045, 0.99428726877040263, 0.99319912948857458, 0.99387921653971711, 0.99333514689880309, 0.99333514689880309, 0.99415125136017413]

# from sklearn.metrics import roc_auc_score, precision_score, recall_score, accuracy_score, confusion_matrix
# from sklearn.ensemble import RandomForestClassifier
# scores_cv_train = []
# for n in range(90, 300, 10):
#   rf = RandomForestClassifier(n_estimators=90, n_jobs=4, min_samples_leaf=10)
#   scores_cv = cross_val_score(rf, train_pca, train_labels, cv=100, scoring='accuracy')
#   scores_cv_train.append(scores_cv.mean())
#   print scores_cv_train

# plotting  confusion matrix
def plot_confusion(classifier, test_pts, test_labels):
    classes = ['STANDING',
               'SITTING',
               'LYING',
               'WALKING',
               'WALKING_DOWNSTAIRS',
               'WALKING_UPSTAIRS']
    cl = ['STANDING',
               'SITTING',
               'LYING',
               'WALK',
               'WALK_DOWN',
               'WALK_UP']
    pred_label = classifier.predict(test_pts)
    # print(true_label)
    result = cf(test_labels, pred_label, labels=classes)
    res_nor = np.ndarray((6, 6), dtype=float)
    # for i in range(0, 6):
    #     s = result[i].sum()
    #     for j in range(0, 6):
    #         res_nor[i][j] = float(result[i][j] / s)
    print(result)
    # print(res_nor)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(result)
    # plt.matshow(result)
    fig.colorbar(cax)
    ax.set_xticklabels([''] + cl)
    ax.set_yticklabels([''] + cl)
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.legend(loc='best')
    plt.show()

rf = RandomForestClassifier(n_estimators=200, n_jobs=4, min_samples_leaf=10)  # 0.90566677977604348
rf.fit(train_pca, train_labels)
print rf.score(test_pca, test_labels)
plot_confusion(rf, test_pca, test_labels)

# plotting accuracy graphs

# n_estim = list(range(10, 300, 10))
# plt.plot(n_estim, scores_train, label="Training Accuracy")
# plt.plot(n_estim, scores_test, label="Testing Accuracy")
# plt.xlabel("n_estimators")
# plt.ylabel("Accuracy of random forest")
# plt.title("Accuracy V/S no of estimators(on original data)")
# plt.legend(loc='best')
# plt.show()


# precision vs recall
rf = RandomForestClassifier(n_estimators=200, n_jobs=4, min_samples_leaf=10)  # 0.90566677977604348
rf.fit(train_pca, train_labels)
y_pred = rf.predict(test_pca)
print rf.score(test_pca, test_labels)

# print y_pred
# print test_pca
target_names = ['STANDING', 'SITTING', 'LYING', 'WALKING', 'WALKING_DOWNSTAIRS',
                'WALKING_UPSTAIRS']

print(classification_report(test_labels, y_pred, target_names=target_names))
