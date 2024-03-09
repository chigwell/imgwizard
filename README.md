[![PyPI version](https://badge.fury.io/py/imgwizard.svg)](https://badge.fury.io/py/imgwizard)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/imgwizard)](https://pepy.tech/project/imgwizard)

# ImgWizard

`ImgWizard` is a Python package that simplifies image resizing and caching by interfacing with the `wsrv.nl` service. It supports a range of image formats and manipulations, making it an ideal tool for developers needing to dynamically adjust images in their applications.

## Installation

To install `ImgWizard`, you can use pip:

```bash
pip install imgwizard
```

## Usage

`ImgWizard` is designed to be intuitive and easy to use. Here's a quick start example:

```python
from imgwizard import ImgWizard

img = ImgWizard('https://i.ibb.co/tHzGgg9/Screenshot-2024-03-09-at-16-00-21.png')
resized_image_url = img.resize(width=300, height=300, fit='cover').fetch()
print(resized_image_url)
```

This example demonstrates how to resize an image to a 300x300 dimension using the `cover` fit option and then fetches the URL of the processed image.

### Cropping Images

You can easily crop images by specifying alignment or using a smart crop:

```python
cropped_image_url = img.crop(alignment='top').fetch()
print(cropped_image_url)
```

### Applying Adjustments

Apply various adjustments such as blur, contrast, and tint:

```python
adjusted_image_url = img.apply_adjustments(blur=5, contrast=15, tint='blue').fetch()
print(adjusted_image_url)
```

### Changing Image Format

Convert images to different formats with quality adjustments:

```python
formatted_image_url = img.set_format(output_format='png', quality=50).fetch()
print(formatted_image_url)
```

## Before and After Examples

**Original Image:**

![Original Image](https://i.ibb.co/tHzGgg9/Screenshot-2024-03-09-at-16-00-21.png)

**Resized Image:**

![Resized Image](https://wsrv.nl/?url=i.ibb.co/tHzGgg9/Screenshot-2024-03-09-at-16-00-21.png&w=300&h=300&fit=cover)

**Cropped Image:**

![Cropped Image](https://wsrv.nl/?url=i.ibb.co/tHzGgg9/Screenshot-2024-03-09-at-16-00-21.png&w=300&h=300&fit=cover&a=top)

**Adjusted Image:**

![Adjusted Image](https://wsrv.nl/?url=i.ibb.co/tHzGgg9/Screenshot-2024-03-09-at-16-00-21.png&w=300&blur=5&con=15&tint=blue)

**Reformatted Image:**

![Reformatted Image](https://wsrv.nl/?url=i.ibb.co/tHzGgg9/Screenshot-2024-03-09-at-16-00-21.png&w=300&output=png&q=50)

## Features

- Supports resizing, cropping, and various image adjustments such as blur, contrast, and tint.
- Easy integration with Python projects for dynamic image manipulation.
- Leverages the global caching and delivery capabilities of Cloudflare via `wsrv.nl`.

## Contributing

Your contributions are welcome! If you have suggestions or issues, please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/yourusername/imgwizard/issues).

## License

`ImgWizard` is available under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use it in your projects and contribute back to the open-source community.

