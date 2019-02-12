import sys
import os.path
import luigi

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

#from tasks.ping_task import PingTask
import tasks

if __name__ == '__main__':
    luigi.build([tasks.SendEmailTask()])
    luigi.build([tasks.SendEmailTask()])
    luigi.build([tasks.SendEmailTask()])
    luigi.build([tasks.TelnetTask()])
    luigi.build([tasks.TelnetTask()])
    luigi.build([tasks.TelnetTask()])
    luigi.build([tasks.PingTask()])
    luigi.build([tasks.PingTask()])
    luigi.build([tasks.PingTask()])
    luigi.build([tasks.SendEmailTask()])
    luigi.build([tasks.SendEmailTask()])
    luigi.build([tasks.SendEmailTask()])
    luigi.build([tasks.TelnetTask()])
    luigi.build([tasks.TelnetTask()])
    luigi.build([tasks.TelnetTask()])
    luigi.build([tasks.PingTask()])
    luigi.build([tasks.PingTask()])
    luigi.build([tasks.PingTask()])



print("********************Succesful execution of Task pingTask.")