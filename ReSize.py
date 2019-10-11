import os
import cv2
import tqdm
def transferAndRoi(img):
    '''
    img: 3D numpy array
    return 320*128 metrix
    '''
    ans = cv2.resize(img,(340,240),interpolation=cv2.INTER_CUBIC)
    ans = cv2.resize(ans,(320,240),interpolation=cv2.INTER_CUBIC)
    ans = ans[:,106:234,:]
    return ans
if __name__ == "__main__":
    fileList = sorted(os.listdir(r"C:\\Users\\Administrator\\Desktop\\ZP\\FgSegNet-master2\\SBI2015_train\\OQD\\"))
    for filename in tqdm.tqdm(fileList):
        if(filename[-1]=='y'):
            continue
        image = cv2.imread("C:\\Users\\Administrator\\Desktop\\ZP\\FgSegNet-master2\\SBI2015_train\\OQD\\"+filename)
        res = cv2.resize(image,(320,240),interpolation=cv2.INTER_CUBIC)
        res = res[:,106:234,:]
        # cv2.imshow("res",res)
        # print(res.shape)
        cv2.imwrite(r"C:\\Users\\Administrator\\Desktop\\ZP\\FgSegNet-master2\\SBI2015_train\\baoguoQD\\"+filename, res)
    fileList = sorted(os.listdir(r"C:\\Users\\Administrator\\Desktop\\ZP\\FgSegNet-master2\\SBI2015_dataset\\baoguoQD\\OG"))
    for filename in tqdm.tqdm(fileList):
        if(filename[-1]=='y'):
            continue
        image = cv2.imread("C:\\Users\\Administrator\\Desktop\\ZP\\FgSegNet-master2\\SBI2015_dataset\\baoguoQD\\OG\\"+filename)
        res = cv2.resize(image,(320,240),interpolation=cv2.INTER_CUBIC)
        res = res[:,106:234,:]
        # cv2.imshow("res",res)
        # print(res.shape)
        cv2.imwrite(r"C:\\Users\\Administrator\\Desktop\\ZP\\FgSegNet-master2\\SBI2015_dataset\\baoguoQD\\groundtruth\\"+filename, res)

    cv2.waitKey(0)
    fileList = sorted(os.listdir(r"C:\\Users\\Administrator\\Desktop\\ZP\\FgSegNet-master2\\SBI2015_dataset\\baoguoQD\\OI"))
    for filename in tqdm.tqdm(fileList):
        if(filename[-1]=='y'):
            continue
        image = cv2.imread("C:\\Users\\Administrator\\Desktop\\ZP\\FgSegNet-master2\\SBI2015_dataset\\baoguoQD\\OI\\"+filename)
        res = cv2.resize(image,(320,240),interpolation=cv2.INTER_CUBIC)
        res = res[:,106:234,:]
        # cv2.imshow("res",res)
        # print(res.shape)
        cv2.imwrite(r"C:\\Users\\Administrator\\Desktop\\ZP\\FgSegNet-master2\\SBI2015_dataset\\baoguoQD\\input\\"+filename, res)
        cv2.imwrite(r"C:\\Users\\Administrator\\Desktop\\ZP\\FgSegNet-master2\\sample_test_frames\\baoguoQD\\"+filename, res)
        

    cv2.waitKey(0)