import time

def traffic_light(sequence):
    while True:
        for step in sequence:
            if step == 1:
                print("N/S straight green, N/S left red, E/W straight red, E/W left red")
            elif step == 2:
                print("N/S straight orange, N/S left red, E/W straight red, E/W left red")
            elif step == 3:
                print("N/S straight red, N/S left red, E/W straight green, E/W left red")
            elif step == 4:
                print("N/S straight red, N/S left red, E/W straight orange, E/W left red")
            elif step == 5:
                print("N/S straight red, N/S left green, E/W straight red, E/W left red")
            elif step == 6:
                print("N/S straight red, N/S left orange, E/W straight red, E/W left red")
            elif step == 7:
                print("N/S straight red, N/S left red, E/W straight red, E/W left green")
            elif step == 8:
                print("N/S straight red, N/S left red, E/W straight red, E/W left orange")
            
            # กำหนดเวลา
            if step == 5 or 7:
                time.sleep(10)  # ไฟเขียวเลี้ยวซ้าย 10 วินาที
            elif step == 1 or 3:
                time.sleep(30)  # ไฟเขียวตรง 30 วินาที
            else:
                time.sleep(5)   # ไฟสีส้ม 5 วินาที

            if step != sequence[-1]:
                time.sleep(5)   # หน่วง 5 วินาที

# ลำดับ
sequence = [1, 2, 3, 4, 5, 6, 7, 8]

# infi loop
traffic_light(sequence)
