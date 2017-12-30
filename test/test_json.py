#import json
import importlib.util
spec = importlib.util.spec_from_file_location("table", "../src/table.py")
table = importlib.util.module_from_spec(spec)
spec.loader.exec_module(table)

if __name__ == '__main__':
    my_table = table.Table(["id", "name"])
    my_table.add(("2", "yang"))

    my_table._print()
