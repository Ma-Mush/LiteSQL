from setuptools import setup

long_description1 = '''
# LiteSQL 
База данных? Без проблем!

# ЧИТАТЬ НА GITHUB
https://github.com/Ma-Mush/LiteSQL

'''

setup(
name='LiteSQL', 
version='2.0.2',
description='Библиотека для легкого использования БД!', 
packages=['LiteSQL'], 
author_email='ma_mush@mail.ru', 
zip_safe=False,
python_requires='>=3.6',
long_description=long_description1,
long_description_content_type="text/markdown"
)