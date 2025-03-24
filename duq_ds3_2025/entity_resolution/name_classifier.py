import json
import os
import pandas as pd
import pickle
import sklearn.ensemble
import sklearn.linear_model
import sklearn.model_selection
import sklearn.preprocessing
import xgboost as xgb

class NameClassifier():
    def __init__(self, model_type: str):
        """Create a classifier, storing a model and metadata.

        Args:
            model_type (str): can include random forests, logistic
                regression, etc.
        """
        self.model = xgb.XGBClassifier()
        # Initializing the scaler variable for use in the future
        # Add all shared variables to the init function
        self.scaler = None
        self.metadata = None
        
    def train(self, 
              features: pd.DataFrame, 
              labels: pd.Series, 
              test_frac: float = 0.1):
        """Train the model from pandas data

        Args:
            features (pd.DataFrame): input features, dataframe
            labels (pd.Series): input labels
            test_frac (float, optional): fraction of data to preserve 
                for testing. Defaults to 0.1.
        """
        # df['column_name'] is a series
        # a dataframe is multiple columns
        # X is another term for features, y is another term for labels
        self._assess_tf_fraction(labels)

        # We need to scale the data
        # 1. We can set the min to 0 and the max to 1
        # BUT, we need to consider outliers
        # We could remove outliers
        # Or 2. We can use standardization by standard normal
        features_train, features_test, labels_train, labels_test = \
            sklearn.model_selection.train_test_split(features, labels, test_size=test_frac)
        
        self.model.fit(features_train, labels_train)
        pred_labels = self.model.predict(features_test)
        
        # Manual accuracy
        accuracy = (pred_labels == labels_test).sum()/len(labels_test)
        accuracy = (pred_labels == labels_test).mean()

        self.metadata = {}
        self.metadata['training_rows'] = len(features_train)
        self.metadata['accuracy'] = accuracy
        self.metadata['model_type'] = self.model_type
        print('Accuracy on test set is ', accuracy)
        
    def predict(self, features: pd.DataFrame):
        """Predict labels from features
        """
        self.scaler.transform(features)
        self.model.predict(features)

    def save(self, path: str):
        """Save model, scaler, and metadata to files."""
        # data/super_cool_model.stupid_extension
        model_path, _ = os.path.splitext(path)
        scaler_path = model_path + '_scaler.pkl'
        metadata_path = model_path + '.json'
        model_path = model_path + '.pkl'

        with open(model_path, 'wb') as fp:
            pickle.dump(self.model, fp)
        with open(metadata_path, 'w') as fp:
            json.dump(self.metadata, fp)
        
    def load(self, path: str):
        """Load model, scaler, and metadata from MODEL path"""
        model_path, _ = os.path.splitext(path)
        scaler_path = model_path + '_scaler.pkl'
        metadata_path = model_path + '.json'
        model_path = model_path + '.pkl'

        with open(model_path, 'rb') as fp:
            self.model = pickle.load(fp)
        with open(metadata_path, 'r') as fp:
            self.metadata = json.load(fp)

    def _assess_tf_fraction(self, labels: pd.Series):
        """Throw an error for dramatically un-weighted data."""
        if labels.sum() > 0.8*len(labels):
            raise ValueError('Too many trues')
        elif labels.sum() < 0.2*len(labels):
            raise ValueError('Too many falses')

if __name__ == '__main__':
    import duq_ds3_2025.winequality
    wq = duq_ds3_2025.winequality.WineQuality()
    wq.read('data/wine_quality.zip')
    df = wq.df

    labels = df['quality'] > 5
    # features = df[['fixed acidity', 'sulphates', 'alcohol']]
    features = df.drop(['quality'], axis=1)

    lr = NameClassifier('logistic_regression')
    lr.train(features, labels)

    lr = NameClassifier('random_forest')
    lr.train(features, labels)

    lr.save('data/model_rf')
    lr.load('data/model_rf')

    lr.predict(features)