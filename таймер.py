import time
import sys
wait=0
z=0
hours = 0
minutes = 0
sec = 0
def x():
            print("вы выбрали таймер")
            print("введите кол-во часов")
            hours=int(input())
            print("введите кол-во минут")
            minutes=int(input())
            print("введите кол-во секунд")
            sec=int(input())
            # x=hours*60*60+minutes*60+sec
            wait = hours * 60 * 60 + minutes * 60 + sec
            print("вывод в формате часы минуты секунды")
            # wait=x
            while wait>0:
                v="осталось",hours,"часов,", minutes,"минут и", sec,"секунд"
                print('\b' * 10, end='')
                # print("осталось",hours,"часов,", minutes,"минут и", sec,"секунд", end='')
                print(hours, minutes, sec, end='')
                sys.stdout.flush()
                sec-=1
                minutes-=0
                hours-=0
                wait -= 1
                if sec==0:
                    if hours<=0:
                        if minutes<=0:
                            wait=0
                        elif minutes>0:
                            minutes-=1
                            sec=59
                    elif hours>0:
                        if minutes==0:
                            minutes=59
                            hours-=1
                            sec=59
                        elif minutes>0:
                            minutes-=1
                            sec=59
                elif sec>0:
                    sec=sec
                elif minutes==0:
                    if sec>0:
                        sec=sec
                    elif sec<=0:
                        if hours==0:
                            wait=0
                        elif hours>0:
                            sec=59
                            hours-=1
                            minutes=59
                            if minutes<=0:
                                minutes=0
                elif minutes>0:
                    minutes-=1
                    sec=59
                elif sec==60:
                    sec=0
                    minutes+=1
                elif minutes==60:
                    minutes=0
                    hours+=1
                elif hours<=0:
                    hours=0
                elif minutes<=0:
                    minutes=0
                time.sleep(1)
            print()
            print("время закончилось")
open(file='timer.py')
x()
