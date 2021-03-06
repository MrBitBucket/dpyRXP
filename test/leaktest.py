def test1(n):
	print('starting test1')
	import pyRXPU, sys
	xml='<start><tag1>text here</tag1><tag1>more text</tag1></start>'
	P = i = tup = None
	for i in range(n):
		P=pyRXPU.Parser()
		tup=P(xml)
		sys.stdout.write('.')
	del n, pyRXPU, sys, P, tup, xml
	print('\ntest1 done')

def test2(n):
	import os
	src = """<!DOCTYPE p SYSTEM "xhtml1-strict.dtd">
	<p>The York Early Music Christmas Festival has been going
strong since 1997 and in 2005 sees guest artists such as the Orlando
Consort, the Bach Players, Joglaresa, the Gonzaga Band and the
Huddersfield University Early Music Ensemble. Venues include the
Chapter House of York Minster and St Olave's Church, Marygate as
well as the National Centre for Early Music itself.</p>"""

	def find_dtd():
		try:
			import rlextra
		except ImportError:
			return os.path.join(os.path.dirname(__file__),'xhtml1')
		else:
			return os.path.join(rlextra.__path__[0],'dtd','xhtml1')

	def ident(x,dtdDir=find_dtd(),path_isfile=os.path.isfile,path_join=os.path.join):
		bn = x.split('/')[-1]
		dtd = path_join(dtdDir,bn)
		if path_isfile(dtd):
			return (x, open(dtd).read())
		return x

	def run2():
		import pyRXPU, sys
		p = pyRXPU.Parser(eoCB = ident)
		for i in range(n):
			tree = p.parse(src)
			sys.stdout.write('.')

	run2()
	print('\ntest2 done')

def main(N=None):
	import sys
	n = [x for x in sys.argv if x.startswith('--test=')]
	tests = n and [int(x.lstrip('--test=')) for x in n] or [1,2]
	map(sys.argv.remove,n)
	if N is None:
		if len(sys.argv)>1: N = int(sys.argv[1])
		else: N = 10000
	if 1 in tests:
		test1(N)
	if 2 in tests:
		test2(N)

if __name__=='__main__': #noruntests
	main()
