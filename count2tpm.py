# Convert counts to TPM
import pandas as pd
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str)
parser.add_argument('length_file', type=str)
parser.add_argument('output_file', type=str)
args = parser.parse_args()


counts = pd.read_csv(args.input_file)
length = pd.read_csv(args.length_file)


length.columns = ['gene_id', 'length']
merged = pd.merge(counts, length, 'inner')
rpkm = merged.iloc[:, 1:-1]
rpkm = 1000000 * rpkm / rpkm.sum(0)
rpkm[rpkm.columns] = 1000 * rpkm.values / merged['length'].values.reshape(-1,1)
rpkm.insert(0, merged.columns[0], merged[merged.columns[0]].values)


if args.output_file[-4:] == '.csv':
    rpkm.to_csv(args.output_file, index=False)
else:
    rpkm.to_csv(args.output_file + '.csv', index=False)


########## Sample Inputs ##########

### input_file ###
# gene_id,sample_1,sample_2
# a,1,0
# b,22,100

### length_file ###
# gene_id,length
# a,1000
# b,123