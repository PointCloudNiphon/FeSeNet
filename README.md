由于原来官方开源的代码使用的keras，以及tensorflow版本陈旧，在环境配置是问题很多，故重新写了一套win10下简易可行的配置方案
1.  conda create Newpython36 python==3.6.3
2.  activate Newpython36
3.  pip install -r package.txt
4.  修改文件：
   
             <Your PYTHON 3.6>\site-packages\skimage\transform\pyramids.py里面的pyramid_reduce函数：
   
            把out_shape = tuple([math.ceil(d / float(downscale)) for d in image.shape])
            
            修改为out_shape = tuple([math.floor(d / float(downscale)) for d in image.shape])
5.  下载我的代码，替换原来的代码（主要修改了因为版本不同导致的代码差异）
6.  数据集准备

    按照SBI2015_train、SBI2015_dataset里面的格式，分别在两个文件夹下加入baoguoQD
7.  数据预处理
    
    如果不对原始图片进行处理，很多**不是传送带的物体的引入会导致模型学到很多垃圾**
    将原始图片放在
    
    FgSegNet-master2\SBI2015_dataset\baoguoQD\OG
    
    FgSegNet-master2\SBI2015_dataset\baoguoQD\OI
    
    FgSegNet-master2\SBI2015_train\OQD
    
    下，并创建
    
    FgSegNet-master2\SBI2015_train\baoguoQD
    
    FgSegNet-master2\SBI2015_dataset\baoguoQD\groundtruth
    
    FgSegNet-master2\SBI2015_dataset\baoguoQD\input
    
    FgSegNet-master2\sample_test_frames\baoguoQD
    
    然后， run ReSize.py
    
    
 8.  run FgSegNet_M_S_SBI.py开始训练
 
 9.  开启jupyter查看，run test_prediction.ipynb
    
    
    
    
    
