class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

def main():
    import sys, os, psutil, platform
    sys.__old_stderr__ = sys.stderr
    sys.__stderr__ = sys.stderr = sys.stdout = Unbuffered(sys.stdout)
    wd = os.path.dirname(os.path.abspath(sys.argv[0]))
    sys.path.insert(0,wd)
    os.chdir(wd)
    
    #special case import to allow reportlab to modify the envirnment in development
    try:
      import reportlab
    except ImportError:
      pass

    import leaktest, testRXPbasic, test_xmltestsuite

    leaktest.main(100)
    testRXPbasic.main()
    if platform.system()!='Darwin':
        test_xmltestsuite.main(verbose=int(os.environ.get('VERBOSE','0')))
    else:
        test_xmltestsuite.main(3)
    print(f'+++++ open Files={psutil.Process().open_files()!r}')

if __name__=='__main__':
    main()
