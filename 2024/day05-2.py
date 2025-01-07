#!/bin/env python
# Solution is 4480

import re
import sys

next_pages = {}
prev_pages = {}
pages_list = []

def swap_pages(pages, p1, p2):
	ip1 = pages.index(p1)
	ip2 = pages.index(p2)
	p = pages[ip1];
	pages[ip1] = pages[ip2]
	pages[ip2] = p

def check_pages(pages):
	res = True
	for p1 in pages:
		p2_before_p1 = True
		for p2 in pages:
			if p1 == p2:
				p2_before_p1 = False
				continue

			if p2_before_p1:
				if p2 in prev_pages and p1 in prev_pages[p2]:
					res = False
			else:
				if p2 in next_pages and p1 in next_pages[p2]:
					res = False

			if not res:
				swap_pages(pages, p1, p2)
				return False

	return True

def add_page(pages, p1, p2):
	if p1 in pages:
		pages[p1].append(p2)
	else:
		pages[p1] = [ p2 ]

def main():
	file = sys.argv[1] if len(sys.argv)>=2 else 'day05-input.txt'
	with open(file, 'r') as f:
		for line in f:
			m = re.match(r"(\d+)\|(\d+)", line)
			if m is not None:
				add_page(next_pages, m.group(1), m.group(2))
				add_page(prev_pages, m.group(2), m.group(1))
				continue

			m = re.match(r"(\d+,)+\d+", line)
			if m is not None:
				pages_list.append(m.group(0).split(','))

	res = 0
	for pages in pages_list:
		if not check_pages(pages):
			while (True):
				if check_pages(pages):
					middle_page = pages[int(len(pages) / 2)]
					res += int(middle_page)
					break;

	print(f"res: {res}")

if __name__ == "__main__":
    exit(main())
