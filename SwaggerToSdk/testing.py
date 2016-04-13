import unittest
import os
import logging
logging.basicConfig(level=logging.INFO)

from SwaggerToSdk import *
from credentials import GH_TOKEN

class TestSwaggerToSDK(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        for key in list(os.environ.keys()):
            if key.startswith('TRAVIS'):
                del os.environ[key]

    def test_get_pr_from_travis_commit_sha(self):
        os.environ['TRAVIS_REPO_SLUG'] = 'Azure/azure-sdk-for-python'
        os.environ['TRAVIS_COMMIT'] = '497955507bc152c444bd1785f34cafefc7e4e8d9'
        pr_obj = get_pr_from_travis_commit_sha(GH_TOKEN)
        self.assertIsNotNone(pr_obj)
        self.assertEqual(pr_obj.number, 568)

        os.environ['TRAVIS_COMMIT'] = 'c290e668f17b45be6619f9133c0f15af19144280'
        pr_obj = get_pr_from_travis_commit_sha(GH_TOKEN)
        self.assertIsNone(pr_obj)

    def test_download_autorest(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            exe_path = download_install_autorest(temp_dir)
            self.assertTrue(exe_path.lower().endswith("autorest.exe"))

        with tempfile.TemporaryDirectory() as temp_dir:
            exe_path = download_install_autorest(temp_dir, "0.16.0-Nightly20160410")
            self.assertTrue(exe_path.lower().endswith("autorest.exe"))

        with tempfile.TemporaryDirectory() as temp_dir:
            with self.assertRaises(ValueError):
                exe_path = download_install_autorest(temp_dir, "0.16.0-FakePackage")


if __name__ == '__main__':
    unittest.main()