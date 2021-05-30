#csv 파일 읽기, 정보가 한글이어서 csv파일 저장시 'csv utf-8'로 저장
import csv
f = open('/Users/junsangwon/Desktop/profile_korean.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

# 원하는 열의 값만 가져오고 싶은 경우의 예시
# for line in rdr:
    # print(line[0])
    # print(line[1])
    # print(line[2])
# f.close()
