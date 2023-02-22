# Get gene length from gff file and output a csv file
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('gff_file', type=str)
parser.add_argument('output_file', type=str)
args = parser.parse_args()


# read gtf file
gff_file = open(args.gff_file, 'r')
gff = []
for line in gff_file:
    if 'gene\t' in line:
        gff.append(line.split('\t'))
gff_file.close()

# get gene id and length
out = []
for line in gff:
    length = int(line[4]) - int(line[3])
    gene_id = line[-1].split(';')[2].lstrip('Name=')
    out.append(gene_id + ',' + str(length) + '\n')

# write output
if args.output_file[-4:] == '.csv':
    output = open(args.output_file, 'w')
else:
    output = open(args.output_file + '.csv', 'w')
output.writelines(out)
output.close()