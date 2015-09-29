
import lib2to3.main
from . import fixes

if __name__ == '__main__':
    raise SystemExit(lib2to3.main.main(fixes.__name__))
