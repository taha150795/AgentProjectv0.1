# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from MasterHttpServer import MasterHttpServer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hostIP = "localhost"
    port = 8080
    https = True
    httpserver = MasterHttpServer(hostIP, port, https)
    httpserver.executeServer()




