'''メソッドの例'''
import math

class MyVector:
	'''ベクトルクラス'''
	
	def norm(self,x,y,z):
		'''ノルムの計算'''
		
		return math.sqrt(x**2 + y**2 + z**2) # 自乗和の平方根

if __name__ == '__main__':
	
	import methodexample as me
	
	vector = me.MyVector()
	
	print(vector.norm(1., 2., 3.))
		