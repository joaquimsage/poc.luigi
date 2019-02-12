import sys
import os.path
import luigi

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

#from tasks.ping_task import PingTask
import tasks
import workflows

if __name__ == '__main__':
    workflow.run()



print("********************Succesful execution of Task pingTask.")