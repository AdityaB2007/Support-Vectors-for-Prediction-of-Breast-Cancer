# dataset file: 

from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.metrics import roc_curve, auc, roc_auc_score
from bioinfokit.visuz import stat
from sklearn.metrics import precision_recall_curve, average_precision_score, plot_precision_recall_curve
