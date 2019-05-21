# by: @paraparata
import pandas as pd
import sys, getopt
# Fungsi
def delayF(rata_delay):
    return rata_delay['Delay'].mean()/10**6

def throughputF(rata_th):
    jumlah_node = float(1)
    total_paket = float(rata_th['packetSize'].sum())
    lama_simulasi = float(rata_th['Time'].max())
    formula = ((total_paket*8/jumlah_node)/lama_simulasi)/10**6
    return formula

# Main
# File input
# filenya = 'mcDlPdcpStats_5_10_18_05_2019_05_07_16.txt'
# data = pd.read_csv(filenya, sep=" ", header=None)
# data.columns = ["Xx", "Time", "CellId", "RNTI", "LCID", "packetSize", "Delay"]
# data_rx = data[data['Xx']=='Rx']
# # print(data_rx.head(3))

# print("Delay      = {} ms", format(delayF(data_rx)))
# print("Throughput = {} Mbps", format(throughputF(data_rx)))

def main(argv):
   filenya = 'mcDlPdcpStats_5_10_18_05_2019_05_07_16.txt'
   try:
      opts, args = getopt.getopt(argv,"hi:",["help", "input"])
   except getopt.GetoptError:
      print ('qos.py <nama_file_pdcp_mmwave.txt>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('qos.py <nama_file_pdcp_mmwave.txt>')
         sys.exit()
      elif opt in ("-i", "--input"):
         filenya = arg
         data = pd.read_csv(filenya, sep=" ", header=None)
         data.columns = ["Xx", "Time", "CellId", "RNTI", "LCID", "packetSize", "Delay"]
         data_rx = data[data['Xx']=='Rx']
         # print(data_rx.head(3))
         print("Delay      = {} ms" .format(delayF(data_rx)))
         print("Throughput = {} Mbps" .format(throughputF(data_rx)))

# Main
if __name__ == "__main__":
   main(sys.argv[1:])



