import sys
import RequestProcess as RequestProcess

if __name__ == "__main__":
    rp = RequestProcess.RequestProcess(sys.argv[1])
    rp.run()
