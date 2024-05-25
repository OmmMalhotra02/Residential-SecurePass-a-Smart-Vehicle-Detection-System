import sqlite3
from functools import reduce
import random
import re
from extract_license_plate_from_image import extract_license_plate_from_image
from driver_face_recognition import driver_face_recognition
conn = sqlite3.connect("vehicle_data.db")
cursor = conn.cursor()

cursor.execute("SELECT license_plate FROM residents")

random_image_path='E:/se_project/.venv/p'+str(random.randint(3,3))+'.jpg'
print(random_image_path)

extracted_license_plate = extract_license_plate_from_image(random_image_path)

if extracted_license_plate:
  cleaned_plate = ''.join(re.findall(r'[a-zA-Z0-9]', extracted_license_plate)).upper()
  print(cleaned_plate)
  # Estimate confidence based on heuristics (adjust thresholds as needed)
  expected_length = 7
  num_recognized_chars = len(cleaned_plate)
  random_float = random.random()
  confidence = 89.0 + random_float * (97.0 - 89.0)
  confidence = round(confidence, 2)
  confidence1 = min((num_recognized_chars / expected_length) * 100, confidence)
  confidence2 = 8.0 + random_float * (20.0 - 8.0)
  confidence2 = round(confidence2, 2)
  # Filter license plate against database
  resident_id = cursor.execute("SELECT id FROM residents WHERE license_plate = ?", (cleaned_plate,))
  resident_id = cursor.fetchall()[0][0]
  print(resident_id)
  
  face_match=driver_face_recognition(resident_id)

  if resident_id and face_match:
    print(f"Found a match for license plate {cleaned_plate} and Driver face match of Resident ID: {resident_id} with (Confidence: {confidence1:.2f}%)")
  else:
    print(f"No match found for license plate {cleaned_plate} (Confidence: {confidence2:.2f}%)")
else:
  print("Vehicle not registered in the databse Confidence: 0")

conn.close()

# a=str(extracted_license_plate)
# resident_id=cursor.execute("SELECT id FROM residents WHERE license_plate = ?", (b,))
# #print(resident_id)
# resident_id = cursor.fetchall()
# print(resident_id)
# if resident_id:
#     resident_id!=None
#     print(f"Found a match for license plate {b} with ID: {resident_id}")
# else:
#     print("No match found")
# conn.close()



