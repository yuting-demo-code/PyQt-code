"""
author: lixk
link: https://blog.csdn.net/u013314786/article/details/111059804
description: 本工具包用於執行子進程，實時獲取子進程執行過程中輸出的數據並打印到控制台，然後返回狀態碼和執行結果
"""
import subprocess
import sys


def run(cmd, shell=False):
    """
    開啟子進程，執行對應指令，控制台打印執行過程，然後返回子進程執行的狀態碼和執行返回的數據
    :param cmd: 子進程命令
    :param shell: 是否開啟shell
    :return: 子進程狀態碼和執行結果
    """
    print('\************** START **************')
    p = subprocess.Popen(cmd, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = []
    while p.poll() is None:
        line = p.stdout.readline().strip()
        if line:
            line = _decode_data(line)
            result.append(line)
            print(line)
        # 清空緩存
        sys.stdout.flush()
        sys.stderr.flush()
    # 判斷返回碼狀態
    if p.returncode == 0:
        print('\************** SUCCESS **************')
    else:
        print('************** FAILED **************')
    return p.returncode, '\r\n'.join(result)


def _decode_data(byte_data: bytes):
    """
    解碼數據
    :param byte_data: 待解碼數據
    :return: 解碼字符串
    """
    try:
        return byte_data.decode('utf-8')
    except UnicodeDecodeError:
        return byte_data.decode('GB18030')


if __name__ == '__main__':
    return_code, data = run('python process_function.py')
    # print('return code:', return_code, 'data:', data)