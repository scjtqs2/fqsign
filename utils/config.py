#coding:utf-8
import json,logging,traceback
class Config:
    # 读取用户配置信息
    # 错误原因有两种：格式错误、未读取到错误
    @staticmethod
    def readJson():
        try:
            # 用户配置信息
            with open('./config.json', 'r') as fp:
                config = json.load(fp)
                return config
        except Exception as e:
            print(traceback.format_exc())
            logging.error('账号信息获取失败错误，原因为: ' + str(e))
            logging.error('1.请检查是否在Secrets添加了账号信息，以及添加的位置是否正确。')
            logging.error('2.填写之前，是否在网站验证过Json格式的正确性。')