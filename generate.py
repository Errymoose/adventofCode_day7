import re 

lines = []
with open("input.txt", "r") as f:
	lines = f.readlines()
	
c_keywords = {'do' : 'd_o', 'if': 'i_f' }
	
def bylength(word1,word2):
    return len(word1)-len(word2)

p = re.compile("([a-zA-Z0-9 ]+) -> ([a-zA-Z]+)")
out_lines = {}
for line in lines:
	m = p.search(line)
	out_line = m.group(2) + " = " + m.group(1)
	out_line = out_line.replace("RSHIFT", ">>");
	out_line = out_line.replace("LSHIFT", "<<");
	out_line = out_line.replace("AND", "&");
	out_line = out_line.replace("OR", "|");
	out_line = out_line.replace("NOT", "~");
	for kw in c_keywords.keys():
		out_line = out_line.replace(kw, c_keywords[kw])
	out_lines[m.group(2)] = out_line

f = open("program.c", "w+")
f.write('#include "stdint.h"\n')
f.write('#include "stdio.h"\n')
f.write('int main()\n')
f.write('{\n')
keylist = out_lines.keys()
keylist.sort()
keylist.sort(cmp=bylength)
for key in keylist:
	if key is not 'a':
		f.write("    uint16_t " + out_lines[key] + ";\n")

f.write("    uint16_t " + out_lines['a'] + ";\n")
f.write('\n    printf("a = %d", a);\n')
f.write('}')