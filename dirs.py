#!/usr/bin/env python

import os

dirs = [
("mac_changer","Changes MAC address to CLI flag or user input"),
("network_scanner","Discovers IP and MAC address of all connected clients."),
("arp_spoofer","Redirects and intercepts the flow of packets in the network."),
("packet_sniffer","Filters intercepted data for usernames, passwords, visited links, etc"),
("dns_spoofer","Redirects DNS requests from one domain to another."),
("file_interceptor","Intercepts and replaces files."),
("code_injector","Intercepts HTML pages for code injection"),
("arpspoof_detector","Detects ARP spoofing attacks."),
("execute_command_payload","Executes a system command on remote host."),
("execute_and_report_payload","Executes a system command and emails report."),
("download_and_execute_payload","Downloads and executes file on target system."),
("download_execute_and_report_payload","Downloads a file, executes it emails results"),
("reverse_backdoor","Gives root accesson remote system"),
("keylogger","Sends keylogs by email."),
("crawler","Discovers hidden paths on website."),
("discover_subdomains","Discovers subdomains on website."),
("spider","Maps whole target website, discovers files, directories and links."),
("guess_login","Wordlist brute force attack."),
("vulnerability_scanner","Scans website for weaknesses, produces full report."),
("cyber_python","A library of pentesting tools written in python",True)
]

txt = ["## Getting Started",
"Below you will find details on how to configure and run this tool.",
"### Prerequisites",
"What libraries you need and how to install them",
"```",
"Give examples",
"```",
"## Running the tests",
"Explain how to run tests for this tool",
"### Break down into end to end tests",
"Explain what these tests test and why",
"```",
"Give an example",
"```",
"## Deployment",
"Add additional notes about how to deploy this on a live system"
]


for dir in dirs:
	thedir = dir[0]
	path = "README.md" 
	if not os.path.exists(thedir) and len(dir) == 2:
		path = thedir+"/README.md"
		os.makedirs(thedir)
		f = open(thedir+"/" + thedir + ".py", "w")
		f.write("#!/usr/bin/env python \n\n")
		f.write('"""' + thedir + '.py: ' + dir[1] + '"""')
		f.close()
	f = open(path, "w")
	f.write("# " + thedir + "\n")
	f.write(dir[1] + "\n")
	for line in txt:
		f.write(line + "\n")
	f.close()	
		