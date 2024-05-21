# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"B713.00","system":"readv2"},{"code":"B714200","system":"readv2"},{"code":"B714.00","system":"readv2"},{"code":"B714100","system":"readv2"},{"code":"6828.0","system":"readv2"},{"code":"27925.0","system":"readv2"},{"code":"27402.0","system":"readv2"},{"code":"8825.0","system":"readv2"},{"code":"25862.0","system":"readv2"},{"code":"15062.0","system":"readv2"},{"code":"27577.0","system":"readv2"},{"code":"4961.0","system":"readv2"},{"code":"7359.0","system":"readv2"},{"code":"41898.0","system":"readv2"},{"code":"2700.0","system":"readv2"},{"code":"69106.0","system":"readv2"},{"code":"41880.0","system":"readv2"},{"code":"2922.0","system":"readv2"},{"code":"39965.0","system":"readv2"},{"code":"29916.0","system":"readv2"},{"code":"15072.0","system":"readv2"},{"code":"63594.0","system":"readv2"},{"code":"57584.0","system":"readv2"},{"code":"25999.0","system":"readv2"},{"code":"47964.0","system":"readv2"},{"code":"2207.0","system":"readv2"},{"code":"40656.0","system":"readv2"},{"code":"42868.0","system":"readv2"},{"code":"33345.0","system":"readv2"},{"code":"11340.0","system":"readv2"},{"code":"6891.0","system":"readv2"},{"code":"55538.0","system":"readv2"},{"code":"5975.0","system":"readv2"},{"code":"61560.0","system":"readv2"},{"code":"12298.0","system":"readv2"},{"code":"41672.0","system":"readv2"},{"code":"D12","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('benign-neoplasm-of-colon-rectum-anus-and-anal-canal-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["benign---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["benign---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["benign---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
