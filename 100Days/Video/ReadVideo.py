import imageio
import pylab
import skimage
import numpy as np


def plot_frame(frame):
    '''将帧绘制成图片显示'''

    pylab.figure()
    pylab.imshow(frame)
    pylab.show()


def read_video(filename):
    '''读取视频的每一帧'''

    # 可以选择解码工具
    vidobj = imageio.get_reader(filename, 'ffmpeg')

    for t, frame in enumerate(vidobj):
        frame = skimage.img_as_float(frame).astype(np.float64)
        # type(frame) is ndarray



if __name__ == '__main__':
    filename = '../Resources/hw1_sky_1.avi'
    read_video(filename)
