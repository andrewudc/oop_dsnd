import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):
	""" Binomial distribution class for calculating and 
	visualizing a Binomial distribution.
	
	Attributes:
		mean (float) representing the mean value of the distribution
		stdev (float) representing the standard deviation of the distribution
		data_list (list of floats) a list of floats to be extracted from the data file
		p (float) representing the probability of an event occurring
	
	
	TODO: All functions from plot_histogram_pdf and below
			
	"""
	
	
	def __init__(self, prob=.5, size=20):
				
		self.n = size
		self.p = prob
		
		Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
	
						
	
	def calculate_mean(self):
	
		"""Function to calculate the mean from p and n
		
		Args: 
			None
		
		Returns: 
			float: mean of the data set
	
		"""
		
		self.mean = self.p * self.n
				
		return self.mean



	def calculate_stdev(self):

		"""Function to calculate the standard deviation from p and n.
		
		Args: 
			None
		
		Returns: 
			float: standard deviation of the data set
	
		"""
		
		self.stdev = self.n * self.p * (1 - self.p)
		
		return self.stdev
		
		
	def replace_stats_with_data(self):
	
		"""Function to calculate p and n from the data set
		
		Args: 
			None
		
		Returns: 
			float: the p value
			float: the n value
	
		"""
	
		self.n = len(self.data)
		self.p = 1.0 * sum(self.data) / len(self.data)
		self.mean = self.calculate_mean()
		self.stdev = self.calculate_stdev()		

	
		
	def plot_bar(self):
		"""Function to output a histogram of the instance variable data using 
		matplotlib pyplot library.
		
		Args:
			None
			
		Returns:
			None
		"""
				
		plt.bar(x = ['0', '1'], height = [(1 - self.p) * self.n, self.p * self.n])
		plt.title('Bar Chart of Data')
		plt.xlabel('outcome')
		plt.ylabel('count')
		
		
		
	def pdf(self, k):
		"""Probability density function calculator for the gaussian distribution.
		
		Args:
			x (float): point for calculating the probability density function
			
		
		Returns:
			float: probability density function output
		"""
		
		a = math.factorial(self.n) / (math.factorial(k) * (math.factorial(self.n - k)))
		b = (self.p ** k) * (1 - self.p) ** (self.n - k)
		
		return a * b
		

	def plot_histogram_pdf(self):

		"""Function to plot the pdf of the binomial distribution
		
		Args:
			None
		
		Returns:
			list: x values for the pdf plot
			list: y values for the pdf plot
			
		"""
		
		x = []
		y = []
		
		# calculate the x values to visualize
		for i in range(self.n):
			tmp = min_range + interval*i
			x.append(tmp)
			y.append(self.pdf(tmp))

		# make the plots
		fig, axes = plt.subplots(2,sharex=True)
		fig.subplots_adjust(hspace=.5)
		axes[0].hist(self.data, density=True)
		axes[0].set_title('Normed Histogram of Data')
		axes[0].set_ylabel('Density')

		axes[1].plot(x, y)
		axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
		axes[0].set_ylabel('Density')
		plt.show()

		return x, y
		
	def __add__(self, other):
		
		"""Function to add together two Gaussian distributions
		
		Args:
			other (Gaussian): Gaussian instance
			
		Returns:
			Gaussian: Gaussian distribution
			
		"""
		
		result = Gaussian()
		result.mean = self.mean + other.mean
		result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)
		
		return result
		
		
	def __repr__(self):
	
		"""Function to output the characteristics of the Gaussian instance
		
		Args:
			None
		
		Returns:
			string: characteristics of the Gaussian
		
		"""
		
		return "mean {}, standard deviation {}".format(self.mean, self.stdev)