import web
import bot
from threading import Thread

def mainloop():
    Thread(target=web.app.run, kwargs={'host':'0.0.0.0', 'port':80}).start()
    bot.upd.start_polling()
    while True:
        try:
            input()
        except KeyboardInterrupt:
            bot.upd.stop()
            print('need to close web server')
            break

if __name__ == '__main__':
    mainloop()
