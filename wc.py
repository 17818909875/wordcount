import sys,re
#新建一个类用来处理命令行输入的字符
class wc:
	def __init__(self):
		try:
			self.task=sys.argv[1][1:]
			self.file=open(sys.argv[2],'r',encoding='UTF-8')
		except:
			print('输入参数有误，程序退出')
			exit()
		if self.task=='c':#如果返回字符数
			self.c()
		elif self.task=='w':#如果返回词的数目:
			self.w()
		elif self.task=='l':#如果返回行数
			self.l()
		else:
			print('输入参数有误，程序退出')
			exit()
	def l(self):
		print('文件共'+str(len(self.file.readlines()))+'行')
		exit()
	def c(self):
		print('文件共'+str(len(self.file.read().replace('\n', '')))+'个字符')
		exit()
	def w(self):
		print('文件共'+str(len(re.split(r'[^a-zA-Z]+',self.file.read())))+'个词')
		exit()
if __name__ == '__main__':
	wc()
