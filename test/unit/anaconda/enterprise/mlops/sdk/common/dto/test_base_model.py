import unittest

from src.anaconda.enterprise.mlops.sdk.common.dto.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_base_model(self):
        class TestModel(BaseModel):
            test_attribute: str

        test_dict: dict = {"testAttribute": "testValue"}

        test_model = TestModel.parse_obj(test_dict)
        self.assertEqual(test_model.test_attribute, "testValue")
        self.assertEqual(test_dict, test_model.dict(by_alias=True))


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(TestBaseModel())
