#!/bin/env python
# Solution is css,cwt,gdd,jmv,pqt,z05,z09,z37

import re
import sys

def main():
	file = sys.argv[1] if len(sys.argv)>=2 else 'day24-input.txt'
	_inputs, _gates = open(file, 'r').read().split('\n\n')

	inputs = {}
	for i in _inputs.strip().split('\n'):
		w, v = i.split(': ')
		inputs[w] = int(v)

	z_msb = "z00"
	gates = set()
	for g in _gates.strip().split('\n'):
		m = re.match(r'^(...) ([ANDXOR]+) (...) -> (...)', g)
		gates.add((m.group(1), m.group(2), m.group(3), m.group(4)))
		out = m.group(4)
		if out.startswith("z") and out > z_msb:
			z_msb = out

	# The puzzle input describes a full-adder taking x and y bits as inputs
	# and output the results in z bits.
	#
	# Here is a representation that inputs 2 4-bits words from x and y and
	# adds them to a 5-bits result in z.
	#
	# So no need to fix the circuitry but only check for obvious errors and
	# report them.
	#
	#    x00──┬─┐
	#         │ │XOR──z00
	#    y00─┬┼─┘
	#        │└─┐
	#        │  │AND───────┬─┐
	#        └──┘          │ │XOR──z01
	#       x01──┬─┐    ┌─┬┼─┘
	#            │ │XOR─┘ │└─┐
	#       y01─┬┼─┘      │  │AND─┐
	#           │└─┐      └──┘    │OR─┬─┐
	#           │  │AND───────────┘   │ │XOR──z02
	#           └──┘            ┌────┬┼─┘
	#          x02──┬─┐         │    │└─┐
	#               │ │XOR──────┘    │  │AND──┐
	#          y02─┬┼─┘              └──┘     │OR─┬─┐
	#              │└─┐         ┌─────────────┘   │ │XOR──z03
	#              │  │AND──────┘ ┌──────────────┬┼─┘
	#              └──┘           │              │└─┐
	#             x03──┬─┐        │              │  │AND─┐
	#                  │ │XOR─────┘              └──┘    │OR──z04
	#             y03─┬┼─┘        ┌──────────────────────┘
	#                 │└─┐        │
	#                 │  │AND─────┘
	#                 └──┘

	bad = set()
	for w1, op, w2, out in gates:
		# All z bits come from XOR gates, except for z msb which comes
		# from an OR gate as it is the last carry
		if out.startswith("z") and op != "XOR" and out != z_msb:
			bad.add(out)
			continue

		# XOR gates (that sums 2 bits or the sum of 2 bits plus the
		# previous carry) must input at least one x or y bit or output
		# a z bit
		if (op == "XOR" and
		    w1[0] not in ["x", "y"] and
		    w2[0] not in ["x", "y"] and
		    out[0] not in ["z"]):
			bad.add(out)
			continue

		# Verify where the current gate output lands
		# All AND gates except the one 'x00 AND y00' (the first carry)
		# must output to a OR gate
		# All XOR gates must output to a XOR or AND gate
		for _w1, _op, _w2, _ in gates:
			if out != _w1 and out != _w2:
				continue

			if ((op == "AND" and "x00" not in [w1, w2] and _op != "OR") or
			    (op == "XOR" and _op == "OR")):
				bad.add(out)

	print(f"Res: {','.join(sorted(bad))}")


if __name__ == "__main__":
    exit(main())
