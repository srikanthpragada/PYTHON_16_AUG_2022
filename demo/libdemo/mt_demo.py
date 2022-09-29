import threading

print(threading.main_thread())
print(threading.current_thread())


class PrintThread(threading.Thread):
    def run(self):
        for i in range(1, 26):
            print(f"Child -> {i}")


pt = PrintThread()
pt.start()
for i in range(1, 26):
    print(f"Main -> {i}")