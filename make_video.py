import cv2
import os
import time

start_time = time.time()

# 圖片資料夾與影片輸出路徑
image_folder = "/mnt/e/flowformer/viz_results/demo"  # 圖片的資料夾名稱
output_video = "output_video.mp4"  # 輸出影片名稱

# 設定影片的 FPS
fps = 60

# 取得資料夾內圖片列表並排序
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images.sort()  # 確保按照順序讀取圖片

# 讀取第一張圖片以獲取解析度
first_image_path = os.path.join(image_folder, images[0])
frame = cv2.imread(first_image_path)
height, width, layers = frame.shape

# 設定影片編碼器和參數
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # 使用 mp4v 編碼
video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

# 將圖片逐一寫入影片
for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)
    video.write(frame)

# 釋放資源
video.release()
print(f"影片已保存至 {output_video}")

end_time = time.time()
execution_time = end_time - start_time
print(f"執行時間：{execution_time:.2f} 秒")
