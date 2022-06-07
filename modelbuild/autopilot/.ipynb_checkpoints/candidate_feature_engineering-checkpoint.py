from numpy import nan
from sagemaker_sklearn_extension.externals import Header
from sagemaker_sklearn_extension.impute import RobustImputer
from sagemaker_sklearn_extension.preprocessing import RobustLabelEncoder
from sagemaker_sklearn_extension.preprocessing import RobustStandardScaler
from sagemaker_sklearn_extension.preprocessing import ThresholdOneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Given a list of column names and target column name, Header can return the index
# for given column name
HEADER = Header(
    column_names=[
        'rings', 'sex', 'length', 'diameter', 'height', 'whole_weight',
        'shucked_weight', 'viscera_weight', 'shell_weight'
    ],
    target_column_name='rings'
)


def build_feature_transform():
    """ Returns the model definition representing feature processing."""

    # These features can be parsed as numeric.

    numeric = HEADER.as_feature_indices(
        [
            'length', 'diameter', 'height', 'whole_weight', 'shucked_weight',
            'viscera_weight', 'shell_weight'
        ]
    )

    # These features contain a relatively small number of unique items.

    categorical = HEADER.as_feature_indices(
        ['sex', 'length', 'diameter', 'height']
    )

    numeric_processors = Pipeline(
        steps=[
            (
                'robustimputer',
                RobustImputer(strategy='constant', fill_values=nan)
            )
        ]
    )

    categorical_processors = Pipeline(
        steps=[('thresholdonehotencoder', ThresholdOneHotEncoder(threshold=7))]
    )

    column_transformer = ColumnTransformer(
        transformers=[
            ('numeric_processing', numeric_processors, numeric
            ), ('categorical_processing', categorical_processors, categorical)
        ]
    )

    return Pipeline(
        steps=[
            ('column_transformer', column_transformer
            ), ('robuststandardscaler', RobustStandardScaler())
        ]
    )


def build_label_transform():
    """Returns the model definition representing feature processing."""

    return RobustLabelEncoder(
        labels=[
            '1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '2', '20', '21', '22', '23', '24', '25', '26', '27', '29', '3', '4',
            '5', '6', '7', '8', '9'
        ]
    )
