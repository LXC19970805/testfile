import re

file_path = 'C:\\Users\\Lenovo\\Desktop\\Vision Prompt\\log.txt-2024-02-29-10-40-09'  # 替换成你的txt文件路径
val_acc = []
test_acc = []

with open(file_path, 'r') as file:
    lines = file.readlines()

index = 0
while index < len(lines):
    if "Evaluate on the *val* set" in lines[index]:
        # 如果找到目标行，提取第四行的数字部分
        
        val_line = lines[index + 4].strip()
        val_match = re.search(r'accuracy: (\d+\.\d+)%', val_line)
        if val_match:
            accuracy = float(val_match.group(1))
            val_acc.append(accuracy)
        test_line = lines[index + 11].strip()
        test_match = re.search(r'accuracy: (\d+\.\d+)%', test_line)
        if test_match:
            accuracy = float(test_match.group(1))
            test_acc.append(accuracy)
        # 继续检查下一个目标行
        index += 1
    else:
        # 如果不是目标行，继续检查下一行
        index += 1
print(f"val_acc的长度是{len(val_acc)}:", val_acc)
print(f"test_acc的长度是{len(test_acc)}:",test_acc)
