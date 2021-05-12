import bstrap as bs
import pandas as pd
import time

def main():
	start = time.time()
	
	# initialize list of lists
	data = [['tom', 10], ['nick', 15], ['juli', 14], ['jill', 16], ['oscar', 13]]

	# Create the pandas DataFrame
	df = pd.DataFrame(data, columns = ['Name', 'Age'])

	print("Mean:", df['Age'].mean())
	print()
	
	m, s, lo, hi = bs.b_mean(df['Age'], 10000)
	#print("Boostrapped mean:", (sum(b_means) / len(b_means)) )
	print("---BOOTSTRAPPED VALUES---")
	print("Mean:", m, "\nSt Dev: ", s, "\nLow Conf Int:", lo, "\nHigh Conf Int:", hi)
	print()
	
	end = time.time()

	print("Seconds elapsed:", end-start)

main()
