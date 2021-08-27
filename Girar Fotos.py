# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:02:42 2021

@author: C0624150
"""

import os
from PIL import Image

diretorio = r'C:\Users\c0624150\OneDrive - Vale S.A\Pictures\IMAGO\GIRAR'
#lista = []
for root, dirs, files in os.walk(diretorio):
    for arquivo in files:
        
        img = Image.open(f'{root}\{arquivo}')
        
        
        b = 180
        
        img = img.rotate(angle=b,expand=True)
        
        img.save(f'{root}\{arquivo}')
        