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
    wx_group.send('这是一个定时任务 现在的时间是 {}'.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

def sched_fun(wx_group):
    print("start thread")
    sched = BlockingScheduler()
    sched.add_job(send_timing_information,'interval',minutes =1,args=(wx_group,))
    sched.start()


if __name__ == '__main__':
    bot = Bot(cache_path=True)
    bot.enable_puid('wxpy.pkl')
    wx_group = ensure_one(bot.groups().search(''))



    @bot.register(wx_group,TEXT)
    def auto_reply(msg):
        if  not msg.is_at:
            return
        else:
            return '收到消息：{} ({})'.format(msg.text,msg.type)



    try:
        _thread.start_new_thread(sched_fun,(wx_group,))
    except:
        print("error : dont start the thread")
    # sched_fun(wx_group)


    embed()






