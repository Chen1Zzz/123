import tkinter
import http.client
import time


def get_webservertime(host):
    conn = http.client.HTTPConnection(host)
    conn.request("GET", "/")
    r = conn.getresponse()
    ts = r.getheader('date')  # 获取http头date部分
    # 将GMT时间转换成北京时间
    ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    ttime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)
    dat = "%u-%02u-%02u" % (ttime.tm_year, ttime.tm_mon, ttime.tm_mday)
    tm = "%02u:%02u:%02u" % (ttime.tm_hour, ttime.tm_min, ttime.tm_sec)
    return tm

def tick():
    global time1
    # 获取时间
    time2 = get_webservertime('www.taobao.com')
    # 如果时间发生变化，代码自动更新显示的系统时间
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
    clock.after(200, tick)


win = tkinter.Tk()
win.title("获取淘宝服务器时间")
time1 = ''
clock = tkinter.Label(win, font=('times', 100, 'bold'), bg='green')
clock.grid(row=0, column=0)
tick()
win.mainloop()

