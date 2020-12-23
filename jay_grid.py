#!/usr/bin/env python3
#
# Draws a grid on the image. Expects image in std input, writes image to stdout.
#
# Original image at https://www.santacruzmuseum.org/wp-content/uploads/2020/03/California_Scrub-Jay_26994352448-1024x683.jpg

from PIL import Image, ImageDraw

import sys
import urllib.request

def _CropImage(img):
  width, height = img.size
  edge = 630
  top_left = (280, 0)
  
  return img.crop(top_left + (top_left[0] + edge, top_left[1] + edge))

def _DrawGrid(img):
  draw = ImageDraw.Draw(img)

  width, height = img.size

  horizontal_line_count = 10
  vertical_line_count = 10
  
  for i in range(0, vertical_line_count + 1):
    x = int((i / vertical_line_count) * width)
    draw.line((x, 0, x, height), fill=128)

  for i in range(0, horizontal_line_count + 1):
    y = int((i / horizontal_line_count) * height)
    draw.line((0, y, width, y), fill=128)    

def main():
  with Image.open(sys.stdin.buffer) as img:
    img = _CropImage(img)
    _DrawGrid(img)
    img.save(sys.stdout.buffer, "JPEG")
      
if __name__ == '__main__':
  main()
