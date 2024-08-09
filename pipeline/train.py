import os
import pandas as pd
import mlflow
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from mlflow.models import infer_signature

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)


def classification_metrics(y_true, y_pred):
    """
    Calculate and return a dictionary of classification metrics.

    Args:
    y_true (list or array-like): True labels.
    y_pred (list or array-like): Predicted labels.

    Returns:
    dict: Dictionary containing accuracy, precision, recall, f1 score, and confusion matrix.
    """
    metrics = {}
    metrics["accuracy"] = accuracy_score(y_true, y_pred)
    metrics["precision"] = precision_score(y_true, y_pred, average="weighted")
    metrics["recall"] = recall_score(y_true, y_pred, average="weighted")
    metrics["f1_score"] = f1_score(y_true, y_pred, average="weighted")

    return metrics


def main():

    os.environ["MLFLOW_TRACKING_URI"] = "http://localhost:8080"

    mlflow.set_experiment("iris")

    train = pd.read_csv("data/train.csv")
    val = pd.read_csv("data/val.csv")
    test = pd.read_csv("data/test.csv")

    target = "target"
    features = [col for col in train.columns if col != target]

    x_train = train[features]
    y_train = train[target]
    x_val = val[features]
    y_val = val[target]
    x_test = test[features]
    y_test = test[target]

    with mlflow.start_run():
        print("Training model")
        model = Pipeline(
            [
                ("scaler", StandardScaler()),
                (
                    "classifier",
                    RandomForestClassifier(n_estimators=10, random_state=42),
                ),
            ]
        )

        model.fit(x_train, y_train)

        # Registrando um modelo com assinatura
        signature = infer_signature(x_train, y_train)
        mlflow.sklearn.log_model(model, "model", signature=signature)

        y_pred = model.predict(x_val)
        metrics = classification_metrics(y_val, y_pred)
        mlflow.log_metrics(metrics)

        # Logando dados
        mlflow.log_input(
            dataset=mlflow.data.from_pandas(train), context="train_dataset"
        )

        mlflow.log_input(dataset=mlflow.data.from_pandas(val), context="val_dataset")

        mlflow.log_input(dataset=mlflow.data.from_pandas(test), context="test_dataset")

        # Logando hiperparâmetros
        mlflow.log_params(model.get_params())


if __name__ == "__main__":
    main()
