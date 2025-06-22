import numpy as np

M = np.random.rand(3,3)*5

fmt = f"{{:.{3}f}}"

data = []
for line in M:
    fmtd_line = [fmt.format(x) for x in line]
    data.append(fmtd_line)

for line in data:
    str_line = "| "
    for x in line:
        str_line += f"{x} | "
    print(str_line)