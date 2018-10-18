"""
"""

class SimpleFactory():


    @staticmethod
    def build_connection(protocol):

        if protocol == "http":
            return( HTTPConnection())
        elif protocol == "ftp":
            return( FTPConnection())
        else:
            raise RunTimeError("Unknown protocol")

if __name__ == "__main__":

    protocol = input("Which protocol to use ?")
    protocol = SimpleFactory.build_connection(protocol)

    protocol.connect()
    print(protocol.get_response())
