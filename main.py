import app
import sys

if __name__ == "__main__":
    print(app.hello()[0])
    args = sys.argv[1:]
    if not isinstance(args, list):
        args = [args]
    if len(args) < 1:
        args = [input("Enter a State: ")]
    for stateabbr in args:
        result = app.bird(stateabbr)
    exit()
