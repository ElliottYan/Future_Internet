import urllib2
import dns.resolver
import pp
import pdb

def url_test():
	url_list = []
	total = 1000
	ppservers = ()
	ncpus = 2
	step = 100
	job_server = pp.Server(ncpus, ppservers=ppservers)
	with open("top-1m.csv") as cvsfile:
		for row in cvsfile:
			row = row[0:len(row)-1]
			row = row.split(",")
			# pdb.set_trace()
			url_list.append(row[1])
	# cnt = test_for_v6(url_list,1,1000)
	partition = range(0,total,step)
	inputs = [(url_list,partition[i],partition[i]+step) for i in range(10)]
	jobs = [(input, job_server.submit(test_for_v6,input, (), ("dns.resolver",))) for input in inputs]
	# pdb.set_trace()
	result = []
	for input, job in jobs:
		result.append(job())

	with open("output.txt","w") as output_file:
		for rt in result:
			for url in rt:
				output_file.write(url+"\n")
	pdb.set_trace()
	return result


def test_for_v6(url_list,start,end):
	r_list = []
	# count =	0
	# with open("v6_support.txt","w") as ouput_file:
 	for index in range(start,end):
		# pdb.set_trace()
		url = url_list[index]
		try:
			aaaa_record = dns.resolver.query(url,rdtype = "AAAA")
		except:
			continue
		# count+=1
		print url
		r_list.append(url)
			# ouput_file.write(url+"\n")
	return r_list

if __name__=="__main__":
	rs = url_test()