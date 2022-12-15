import os
import unittest

from src.anaconda.enterprise.mlops.sdk.ae5.secrets import load_ae5_user_secrets
from src.anaconda.enterprise.mlops.sdk.common.config.environment import demand_env_var


class TestSecrets(unittest.TestCase):
    def setUp(self) -> None:
        if "MOCK_SECRET" in os.environ:
            del os.environ["MOCK_SECRET"]

    def test_load_ae5_user_secrets(self):
        mock_path: str = "test/fixtures/secrets"
        load_ae5_user_secrets(secrets_path=mock_path)
        self.assertEqual(demand_env_var(name="MOCK_SECRET"), "This is a mock secret.")

    def test_load_ae5_user_secrets_with_silent_true(self):
        mock_path: str = "test/fixtures/secrets"
        load_ae5_user_secrets(secrets_path=mock_path, silent=True)
        self.assertEqual(demand_env_var(name="MOCK_SECRET"), "This is a mock secret.")


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(TestSecrets())
