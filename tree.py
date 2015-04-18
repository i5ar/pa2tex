#!/usr/bin/env python

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

pa2tex_info = {
    "name": "tree",
    "author": "iSar",
    "version": (0, 0, 0),
    "python": (3, 4),
    "pillow": (2, 8, 1),
    "description": "Pattern to Texture image generator" }

import glob, os
from PIL import Image, ImageFont, ImageDraw

# Make directories if they do not exist
if not os.path.exists('_build'):
    os.makedirs('_build')

# Input width, height
while True:
    try:
        isar_width = int(input("Please, enter the width [1200]: ") or 1200)
        break
    except ValueError:
        print("That wasn't a valid number. Please, try again: ")

while True:
    try:
        isar_height = int(input("Please, enter the height [600]: ") or 600)
        break
    except ValueError:
        print("That wasn't a valid number. Please, try again: ")


box = (isar_width, isar_height)

# List files
patterns_glob = glob.glob("patterns\\*")

# Get image from 'patterns' directory
for infile in patterns_glob:
    file, ext = os.path.splitext(infile)
    # Allow only \\*.png or \\*.jpg exension
    if ext != '.png' and ext != '.jpg':
        break

    # Print the name of the pattern file
    print("File name: " + file[9:] + ext)
    # Get size
    im = Image.open(infile)
    width, height = im.size

    new_im = Image.new('RGB', box,'black')
    # Get rows and cols
    width_rapp = box[0]//width+1
    height_rapp = box[1]//height+1

    i = 0
    i_h = 0
    for _ in range(height_rapp):
        new_im.paste(im, ( (box[0]//2) - width//2, i_h))
        i_h = i_h + height
        i += 1
        i_w = 0
        for _ in range(i):
            i_w = i_w + width
            new_im.paste(im, ((box[0]//2) - width//2 + i_w, i_h ))
            new_im.paste(im, ((box[0]//2) - width//2 - i_w, i_h ))

    # Insert the new image into "_build" directory
    filename = "_build\\" + file[9:] + "-header" + ext
    # Input title, author, account
    title_name = input("Please, enter the title of \"" + file[9:] + ext + "\": ")
    author_name = input("Please, enter the author of \"" + file[9:] + ext + "\": ")
    account_name = input("Please, enter " + author_name.upper() + " Twitter account: ")

    # Get fonts
    if not os.path.isfile("fonts/head.woff"):
        print("Please, use a font of your choice next time!")
        title_font = ImageFont.load_default()
    else:
        title_font = ImageFont.truetype( "fonts/head.woff", 30 )
    if not os.path.isfile("fonts/auth.woff"):
        auth_font = ImageFont.load_default()
    else:
        auth_font = ImageFont.truetype("fonts/auth.woff", 15)

    # Draw texture image
    draw = ImageDraw.Draw(new_im)

    # Draw title
    draw.text((20, 66), title_name.upper(), (255, 255, 255), font=title_font)

    # Get "BY " size
    auth_text_by = "BY "
    get_by_size = auth_font.getsize(auth_text_by)

    # Author
    if author_name != '':
        # Draw "BY "
        draw.text((20, 106), auth_text_by, (255, 255, 255), font=auth_font)
        # Draw author name
        draw.text((20 + get_by_size[0], 106), author_name.upper(), (227, 112, 112), font=auth_font)

    # Account
    if author_name != '' and account_name != '':
        # Draw hyphen " - "
        auth_text_hyphen = " - "
        get_text_size_name = auth_font.getsize(author_name.upper())
        draw.text((20 + get_by_size[0] + get_text_size_name[0], 106), auth_text_hyphen, (255, 255, 255), font=auth_font)
        # Draw author @account
        get_hyphen_size = auth_font.getsize(auth_text_hyphen)
        draw.text((20 + get_by_size[0] + get_text_size_name[0] + get_hyphen_size[0], 106), "@" + account_name.upper(), (227, 112, 112), font=auth_font)
    elif account_name != '':
        draw.text((20, 106), "@" + account_name.upper(), (227, 112, 112), font=auth_font)

    new_im.save(filename)

    # Open the file
    os.startfile(filename)
