# @Time    : 2018/11/23 17:29
# @Author  : Ghoul
# @FileName: main.py
# @Software: PyCharm
# @Project： wxbot
from datetime import datetime
from wxpy import *
import _thread
from apscheduler.schedulers.blocking import BlockingScheduler

def send_timing_information(wx_group):
    wx_group.send('不要忘记今天的周报呦~ 现在的时间是 北京时间 {}'.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

def sched_fun(wx_group):
    print("start thread")
    sched = BlockingScheduler()
    sched.add_job(send_timing_information,'cron',hour  =8,minute = 30,args=(wx_group,))
    sched.start()


if __name__ == '__main__':
    bot = Bot(cache_path=True,console_qr = True)
    bot.enable_puid('wxpy.pkl')
    wx_group = ensure_one(bot.groups().search('魔法师俱乐部'))

    wx_group.send('小助手启动了，试试@我看我会说什么吧，每天早上八点三十分还会有神秘惊喜呦~')
    @bot.register(wx_group,TEXT)
    def auto_reply(msg):
        if  not msg.is_at:
            return
        else:
            return '小助手收到您的消息了呢：{} ({}),现在小助手会的还很少，正在抓紧开发中。'.format(msg.text,msg.type)



    try:
        _thread.start_new_thread(sched_fun,(wx_group,))
    except:
        print("error : dont start the thread")
    # sched_fun(wx_group)


    embed()






