# -*- coding: utf-8 -*-
# @Time : 2021/3/5 0005
# @Author : yang
# @Email : 2635681517@qq.com
# @File : test_f.py
import threading

from django.db.models import F

from weibo.models import WeiboUser


class ChangeThread(threading.Thread):
    """改变用户的状态"""

    def __init__(self, max_count=100, *args, **kwargs):
        super(ChangeThread, self).__init__(*args, **kwargs)
        self.max_count = max_count

    def run(self) -> None:
        count = 0
        user = WeiboUser.objects.get(pk=40628)
        while True:
            """最多循环max_count次"""
            if count >= self.max_count:
                break
            print(self.getName(), count)
            # user.status += 1
            #
            user.status = F('status') + 1
            user.save()
            count += 1


def main():
    t1 = ChangeThread(max_count=800)
    t2 = ChangeThread(max_count=500)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()
