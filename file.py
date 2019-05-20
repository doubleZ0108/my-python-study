# region tagfinder
            dict = {}

            dict.clear()
            # region 将result文件夹中的图片名字保存到result_list中
            resultPath = 'static/result'
            result_list = os.listdir(resultPath)
            for i in range(0, len(result_list)):
                result_list[i] = result_list[i][2:]  # 去除搜索结果图片名中的im

                (filename, extension) = os.path.splitext(result_list[i])  # 划分文件名和后缀名
                result_list[i] = filename
            print(result_list)
            # endregion

            tagPath = 'database/tags'
            tag_list = os.listdir(tagPath)

            for tagnow in tag_list:
                if result_list.__len__() == 0:  # 8张图片都已找到tag
                    break
                # print(tagnow)
                with open("database/tags/" + tagnow, "r") as fp:
                    str_list = fp.readlines()  # 读取文件的全部信息存储到str_list中

                    for i in range(0, len(str_list)):
                        str_list[i] = str_list[i].rstrip()  # 去除行尾的\n

                    for result in result_list[::-1]:  # 倒序遍历避免删除错误
                        if str_list.count(result):  # 如果打开的此文件中有此图片标号
                            dict.setdefault(result, tagnow)  # 将图片[名-tag]加入字典中
                            result_list.remove(result)

            # region 去除字典中的后缀
            for key in dict.keys():
                (filename, extension) = os.path.splitext(dict[key])
                dict[key] = filename
            # endregion

            print(dict)
            # endregion
