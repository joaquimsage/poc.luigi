import sys
import os.path
import luigi

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

#from tasks.ping_task import PingTask
import tasks


class Workflow:

    def run(self):
        luigi.build([tasks.ReSubPingTask()])


if __name__ == '__main__':
    Workflow().run()
    luigi.build([tasks.SendEmailTask()])
    luigi.build([tasks.SendEmailTask()])
    luigi.build([tasks.SendEmailTask()])
    luigi.build([tasks.TelnetTask()])
    luigi.build([tasks.TelnetTask()])
    luigi.build([tasks.TelnetTask()])





print("********************Succesful execution of Task pingTask.")