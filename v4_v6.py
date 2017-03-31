import urllib2
import dns.resolver
import pdb

def url_test():
	url_list = []
	with open("top-1m.csv") as cvsfile:
		for row in cvsfile:
			row = row[0:len(row)-1]
			row = row.split(",")
			# pdb.set_trace()
			url_list.append(row[1])

	count =	0
	for url in url_list:
		# pdb.set_trace()
		try:
			aaaa_record = dns.resolver.query(url,rdtype = "AAAA",raise_on_no_answer=False)
		except dns.resolver.NXDOMAIN:
			continue
		if(len(aaaa_record.response.answer)>=1):
			count+=1
		print count
	return count

if __name__=="__main__":
	print url_test()