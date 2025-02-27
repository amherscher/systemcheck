import os
import shutil

def diskspacecheck(path):
    try:
        if not os.path.exists(path):
            return f"Error: Path '{path}' does not exist"
        diskUse = shutil.disk_usage(path)
        freeDisk = diskUse.free
        convertToGB = freeDisk / (1024 ** 3)
        return f"Free disk space in '{path}': {convertToGB:.2f} GB"
    except PermissionError:
        return f"Error: Permission denied to access '{path}'"
    except Exception as e:
        return f"Error: Unexpected issue with '{path}': {str(e)}"