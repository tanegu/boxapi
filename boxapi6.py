from boxsdk import JWTAuth
from boxsdk import Client
import datetime
import sys

auth = JWTAuth.from_settings_file('/Users/tanegu/Desktop/197894819_4r2t9oka_config.json')
client = Client(auth)

#file_path = '/Users/tanegu/Desktop/boxapi/test2.rtf'
#file_name = 'test2'
#folder_id = '0'

file_id_01 = '460527349299'
file_info_01 = client.file(file_id_01).get()

print(file_info_01,end="")

file_id_02 = '460527606671'
file_info_02 = client.file(file_id_02).get()

print(file_info_02,end="")

file_id_03 = '460530323749'
file_info_03 = client.file(file_id_03).get()

print(file_info_03,end="")

file_id_04 = '460540008243'
file_info_04 = client.file(file_id_04).get()

print(file_info_04,end="")

file_id_05 = '460540113455'
file_info_05 = client.file(file_id_05).get()

print(file_info_05,end="")

file_id_06 = '460543608143'
file_info_06 = client.file(file_id_06).get()

print(file_info_06,end="")

file_id_07 = '460540106903'
file_info_07 = client.file(file_id_07).get()

print(file_info_07,end="")

file_id_08 = '460540050257'
file_info_08 = client.file(file_id_08).get()

print(file_info_08,end="")

file_id_09 = '460532181898'
file_info_09 = client.file(file_id_09).get()

print(file_info_09,end="")

file_id_10 = '460532497156'
file_info_10 = client.file(file_id_10).get()

print(file_info_10,end="")

file_id_11 = '460530438150'
file_info_11 = client.file(file_id_11).get()

print(file_info_11,end="")

file_id_12 = '460540895469'
file_info_12 = client.file(file_id_12).get()

print(file_info_12,end="")

file_id_13 = '460532207206'
file_info_13 = client.file(file_id_13).get()

print(file_info_13,end="")

file_id_14 = '460532406254'
file_info_14 = client.file(file_id_14).get()

print(file_info_14,end="")

file_id_15 = '460532685724'
file_info_15 = client.file(file_id_15).get()

print(file_info_15,end="")

file_id_16 = '460541020572'
file_info_16 = client.file(file_id_16).get()

print(file_info_16,end="")

file_id_17 = '460530755403'
file_info_17 = client.file(file_id_17).get()

print(file_info_17,end="")

file_id_18 = '460532997968'
file_info_18 = client.file(file_id_18).get()

print(file_info_18,end="")

file_id_19 = '460541050621'
file_info_19 = client.file(file_id_19).get()

print(file_info_19,end="")

file_id_20 = '460541809829'
file_info_20 = client.file(file_id_20).get()

print(file_info_20,end="")

file_id_21 = '460532528866'
file_info_21 = client.file(file_id_21).get()

print(file_info_21,end="")

file_id_22 = '460531309396'
file_info_22 = client.file(file_id_22).get()

print(file_info_22,end="")

file_id_23 = '460541373768'
file_info_23 = client.file(file_id_23).get()

print(file_info_23,end="")

file_id_24 = '460532805886'
file_info_24 = client.file(file_id_24).get()

print(file_info_24,end="")

file_id_25 = '460527897097'
file_info_25 = client.file(file_id_25).get()

print(file_info_25,end="")

file_id_26 = '460541711713'
file_info_26 = client.file(file_id_26).get()

print(file_info_26,end="")

file_id_27 = '460532900847'
file_info_27 = client.file(file_id_27).get()

print(file_info_27,end="")

file_id_28 = '460541721843'
file_info_28 = client.file(file_id_28).get()

print(file_info_28,end="")

file_id_29 = '460531422502'
file_info_29 = client.file(file_id_29).get()

print(file_info_29,end="")

file_id_30 = '460542269472'
file_info_30 = client.file(file_id_30).get()

print(file_info_30,end="")


#box_file = client.folder(folder_id).upload(file_path, file_name)