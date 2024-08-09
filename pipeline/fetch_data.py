import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split


def main():
    dataset = datasets.load_iris()
    dataset = pd.DataFrame(data= np.c_[dataset['data'], dataset['target']], columns= dataset['feature_names'] + ['target'])
    # replace target values with target names
    dataset['target'] = dataset['target'].replace({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

    train, test = train_test_split(dataset, test_size=0.2)
    train, val = train_test_split(train, test_size=0.2)

    train.to_csv('data/train.csv', index=False)
    val.to_csv('data/val.csv', index=False)
    test.to_csv('data/test.csv', index=False)


if __name__ == '__main__':
    main()