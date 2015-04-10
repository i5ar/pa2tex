pa2tex
======

:paw_prints: Pattern To Texture image generator.

pa2tex, short for Pattern To Texture, allows you to generate a large image from a small tileable pattern.

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

Author says it works like a charm.

### Use
Place all patterns inside the main directory and run the `main.py` script. Insert the title, the author and the twitter account when asked.

- Default values:

	- Width: `1500`px;
	- Height: `500`px;
	- Title: `None`;
	- Author: `None`;
	- Account: `None`;

[Python3]: https://www.python.org/
[Pyllow]: https://pypi.python.org/pypi/Pillow/