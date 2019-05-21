from tableaudocumentapi import Datasource, Workbook
import sys, getopt

def main(argv):
   server = None
   port = None
   filename = None
   username = None
   opts, args = getopt.getopt(argv,"hs:f:u:d:",["server=","filename=","username=","dbname="])
   for opt, arg in opts:
     if opt == '-h':
        print('update_datasource.py -f <filename> -u <username> -s <server> -d <dbname>')
        sys.exit()
     elif opt in ("-s", "--server"):
        server = arg
     elif opt in ("-f", "--filename"):
        filename = arg
     elif opt in ("-u", "--username"):
        username = arg
     elif opt in ("-d", "--dbname"):
        dbname = arg
     
   print('filename  is ', filename)
   print('username is ', username)
   print('server is ', server)
   print('dbname is ', dbname)
   
   datasource = Datasource.from_file(filename)

   if username:
      datasource.connections[0].username = username
   if server:
      datasource.connections[0].server = server
   if dbname:
      datasource.connections[0].dbname = dbname

   datasource.save()
   
if __name__ == "__main__":
   main(sys.argv[1:])