"""
You can run this example like this:

    .. code:: console

            $ luigi --module examples.hello_world examples.HelloWorldTask --local-scheduler

If that does not work, see :ref:`CommandLine`.
"""
import luigi
import socket


def try_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = False
    try:
        sock.bind(("localhost", port))
        print("Port NOT IN USE")
        result = False
    except:
        print("Port is IN USE")
        result = True

    sock.close()
    return result


class TelnetTask(luigi.Task):
    task_namespace = 'tasks'

    def run(self):
        port = 8082
        if try_port(port):
            print("{task} says: Port " + str(port) + " open and checked successfully")
        else:
            print("{task} says: Port " + str(port) + " closed and checked successfully")


if __name__ == '__main__':
    luigi.run()
