# Graph-Based-Image-Segmentation
Efficient Graph-Based Image Segmentation（中文参考：http://blog.csdn.net/mao_kun/article/details/50576036) 的实现源码（C++，看不懂),自己尝试用python实现，未遂。

# 环境：
windows10 + Visual Studio 2013 + python3.5
# 程序：
	segment.cpp---主函数，可以改图片的输入路径（其他.h的文件没看懂，步骤可以见上述博客或者论文，比较简单）
	jpg2ppm.py---由于上面的程序图片输入格式是ppm，所以写了一个转成ppm格式的python函数（不一定限于jpg输入）
	ppm2jpg.py---输出图片也是ppm格式，这个python函数可以转成jpg格式进行显示。
