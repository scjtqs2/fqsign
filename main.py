import logging
import glob
import os

module_dir = "demo"
module_suffix_extension = "*.py"


def main():
    current_dir = os.path.abspath(os.path.dirname(__file__))

    for pkg in glob.glob('%s/%s/*%s' % (current_dir, module_dir, module_suffix_extension)):
        base_name = os.path.basename(pkg).split('.')[0]  # 模块名
        pkg_name = module_dir + '.' + base_name  # 模块的路径
        if base_name == '__init__':
            continue
        module = __import__(pkg_name, fromlist=[base_name])  # 导入模块，fromlist只会导入list目录
        # print("module type:", type(module))
        model_class = getattr(module, base_name)  # 获取的是个类
        # print("model_class type:", type(model_class))
        instance = model_class()  # 获取实例对象
        print("instance type:", type(instance))
        try:
            instance.run()
        except Exception:
            logging.error("run error")
        print("-" * 30)

if __name__ == "__main__":
    main()
