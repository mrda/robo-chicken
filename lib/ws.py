import usocket as socket
import machine
import network

DEBUG = False

class WebServer:

    def __init__(self):
        self.station_if = network.WLAN(network.STA_IF)
        self.ip_addr = self.station_if.ifconfig()[0]
        self.port = 8080
        self.payload = {}
        print ("My IP Address is ", self.ip_addr)
        print ("starting webserver on port ", self.port)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.bind((self.ip_addr, self.port))
        except OSError:
            machine.reset()
        self.sock.listen(5)

    def register_url(self, verb, root, str_or_func):
        # TODO(mrda): Worry about verbs :)
        self.payload[root] = str_or_func

    def handle_url(self, verb, action, remaining):
        # TODO(mrda): Worry about verbs :)
        str_or_func = self.payload[action]
        if callable(str_or_func):
            return str_or_func(remaining)
        else:
            return selfstr_or_func

    def message(self, txt=None, err=200, s="OK"):
        return """HTTP/1.0 {0} {1}
Content-Type: text/html

{2}
""".format(err, s, txt)

    def start(self):
        self.register_url("GET", "/", "Nothing to see here, move along")
        self.register_url("GET", "/help", "This is the help string")
        while True:
            conn = None
            try:
                conn, addr = self.sock.accept()
                req = conn.recv(1024)

                req_parts = req.split()
                verb = req_parts[0].decode('ascii')
                url = req_parts[1].decode('ascii')
                req = url.split("/",2)

                action = req[1]
                remaining = req[2]

                if DEBUG:
                    print ("\nNew request:")
                    print ("  verb: ", verb)
                    print ("  action: ", action)
                    print ("  data: ", remaining)

                # Dirty trick to quit the webserver
                if req == '/quit':
                    conn.sendall(self.message(err=200, s="OK", txt="Bye"))
                    break
                try:
                    result = self.handle_url(verb, action, remaining)
                    conn.sendall(self.message(err=200, s="OK", txt=result))
                except KeyError:
                    conn.sendall(self.message(err=404, s="Not Found"))
                    print('Unsupported URL: \"%s\"' % req)
            except:
                conn.sendall(self.message(err=400, s="Bad Request"))
                print('Bad Request: \"%s\"' % req)
            finally:
                if conn is not None:
                    conn.close()


