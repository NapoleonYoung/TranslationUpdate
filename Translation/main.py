# scan folder
# by NapoleonYoung

import os
# print(os.path.join("c/","dd.txt"))#将文件名称添加到文件夹名称后面

# print(os.getcwd())#获取当前文件的路径
# os.mkdir(os.getcwd()+"/abc")#在指定目录下创建文件夹

# 指定的文件夹路径
remoteAppPath = "/Users/NapoleonYoung/Documents/iOS/Hisense/RemoteApp/RemoteApp/RemoteApp/"
dirList = os.listdir(remoteAppPath)  # 返回指定目录下所有的文件名称的列表

# 指定的翻译文件夹路径
translationPath = "/Users/NapoleonYoung/Documents/iOS/Hisense/RemoteApp素材资源/翻译/values-ios/"
translationFileList = os.listdir(translationPath)
print(len(translationFileList))
print(translationFileList)


# 获取RemoteApp文件夹下所有的后缀为.lproj的文件夹
allLprojFolder = []
for lprojFolder in dirList:
    if ".lproj" in lprojFolder:
        if "." in lprojFolder[0:3]:  # 只取标准的文件：国家缩写为两位zh-Hans-HK和zh-Hant-TW这种暂时不取
            allLprojFolder.append(lprojFolder)

allLprojFolder.sort()  # 排序
print(allLprojFolder)
print(len(allLprojFolder))

for lprojFolder in allLprojFolder:
    nameLprojFolder = lprojFolder[0:2]  # 获取对应语言的缩写
    print(nameLprojFolder)
    lprojFolderPath = os.path.join(remoteAppPath, lprojFolder)  # 特定语言的.lproj文件夹
    # print(lprojFolderPath)
    if os.path.isdir(lprojFolderPath):  # 如果当前路径是文件夹
        if len(os.listdir(lprojFolderPath)) > 0:    # 不是空文件夹
            nameStringsFile = os.listdir(lprojFolderPath)[0]    # 获取对应的待翻译的文件名
            for nameTranslationFile in translationFileList:
                if nameLprojFolder in nameTranslationFile:  # 翻译文件夹中找到对应语言的翻译文件
                    translationFilePath = os.path.join(translationPath, nameTranslationFile)  # 取得指定的翻译文件路径
                    if os.path.isfile(translationFilePath):  # 该路径是文件
                        translationFile = open(translationFilePath, 'r')  # 获取该文件
                        translationContent = translationFile.read()     #读取该文件内容
                        # print(translationContent)
                        translationFile.close() # 读取内容后，关闭文件

                        # 打开待翻译的文件
                        stringFilePath = os.path.join(lprojFolderPath, nameStringsFile)  # 获取待翻译的文件路径
                        if os.path.isfile(stringFilePath):
                            stringFile = open(stringFilePath, 'w')  # 获取该文件,并准备写入
                            stringFile.write(translationContent)    # 写入对应的内容
                            stringFile.close()  # 写入完毕后，关闭文件
                            break   # 跳出最近的for循环
