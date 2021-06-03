import struct
f = open( "/dev/input/js2", "rb" )

x = 1
y = 1
z = 0

status = [1, 1, 0]

while True:
  data = f.read(8)
  time, value, type, number = struct.unpack('IhBB', data)

  if number == 2:
    value = round(value / 32767, 2)
  else:
    value = round(0.5 - value / (32767 * 2), 2)
  status[number] = value

  print('R Pedal: %.2f, L_pedal: %.2f, Rotate: %.2f' % (status[0], status[1], status[2]))