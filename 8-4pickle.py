# pickle 프로그램 상에서 우리가 사용하고 있는 데이터를 파일 형태로 저장하는 것


import pickle
# profile_file = open("profile.pickle", "wb")
# #따로 인코딩 설정 필요 없음
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close()

profile_file = open("profile.pickle", "rb") # r은 읽기
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close() 

# 가지고 있는 데이터를 pickle로 파일에 저장하고 파일을 로드를 통해 불러오고..

