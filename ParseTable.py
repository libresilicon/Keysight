#!/usr/bin/python3

class Parser:
	headerline=[]
	data={}
	filters={}

	def clean_up_values(self,line):
		line=line.replace(" mA/um","1e3")
		line=line.replace(" uA/um","1")
		line=line.replace(" nA/um","1e-3")
		line=line.replace(" pA/um","1e-6")
		line=line.replace(" fA/um","1e-9")

		line=line.replace(" mS/um","1e3")
		line=line.replace(" uS/um","1")
		line=line.replace(" nS/um","1e-3")
		line=line.replace(" pS/um","1e-6")
		line=line.replace(" fS/um","1e-9")

		line=line.replace(" mA","e-3")
		line=line.replace(" uA","e-6")
		line=line.replace(" nA","e-9")
		line=line.replace(" pA","e-12")
		line=line.replace(" fA","e-15")

		line=line.replace(" mV","e-3")
		line=line.replace(" V","e-0")

		line=line.replace(" uS","1e-6")

		return line

	def __init__(self,filename):
		print("Reading Keysight data file: "+filename)

		try:
			with open(filename,'r') as file:
				self.headerline=file.readline().split()
				for header in self.headerline:
					self.data[header]=[]

				for line in file:
					#line=line.split()
					line=self.clean_up_values(line).split()
					for idx in range(0,len(self.headerline)):
						label=self.headerline[idx]
						self.data[label].append(float(line[idx]))

		except(ValueError):
			print("Failed reading Keysight data file: "+filename)
		finally:
			file.close()

	def set_filter(self,name,value):
		self.filters[name]=value

	def get_column_names(self):
		return self.headerline

	def get_column(self,name):
		try:
			ret=self.data[name]
		except(ValueError):
			ret=[]
		return ret

	def get_filtered_column(self,name):
		ret=[]
		
		try:
			for idx in range(0,len(self.data[name])):
				for filter_name in filters:
					if self.data[filter_name][idx] == filters[filter_name]:
						ret.append(self.data[name][idx])
		except(ValueError):
			ret=[]

		return ret
