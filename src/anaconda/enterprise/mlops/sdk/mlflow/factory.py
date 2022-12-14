from mlflow import MlflowClient

from ..common.config.environment import demand_env_var


def build_mlflow_client() -> MlflowClient:
    return MlflowClient(
        tracking_uri=demand_env_var(name="MLFLOW_TRACKING_URI"), registry_uri=demand_env_var(name="MLFLOW_REGISTRY_URI")
    )