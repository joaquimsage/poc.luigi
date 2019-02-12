"""
You can run this example like this:

    .. code:: console

            $ luigi --module examples.hello_world examples.HelloWorldTask --local-scheduler

If that does not work, see :ref:`CommandLine`.
"""
import luigi


class SendEmailTask(luigi.Task):
    task_namespace = 'tasks'

    def run(self):
        print("{task} says: About to send email!".format(task=self.__class__.__name__))


if __name__ == '__main__':
    luigi.run()
