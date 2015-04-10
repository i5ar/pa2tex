pa2tex
======

:paw_prints: Pattern To Texture image generator.

Pattern To Texture allows you to generate a large image from a small tileable pattern.

[![Pattern To Texture](https://i.ytimg.com/vi_webp/6ePwLBWAfi0/hqdefault.webp)](https://www.youtube.com/watch?v=6ePwLBWAfi0)

> This script was made for fun in my spare time to spare time.

### Installation and required packages
- Install <a href="https://www.python.org/" target="_blank">Python3</a> if not already in your operating system;
    - Install the PyPA recommended tool <a href="https://pip.pypa.io/" target="_blank">pip</a> for installing Python packages;
		- Install <a href="https://pypi.python.org/pypi/Pillow/" target="_blank">Pillow</a>;

                pip install Pillow

If you intend to insert text over the image you must create a subdirectory called `fonts/` with the fonts of your choice named `head.woff` for the title text and `auth.woff` surprisingly enough for the author text.

### Compatibility
- Python v3.4

- Pillow v2.8.1

### Use
Place all patterns inside the main directory and run the `main.py` script. You can also insert the title, the author and the account when asked or skip by pressing `Enter`.

- Default values:

	- Width: `1500`px;
	- Height: `500`px;
	- Title: `None`;
	- Author: `None`;
	- Account: `None`;

[Python3]: https://www.python.org/
[Pyllow]: https://pypi.python.org/pypi/Pillow/
