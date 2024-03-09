import unittest
from imgwizard.core import ImgWizard


class TestImgWizard(unittest.TestCase):
    def setUp(self):
        self.img_url = 'https://wsrv.nl/lichtenstein.jpg'
        self.img_wizard = ImgWizard(self.img_url)

    def test_resize(self):
        self.img_wizard.resize(width=300, height=200, fit='cover')
        expected_params = {'url': self.img_url, 'w': 300, 'h': 200, 'fit': 'cover'}
        self.assertEqual(self.img_wizard.params, expected_params)

    def test_crop(self):
        self.img_wizard.crop(alignment='top', focal_point={'fpx': 0.3, 'fpy': 0.6})
        expected_params = {'url': self.img_url, 'a': 'top', 'fpx': 0.3, 'fpy': 0.6}
        self.assertEqual(self.img_wizard.params, expected_params)

    def test_adjust_orientation(self):
        self.img_wizard.adjust_orientation(flip=True)
        expected_params = {'url': self.img_url, 'flip': ''}
        self.assertEqual(self.img_wizard.params, expected_params)

    def test_apply_adjustments(self):
        self.img_wizard.apply_adjustments(blur=5, contrast=10, filter_type='greyscale')
        expected_params = {'url': self.img_url, 'blur': 5, 'con': 10, 'filt': 'greyscale'}
        self.assertEqual(self.img_wizard.params, expected_params)

    def test_set_format(self):
        self.img_wizard.set_format(output_format='png', quality=90)
        expected_params = {'url': self.img_url, 'output': 'png', 'q': 90}
        self.assertEqual(self.img_wizard.params, expected_params)


if __name__ == '__main__':
    unittest.main()
