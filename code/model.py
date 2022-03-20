import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, plot_roc_curve, plot_confusion_matrix, roc_curve, confusion_matrix

# -----------------------------------
# evaluation - binary classification
# -----------------------------------

def show_classification_report(model,X,y):    
    y_pred = model.predict(X)
    plot_confusion_matrix(model, X, y)
    plt.show()
    print(classification_report(y, y_pred))


def show_roc_curve(model, X, y):
    plot_roc_curve(model, X, y)
    plt.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r',
        label='Chance', alpha=.8)
    plt.show() 
