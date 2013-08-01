import whois
import threading
lower_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

all = []
all = lower_a + num
alldomains = []
availabledomains = []
count = 0
countavailable = 0
threads = []

def split_list(a_list):
    half = len(a_list)/2
    return a_list[:half], a_list[half:]

def print_domain_if_is_available(domain):
    global countavailable
    global availabledomains
    domain += ".com"
    content = ""
    """ ignore any stort of exception"""
    try:
        content = whois.hamidlookup(domain)
    except Exception:
        pass
    """print content"""
    if "No match" in content:
        print domain
        countavailable +=1
        availabledomains.append(domain)

def recursive_product(myList, length, myString = ""):
    global count
    global alldomains
    if length == 0:
        alldomains.append(myString)
        count += 1
        return
    for c in myList:
        recursive_product(myList, length-1, myString + c)

def iterate_through_domain_list_and_look_for_available_ones(domainlist):
    """ iterate through the list and look for availble domains """
    for d in alldomains:
        print_domain_if_is_available(d)
    return

def create_tread(listofdomains):
    global threads
    thread = threading.Thread(target=iterate_through_domain_list_and_look_for_available_ones, args=[listofdomains])
    thread.start()
    threads.append(thread)
    return

""" first create a list containing all domains """
for r in range(3, 4):
    recursive_product(all, r)

print "Domain List is generated"
"""spit domains list into four lists """
# a, b = split_list(alldomains)
# c, d = split_list(a)
# e, f = split_list(b)

# create_tread(c)
# create_tread(d)
# create_tread(e)
# create_tread(f)

# # to wait until all three functions are finished

# print "Waiting..."

# for thread in threads:
    # thread.join()
iterate_through_domain_list_and_look_for_available_ones(alldomains)
# print 'All domains: [%s]' % ', '.join(map(str, alldomains))
print 'All available domains: [%s]' % ', '.join(map(str, availabledomains))
print 'total domain searched: %d' % (count)
print 'total available domains: %d' % (count)