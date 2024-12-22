#!/bin/env python
# Solution is 6227018762750

import sys

def main():
	chksum = 0
	file = sys.argv[1] if len(sys.argv)>=2 else 'day09-input.txt'
	with open(file, 'r') as f:
		disk_map = list(map(int, f.readline()[:-1]))

	blocks_map_index = 0
	free_blocks = []
	file_blocks = []

	for i, n in enumerate(disk_map):
		if i & 0x1:
			free_blocks.append((blocks_map_index, n))
		else:
			file_blocks.append([blocks_map_index, i // 2, n])
		blocks_map_index += n

	for i, (file_index, file_id, file_size) in reversed(list(enumerate(file_blocks))):
		for j, (free_index, free_size) in enumerate(free_blocks):
			if free_index >= file_index:
				break
			if file_size <= free_size:
				file_blocks[i][0] = free_index
				free_blocks[j] = (free_index + file_size, free_size - file_size)
				break
		size = file_blocks[i][2]
		while size:
			size -= 1
			chksum += file_id * (file_blocks[i][0] + size)

	print(f"checksum: {chksum}")

if __name__ == "__main__":
	exit(main())
