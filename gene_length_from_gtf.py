# Get gene length from gtf file and output a csv file
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('gtf_file', type=str)
parser.add_argument('output_file', type=str)
args = parser.parse_args()


# read gtf file
gtf_file = open(args.gtf_file, 'r')
gtf = []
for line in gtf_file:
    if 'gene\t' in line:
        gtf.append(line.split('\t'))
gtf_file.close()

# get gene id and length
out = []
for line in gtf:
    length = int(line[4]) - int(line[3])
    gene_id = line[-1].split(';')[0].split('"')[1]
    out.append(gene_id + ',' + str(length) + '\n')

# write output
if args.output_file[-4:] == '.csv':
    output = open(args.output_file, 'w')
else:
    output = open(args.output_file + '.csv', 'w')
output.writelines(out)
output.close()