import queue
import diskspacecheck

task_queue = queue.Queue()
task_queue.put(diskspacecheck("/home/amherscher/Desktop/shared"))
while not task_queue.empty():
    task = task_queue.get()
    print(task())