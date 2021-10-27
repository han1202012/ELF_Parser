# coding=utf-8
# 解析 elf 文件需要导入的依赖库
#   安装 pyelftools 库
from elftools.elf.elffile import ELFFile


def main():
    # 要解析的动态库路径
    elf_path = r'libwtcrypto.so'
    # 打开 elf 文件
    file = open(elf_path, 'rb')
    # 创建 ELFFile 对象 , 该对象是核心对象
    elf_file = ELFFile(file)

    # 打印 elf 文件头
    print(elf_file.header)
    # 打印 程序头入口 个数
    print(elf_file.num_segments())
    # 打印 节区头入口 个数
    print(elf_file.num_sections())

    # 遍历打印 程序头入口
    for segment in elf_file.iter_segments():
        print(segment.header)
        print(segment.header['p_align'])

    # 遍历打印 节区头入口
    for section in elf_file.iter_sections():
        print('name:', section.name)
        print('header', section.header)

    # 关闭文件
    file.close()
    pass


if __name__ == '__main__':
    main()
