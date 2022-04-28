from lirc import LircdConnection
with LircdConnection(program, lircrc_path, socket_path) as conn:
	while True:
		string = conn.readline()
		print(string)
