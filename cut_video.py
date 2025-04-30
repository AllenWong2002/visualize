import cv2
import os
import time

start_time = time.time()

# 影片路徑與輸出資料夾
video_path = "/mnt/e/flowformer/visualize/b.mp4"
output_folder = "demo"

# 如果輸出資料夾不存在，則創建
os.makedirs(output_folder, exist_ok=True)

# 開啟影片
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("無法打開影片。請檢查影片路徑或格式。")
else:
    frame_id = 1

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 保存每一幀
        img_path = os.path.join(output_folder, f"{frame_id:06d}.png")
        cv2.imwrite(img_path, frame)
        frame_id += 1

    print(f"已完成處理，共保存 {frame_id - 1} 幀圖片。")

cap.release()

end_time = time.time()
execution_time = end_time - start_time
print(f"執行時間：{execution_time:.2f} 秒")