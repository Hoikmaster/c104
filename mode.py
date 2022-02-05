from collections import Counter
import csv

with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(n_num)



#Calculating Mode
data = Counter(new_data)
mode_data_for_range = {
                        "110-125": 0,
                        "125-140": 0,
                        "140-180": 0
                    }
for weight, occurence in data.items():
    if 50 < float(weight) < 60:
        mode_data_for_range["110-125"] += occurence
    elif 60 < float(weight) < 70:
        mode_data_for_range["125-140"] += occurence
    elif 70 < float(weight) < 80:
        mode_data_for_range["140-180"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")
