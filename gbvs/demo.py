from saliency_models import gbvs, ittikochneibur
import cv2
import time
from matplotlib import pyplot as plt

if __name__ == '__main__':
    imname = "./images/bb.jpg"  # 替換成你自己的圖片路徑
    print("processing {}".format(imname))

    # 讀取圖片
    img = cv2.imread(imname)

    # 確保圖片正確讀取
    if img is None:
        print("Failed to load image!")
    else:
        # 計算顯著性圖
        saliency_map_gbvs = gbvs.compute_saliency(img)
        saliency_map_ikn = ittikochneibur.compute_saliency(img)

        # 將結果保存
        oname = "./outputs/my_image_out{}.jpg".format(time.time())
        cv2.imwrite(oname, saliency_map_gbvs)

        # 顯示圖片
        fig = plt.figure(figsize=(10, 3))

        # 原圖
        fig.add_subplot(1, 3, 1)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 注意轉換色彩空間
        plt.gca().set_title("Original Image")
        plt.axis('off')

        # GBVS 顯著性圖
        fig.add_subplot(1, 3, 2)
        plt.imshow(saliency_map_gbvs, cmap='gray')
        plt.gca().set_title("GBVS")
        plt.axis('off')

        # Itti-Koch-Neibur 顯著性圖
        fig.add_subplot(1, 3, 3)
        plt.imshow(saliency_map_ikn, cmap='gray')
        plt.gca().set_title("Itti Koch Neibur")
        plt.axis('off')

        plt.show()