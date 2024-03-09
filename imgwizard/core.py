import requests


class ImgWizard:
    def __init__(self, image_url):
        self.base_url = 'https://wsrv.nl/'
        self.params = {'url': image_url}

    def resize(self, width=None, height=None, fit='inside', dpr=None):
        if width:
            self.params['w'] = width
        if height:
            self.params['h'] = height
        self.params['fit'] = fit
        if dpr:
            self.params['dpr'] = dpr
        return self

    def crop(self, alignment='center', focal_point=None, smart_crop=None):
        if alignment:
            self.params['a'] = alignment
        if focal_point:
            self.params.update(focal_point)
        if smart_crop:
            self.params['a'] = smart_crop
        return self

    def adjust_orientation(self, flip=None, flop=None, rotate=None):
        if flip:
            self.params['flip'] = ''
        if flop:
            self.params['flop'] = ''
        if rotate is not None:
            self.params['ro'] = rotate
        return self

    def apply_adjustments(self, blur=None, contrast=None, filter_type=None, gamma=None, saturation=None, sharpness=None, tint=None):
        if blur is not None:
            self.params['blur'] = blur
        if contrast is not None:
            self.params['con'] = contrast
        if filter_type:
            self.params['filt'] = filter_type
        if gamma:
            self.params['gam'] = gamma
        if saturation is not None:
            self.params['sat'] = saturation
        if sharpness:
            self.params['sharp'] = sharpness
        if tint:
            self.params['tint'] = tint
        return self

    def set_format(self, output_format='jpg', quality=None, interlace=None):
        self.params['output'] = output_format
        if quality is not None:
            self.params['q'] = quality
        if interlace:
            self.params['il'] = ''
        return self

    def fetch(self):
        response = requests.get(self.base_url, params=self.params)
        if response.status_code == 200:
            return response.url
        else:
            raise Exception(f'Failed to process image, status code {response.status_code}')
