#!/usr/bin/bash

set -e

filename=$([[ "$1" != "" ]] && echo "$1" || echo "day19-input.txt")
res=0

while IFS= read -r line; do
	if [[ "${line}" =~ ^([wubrg]+,\ )+[wubrg]+$ ]]; then
		pattern="^(${line//, /|})+$"
	elif [[ "${line}" =~ ${pattern} ]]; then
		res=$((res+1))
	fi
done < ${filename}

echo "Res: ${res}"
