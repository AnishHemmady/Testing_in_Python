import pdb
import unittest
class insertn_sort(object):
	def __init__(self,inp):
		self.inp=inp
		
		
	def insertn_sort(self):
		for i in range(0,len(self.inp)):
			while(i>0 and self.inp[i-1]>self.inp[i]):
				self.inp[i-1],self.inp[i]=self.inp[i],self.inp[i-1]
				i-=1
				
		return(self.inp)
		
		
#quicksort
class Quickr(object):
		
	def partition(self,lst,start,end):
		pivt=lst[end]
		i=start-1
		for k in range(start,end):
			if lst[k]<pivt:
				i+=1
				lst[k],lst[i]=lst[i],lst[k]
		lst[i+1],lst[end]=lst[end],lst[i+1]
		return i+1
	
	def quick_srt(self,inp,st,end):
		if st<end:
			p=self.partition(inp,st,end)
			self.quick_srt(inp,st,p-1)
			self.quick_srt(inp,p+1,end)
			
		return inp
			
			

class Big_Bang_Tester(unittest.TestCase):
	def setUp(self):
		self.inpt_lst=[4,0,1,56,23,100,5000,22,12,10]
		self.insrtn=insertn_sort(self.inpt_lst)
		self.finl_ans=sorted(self.inpt_lst[:])
		self.qukr=Quickr()
		
	def test_quick(self):
		
		self.assertEqual(self.qukr.quick_srt(self.inpt_lst,0,len(self.inpt_lst)-1),self.finl_ans,"incorrect answer")
		
	def test_insertn(self):
		self.assertEqual(self.insrtn.insertn_sort(),self.finl_ans,"incorrect answer")
		
	def tearDown(self):
		self.inpt=None
		self.insrtn=None
		self.qukr=None
		
		
def suite():
	tests=['test_insertn','test_quick']
	return unittest.TestSuite(map(Big_Bang_Tester, tests))
		
		
if __name__ == "__main__":
    unittest.main()