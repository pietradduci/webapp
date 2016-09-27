#!/usr/local/bin/python

import cgi
import cgitb; cgitb.enable()
import matplotlib
matplotlib.use( 'Agg' )
import numpy as np
from scipy.stats.kde import gaussian_kde
import os,sys
import pylab
from PIL import Image

def crop(arg1):
    # size is width/height
    img = Image.open(arg1)
    left = 88
    top = 41
    width = 545
    height = 321
    box = (left, top, left+width, top+height)
    #area = img.crop(box)

    #area.save('cropped_0_388_image1', 'jpeg')
    output_img = img.crop(box)
    output_img.save(filename+".png", 'png')


def make_fig():
    global name
    global filename
    filecsv = sys.argv[1]
    filename, file_extension = os.path.splitext(filecsv)
    # print sys.argv[1]
    x, y = np.genfromtxt(filecsv, delimiter=',', unpack=True)
    form = cgi.FieldStorage()

    #print(x[1], y[1])
    y = y[np.logical_not(np.isnan(y))]
    x = x[np.logical_not(np.isnan(x))]
    k = gaussian_kde(np.vstack([x, y]))
    xi, yi = np.mgrid[x.min():x.max():x.size**0.5*1j,y.min():y.max():y.size**0.5*1j]
    zi = k(np.vstack([xi.flatten(), yi.flatten()]))


    fig = pylab.figure(figsize=(7,4), frameon=False)
    #ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(111, frameon=False)

    #alpha=0.5 will make the plots semitransparent
    #ax1.pcolormesh(yi, xi, zi.reshape(xi.shape), alpha=0.5)
    ax2.contourf(yi, xi, zi.reshape(xi.shape), alpha=0.5)

    pylab.axis('off')
    #ax2.plot(y,x, "o")
    #ax1.set_xlim(0, 740)
    #ax1.set_ylim(515, 0)
    ax2.set_xlim(0, 740)
    ax2.set_ylim(515, 0)
    ax2.axison=False

    #overlay your soccer field
    im = pylab.imread('statszone_football_pitch.png')
    #ax1.imshow(im, extent=[0, 740, 0, 515], aspect='auto')
    ax2.imshow(im, extent=[0, 740, 0, 515], aspect='auto')

    #plt.show()
    #plt.savefig('heatmaps_tackles.png')
    #fig.savefig('test.png', bbox_inches='tight')
    name = filename+".png"
    fig.savefig( name, format='png' )
    # import shutil
    # shutil.copyfileobj(open("tempfile.png",'rb'), sys.stdout)
make_fig()
crop(name)
