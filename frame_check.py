import cv2
import time

# 讀取影片
video_path = "/mnt/e/flowformer/visualize/b.mp4"  # 替換成你的影片路徑
cap = cv2.VideoCapture(video_path)

# 獲取幀數
if not cap.isOpened():
    print("無法打開影片。請檢查影片路徑或影片格式是否正確。")
else:
    # 獲取 FPS
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"影片的 FPS：{fps}")
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"影片總幀數：{frame_count}")
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"影片解析度：{width} x {height}")

# 關閉影片
cap.release()
