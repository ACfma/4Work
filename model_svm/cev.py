"""CEV.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F3zxDwhSS79kzDAXoRjYyRW6HCT4Z0XL
"""

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

def cum_explained_variance(dataset):
    '''
    cum_explained_variance return a 1D array that contain the cumulative explained\
    variance of a dataset and a plot of cumulative explained variance vs number of\
    possible components.

    Parameters
    ----------
    dataset : array
        2D array obtained from all images.
    Returns
    -------
    cum_var_exp : array
        2D array with shape (n_samples)
    axs : seaborn lineplot

    '''
    standardized_data = StandardScaler().fit_transform(dataset)
    pca = PCA()
    pca.fit_transform(standardized_data)
    ex_var_ratio = pca.explained_variance_ratio_
    cum_var_exp = np.cumsum(ex_var_ratio)

    #x_in = np.linspace(0, dataset.shape[0]-1, dataset.shape[0])
    axs = sns.lineplot(data = cum_var_exp, label='cumulative explained variance')
    plt.xlabel("Number of components")
    plt.ylabel("Cumulative explained variance (%)")
    plt.axhline(y=0.95, color='k', linestyle='--', label='95% Explained Variance')
    plt.axhline(y=0.90, color='c', linestyle='--', label='90% Explained Variance')
    plt.axhline(y=0.85, color='r', linestyle='--', label='85% Explained Variance')
    plt.axhline(y=0.80, color='y', linestyle='--', label='80% Explained Variance')
    plt.legend(loc='best')
    plt.legend(loc='best')
    plt.title("Cumulative explained variance vs number of components")
    plt.show(block = False)

    return cum_var_exp, axs
