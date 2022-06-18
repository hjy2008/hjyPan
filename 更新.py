import glob
import os

from PIL import Image

if not os.path.isdir('.\\tmp'):
    os.mkdir('.\\tmp')

with open('README.md', 'w', encoding = 'utf-8') as f:
    f.write("# hjyPan\n\n[TOC]\n\n## 网盘列表\n\n")


def thumbnail_pic(jpgPath, tmpPath):
    # glob.glob(pathname)，返回所有匹配的文件路径列表
    a = glob.glob(r'*.jpg')
    for x in a:
        nameTmp = os.path.join(jpgPath, x.split('.')[-2] + '_tmp.' + x.split('.')[-1])
        # print(name)
        im = Image.open(os.path.join(jpgPath, x))
        im.thumbnail((100, 100))
        # print(im.format, im.size, im.mode)
        im.save(os.path.join(tmpPath, nameTmp), 'JPEG')

        # glob.glob(pathname)，返回所有匹配的文件路径列表
    a = glob.glob(r'*.png')
    for x in a:
        nameTmp = os.path.join(jpgPath, x.split('.')[-2] + '_tmp.' + x.split('.')[-1])
        # print(name)
        im = Image.open(os.path.join(jpgPath, x))
        im.thumbnail((100, 100))
        # print(im.format, im.size, im.mode)
        im.save(os.path.join(tmpPath, nameTmp), 'PNG')
    print('Done!')


path = '.\\tmp'
print('生成缩略图 ing...')
thumbnail_pic('.', path)

print('处理README.md ing...')
for k, v in zip(glob.glob('*.jpg'), glob.glob('.\\tmp\\*.jpg')):
    with open('README.md', 'a', encoding = 'utf-8') as f:
        f.writelines(f'#### <img src="{v}"/>[{k}](.\\{k})\n------\n\n')
for k, v in zip(glob.glob('*.png'), glob.glob('.\\tmp\\*.png')):
    with open('README.md', 'a', encoding = 'utf-8') as f:
        f.writelines(f'#### <img src="{v}"/>[{k}](.\\{k})\n------\n\n')


