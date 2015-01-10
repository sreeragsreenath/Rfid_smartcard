import serial
import MySQLdb
import time
ser = serial.Serial('COM4', 9600, timeout=0)
 
cnx = mysql.connector.connect(user='root', database='test')
cursor = cnx.cursor()

while 1:
 try:
  id = ser.readline()
  print id
  query = ("INSERT INTO test (rfid) VALUES (id)")
  cursor.execute(query)
  cnx.commit()
  cursor.close()
  cnx.close()
  time.sleep(1)
 except ser.SerialTimeoutException:
  print('Data could not be read')
  time.sleep(1)
