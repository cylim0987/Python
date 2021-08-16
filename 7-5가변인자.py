# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") 
# #end 부분은......end 빈카능로 하면 하고 나서 계소
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") 
#end 부분은......end 빈카능로 하면 하고 나서 계소
    for lang in language:
        print(lang, end= " ")
    print()

profile("유재석", 20, "Python", "java", "c", "c00", "c#", "dmdkdkdk")
profile("김태호", 25, "kotilin", "swift", "", "", "")

profile("김태호", 25, "kotilin", "swift", "", "", "")
