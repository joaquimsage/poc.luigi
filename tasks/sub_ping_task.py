"""
You can run this example like this:

    .. code:: console

            $ luigi --module examples.hello_world examples.HelloWorldTask --local-scheduler

If that does not work, see :ref:`CommandLine`.
"""
import luigi
from tasks import *


class SubPingTask(luigi.Task):
    task_namespace = 'tasks'

    def requires(self):
        return ping_task.PingTask()

    def run(self):
        print("{task} says: After Ping Re-Hello!".format(task=self.__class__.__name__))


if __name__ == '__main__':
    luigi.run()
