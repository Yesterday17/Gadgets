# 作者：匿名用户
# 链接：https: // www.zhihu.com/question/22083486/answer/20449598
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

import sys


def ip_to_str(ip):
    _ip = [None] * 4
    _ip[0] = (ip & 0xff000000) >> 24
    _ip[1] = (ip & 0x00ff0000) >> 16
    _ip[2] = (ip & 0x0000ff00) >> 8
    _ip[3] = (ip & 0x000000ff)

    return '.'.join([str(i) for i in _ip])


def convert_to_seg(ip):
    list = ip.split('/')
    if len(list) == 1:
        return list[0]
    ip = list[0]
    mask_len = list[1]

    ip = sum([int(part_ip)*256**(3-i)
              for i, part_ip in enumerate(ip.split('.'))])

    mask_len = int(mask_len)

    low_mask = 0xffffffff << (32-mask_len)
    low_ip = ip_to_str((ip & low_mask)+1)

    high_mask = 0xffffffff >> mask_len
    high_ip = ip_to_str(ip | high_mask)

    return '-'.join((low_ip, high_ip))


if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename) as f:
        for line in f:
            line = line.strip()
            print(convert_to_seg(line))
