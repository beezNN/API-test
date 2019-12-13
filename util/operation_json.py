import json


class OperationJson:
    """操作json文件"""

    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = "D:/pycharm/API-test/dataconfig/data.json"
        else:
            self.file_path = file_path
        self.data = self.read_data()

    def read_data(self):
        """
        读取json文件
        :param file_name:文件路径
        :return:
        """
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data

    def get_data(self, id):
        """根据关键字获取对应数据"""
        return self.data[id]

    # 写入json
    def write_data(self, data):
        with open("D:/pycharm/API-test/dataconfig/token.json", 'w+b') as fp:
            fp.write(json.dumps(data).encode())


if __name__ == '__main__':
    # file_path = "D:/pycharm/API-test/dataconfig/data.json"
    opejson = OperationJson()
    print(opejson.read_data())
    print(opejson.get_data('id'))