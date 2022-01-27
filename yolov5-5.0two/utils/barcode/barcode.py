import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar


def decodeDisplay(video):
    # 转为灰度图像

    gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray)
    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        barData = str(barcodeData)

        # 在图像上面显示识别出来的内容
        # 打印识别后的内容
        print("[扫描结果] 二维码类别： {0} 内容： {1}".format(barcodeType, barcodeData))
        with open('barcode.txt', 'w', encoding='utf-8') as f:
            f.write(barData)
            f.close()
