import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

if 'transformer' not in globals():
    try:
        from mage_ai.data_preparation.decorators import transformer
    except ImportError:
        def transformer(fn):
            return fn

if 'test' not in globals():
    try:
        from mage_ai.data_preparation.decorators import test
    except ImportError:
        def test(fn):
            return fn


@transformer
def evaluate(df, *args, **kwargs):
    y_true = df['target']
    y_pred = df['predicted']

    print('Confusion matrix:')
    cm = pd.crosstab(y_true, y_pred, rownames=['actual'], colnames=['predicted'])
    print(cm)

    metrics = pd.DataFrame({
        'metric': ['accuracy', 'precision', 'recall', 'f1_score'],
        'value': [
            round(accuracy_score(y_true, y_pred), 3),
            round(precision_score(y_true, y_pred, average='macro'), 3),
            round(recall_score(y_true, y_pred, average='macro'), 3),
            round(f1_score(y_true, y_pred, average='macro'), 3),
        ]
    })
    print('\nClassification Metrics:')
    print(metrics)
    return metrics


@test
def test_metrics(output, *args):
    """Independent improvement (Neelanjana Prakash, 23BCS176):
    Added a @test quality gate to the evaluate_model block.
    Previously this block had no assertion; a corrupt predictions DataFrame
    could silently produce NaN metrics. This gate catches that early.
    """
    assert len(output) == 4, "Expected 4 metric rows (accuracy, precision, recall, f1_score)"
    for _, row in output.iterrows():
        assert 0.0 <= row['value'] <= 1.0, (
            f"Metric '{row['metric']}' value {row['value']} is outside [0, 1]"
        )
