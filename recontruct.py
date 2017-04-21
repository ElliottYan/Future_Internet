import dns.resolver
import multiprocessing
import pdb

def url_ip(urls):
	result = []
	for url in urls:
		try:
			a_record = dns.resolver.query(url,rdtype="A")
			aaaa_record = dns.resolver.query(url,rdtype = "AAAA")
			ip_4 = a_record.response.answer[0].items[0].to_text()
			# print(ip_4)
			ip_6 = aaaa_record.response.answer[0].items[0].to_text()
			# print(ip_6)
			result.append([url,ip_4,ip_6])
			# print(result)
		except:
			continue
	return result

def test():
	return "in process"

def write_in(result):
	with open("domain_ip.dat","w") as OUT:
		for rs in result:
			for row in rs:
				first = 1
				for s in row:
					if(first == 1):
						first = 0
					else:
						OUT.write(",")
					OUT.write(s)
				OUT.write("\n")

if __name__ == "__main__":
	url_list=[] 
	cpus = 3
	result=[]
	pool = multiprocessing.Pool(processes=cpus)
	with open("output.txt","r") as domain_file:
		for line in domain_file:
			url_list.append(line.strip())
	length = len(url_list)
	step = 100
	pdb.set_trace()
	arg_list = [url_list[x:x+step] for x in range(0,length,step)]
	pdb.set_trace()
	ret = [pool.apply_async(url_ip,(arg,)) for arg in arg_list]	
	# print(pool.apply_async(test))
	result = [rtitem.get() for rtitem in ret]
	# print(result)
	write_in(result)

