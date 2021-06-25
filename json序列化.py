# import json

# dic = {'k':'v'}
# print(type(dic), dic)
# ret = json.dumps(dic)           # 序列化方法
# print(type(ret), ret)
# dic_d = json.loads(ret)         # 反序列化方法
# print(type(dic_d), dic_d)

# python中可以序列化的数据类型有：list, str, dict, num, tuple（当成列表来序列化的）,set不是json可序列化的


# import json

# dic = {'k': 'v'}
# f = open('fff', 'w', encoding='utf-8')
# json.dump(dic, f)           # 先序列化然后把序列化的结果写入文件中
# f.close()
# f = open('fff')
# res = json.load(f)              # 从文件中读出并进行反序列化转成字典
# f.close()
# print(res)








