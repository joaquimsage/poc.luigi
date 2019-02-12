"""
You can run this example like this:

    .. code:: console

            $ luigi --module examples.hello_world examples.HelloWorldTask --local-scheduler

If that does not work, see :ref:`CommandLine`.
"""
import luigi
from tasks import *


class ReSubPingTask(luigi.Task):
    task_namespace = 'tasks'

    def requires(self):
        return sub_ping_task.SubPingTask()

    def run(self):
        print("{task} says: After Ping Re-Hello!".format(task=self.__class__.__name__))


if __name__ == '__main__':
    luigi.run()
