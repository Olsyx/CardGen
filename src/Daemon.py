import os 

class Daemon:
    watching = {}

    @staticmethod
    def watch_file(path):
        if not os.path.isabs(path):
            path = os.path.join(Daemon.output_folder, path)

        Daemon.watching[path] = os.stat(path).st_mtime

    @staticmethod
    def stop_watching(path):
        if not os.path.isabs(path):
            path = os.path.join(Daemon.output_folder, path)

        Daemon.watching.pop(path)
        
    @staticmethod
    def check():
        for path in Daemon.watching:
            stamp = os.stat(path).st_mtime

            if stamp != Daemon.watching[path]:
                Daemon.watching[path] = stamp
                return True
        
        return False