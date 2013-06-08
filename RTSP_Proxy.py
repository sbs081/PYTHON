#!/usr/bin/python

"""

RTSP Proxy v1.2
---------------
Jonathan Hogg <jonathan@onegoodidea.com>

Copyright (c) 1999 One Good Idea Limited <http://www.onegoodidea.com/>

Permission to use, copy, modify, and distribute this software and its
documentation for any purpose, without fee, and without a written agreement
is hereby granted, provided that the above copyright notice and this
paragraph and the following two paragraphs appear in all copies.

IN NO EVENT SHALL ONE GOOD IDEA LIMITED BE LIABLE TO ANY PARTY FOR DIRECT, 
INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING LOST 
PROFITS, ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, 
EVEN IF ONE GOOD IDEA LIMITED HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH 
DAMAGE.

ONE GOOD IDEA LIMITED SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, 
BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS 
FOR A PARTICULAR PURPOSE.  THE SOFTWARE PROVIDED HEREUNDER IS ON AN "AS 
IS" BASIS, AND ONE GOOD IDEA LIMITED HAS NO OBLIGATIONS TO PROVIDE 
MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.


Usage:

    % RTSP_Proxy


The proxy listens on port 7070 so that it doesn't need to be run as root
to operate (although this can be easily changed down the bottom of the
script). It is a very simple program and can get confused, but in it's
present state is about as functional as Apple's rtsp_proxy but a lot less
buggy.

"""


import sys
import string
import re
import time
from threading import *

from socket import *
if not globals().has_key('IPPROTO_TCP'):
    IPPROTO_TCP = 6

from select import *

import urlparse
try:
    if "rtsp" not in urlparse.uses_netloc:
        urlparse.uses_netloc.append("rtsp")
except:
    pass



#------------------------------------------------------------------------

class Logger:

    def __init__( self, file = sys.stderr ):
        self._lastmsg = ''
        self._first = 1
        self._repeats = 0
        self._file = file
        self._file.write( "[log started]" )
        self._lock = Lock()
    
    def log( self, msg ):
        self._lock.acquire()
        if msg == self._lastmsg:
            if self._repeats == 0:
                self._file.write( ' (.' )
            self._file.write( '.' )
            self._repeats = self._repeats + 1
        else:
            if self._repeats > 0:
                self._file.write( ')' )
            self._file.write( '\n' )
            self._first = 0
            self._file.write( msg )
            self._repeats = 0
        self._file.flush()
        if self._repeats == 75 - len(msg):
            self._lastmsg = ''
        else:
            self._lastmsg = msg
        self._lock.release()


logger = Logger()
debug = logger.log


def makeportrange( ports ):

    if len(ports) == 1:
        return "%d" % ports[0]
    else:
        return "%d-%d" % (ports[0], ports[-1])



#------------------------------------------------------------------------

class Message:

    def __init__( self, conn, new_host=None, old_host=None ):

        self._conn = conn
        self._buffer = ""
        self._content = ""
        self._command = ""
        self._arguments = []
        self._headerdict = {}
        self._headerlist = []
        self.old_host = old_host
        self.new_host = new_host
        if conn:
            self.readcommand()
            self.readheaders()
            self.readcontent()
    
    
    def readdata( self ):

        self._buffer = self._buffer + self._conn.recv( 1024 )


    def getdata( self, length):
    
        while 1:
            if len(self._buffer) >= length:
                data = self._buffer[0:length]
                self._buffer = self._buffer[length:]
                return data
            else:
                self.readdata()


    def readline( self ):
    
        while 1:
            if self._buffer == "":
                self.readdata()
            
            pos = string.find( self._buffer, "\r\n" )
        
            if pos <> -1:
                line = self._buffer[:pos]
                self._buffer = self._buffer[pos+2:]
                if self.new_host:
                    pos = string.find( line, "rtsp://")
                    if pos <> -1:
                        end1 = string.find( line[pos+7:], "/")
                        end2 = string.find( line[pos+7:], ":")
                        end = end1
                        if end == -1 or (end2 > 0 and end2 < end1):
                            end = end2
                        if end <> -1:
                            self.old_host = line[pos+7:pos+7+end]
                            print self.old_host
                            line = string.replace(line, self.old_host, self.new_host)
                            print line
                return line
        
            self.readdata()


    def readcommand( self ):
    
        line = self.readline()
        bits = string.split( line )
        self._command = bits[0]
        self._arguments = bits[1:]


    def readheaders( self ):

        self._headerdict = {}
        self._headerlist = []
        
        while 1:
            line = self.readline()
            if line == "":
                break
            if line[0] in string.whitespace:
                header[1] = header[1] + string.lstrip(line)
            else:
                (field,value) = string.split( line, ":", 1 )
                header = [field, string.strip(value)]
                self._headerlist.append( header )
                self._headerdict[string.lower(field)] = header


    def readcontent( self ):
        
        length = self.getheader('content-length')
        if length:
            self._content = self.getdata( int(length) )
            if self.new_host:
                pos = string.find( self._content, "rtsp://")
                if pos <> -1:
                    end1 = string.find( self._content[pos+7:], "/")
                    end2 = string.find( self._content[pos+7:], ":")
                    end = end1
                    if end == -1 or (end2 > 0 and end2 < end1):
                        end = end2
                    if end <> -1:
                        old_host = self._content[pos+7:pos+7+end]
                        self._content = string.replace(self._content, old_host, self.new_host)

            if self.new_host and self.old_host:
                self._content = string.replace(self._content, self.old_host, self.new_host)
        else:
            self._content = ""


    def getmessage( self ):
        print self._command
        print self._arguments
        print self._headerlist
        msg = self._command + " " + string.join( self._arguments ) + "\r\n"
        
        for header in self._headerlist:
            msg = msg + "%s: %s\r\n" % (header[0], header[1])

        msg = msg + "\r\n" + self._content
        
        return msg
        

    def getheader( self, field ):
        
        name = string.lower( field )
        if self._headerdict.has_key( name ):
            print self._headerdict[name]
            return self._headerdict[name][1]
        else:
            return None


    def setheader( self, field, value ):
        
        self._headerdict[string.lower(field)][1] = value
        self._headerlist.append([field, string.strip(value)])


    def getcommand( self ):

        return self._command
    
    
    def setcommand( self, command ):

        self._command = command
    
    
    def getargs( self ):
    
        return self._arguments


    def setargs( self, args ):

        self._arguments = args
    
    

#------------------------------------------------------------------------

class Session( Thread ):

    RTSP_PORT = 554


    def __init__( self, conn, addr, server_conn, server_addr ):
    
        Thread.__init__( self )
        self._clientconn = conn
        self._clientaddr = addr
        self._serverconn = server_conn
        self.new_host = ""
        if server_addr:
            self.new_host = server_addr[0]
            self._serveraddr = server_addr[0]
        self.old_host = None
        self.setDaemon( 1 )


    def getclientmsg( self ):
        return Message( self._clientconn, self.new_host )


    def sendclientmsg( self, msg ):
        self._clientconn.send( msg.getmessage() )

    
    def getservermsg( self ):
        msg = Message( self._serverconn, self.old_host, self.new_host )
        return msg


    def sendservermsg( self, msg ):
        self._serverconn.send( msg.getmessage() )

    
    def dispatch( self, msg ):

        command = msg.getcommand()
        
        debug( "got command: " + command )
        
        if command == "DESCRIBE":
            self.do_describe( msg )
            
        elif command == "SETUP":
            self.do_setup( msg )
            
        elif command == "OPTIONS":
            self.do_options( msg )

        else:
            self.sendservermsg( msg )
            response = self.getservermsg()
            self.sendclientmsg( response )
    
    
    def do_options( self, msg ):
    
        print 'do_options'
        resp = 'RTSP/1.0 200 OK\r\n'
        resp += 'CSeq: 1\r\n'
        resp += 'Public: DESCRIBE, SETUP, PLAY, PAUSE, TEARDOWN, OPTIONS\r\n\r\n'
        self._clientconn.send(resp)


    def do_describe( self, msg ):
    
        url = msg.getargs()[0]
        parsed_url = urlparse.urlparse( url, "rtsp" )
        site = parsed_url[1]
        self._client_type = msg.getheader('user-agent')
        debug( "  client is a: %s" % self._client_type )
        self.old_host = msg.old_host

        pos = string.find( site, ":" )
        if pos >= 0:
            addr,port = string.split( site, ":" )
            port = int( port )
        else:
            addr = site
            port = self.RTSP_PORT
        
        if not self._serverconn:
            debug( "  trying connection to %s:%d" % (addr,port) )
            sock = socket( AF_INET, SOCK_STREAM )
            sock.connect( (addr,port) )
            self._serverconn = sock
            self._serveraddr = addr
        
        self.sendservermsg( msg )
        print msg.getmessage()
        response = self.getservermsg()
        print response.getmessage()
        self._server_type = response.getheader('server')
        debug( "  server is a: %s" % self._server_type )
        self.sendclientmsg( response )


    def do_setup( self, msg ):
    
        client_port = ''
        
        debug( "  client requests of proxy:\n    %s" % msg.getheader('transport') )
        
        for bit in string.split( msg.getheader('transport'), ";" ):
            bit = string.strip( bit )
            
            if string.find( bit, '=' ) > 0:
                name, value = string.split( bit, '=', 1 )
            
                if name == 'client_port':
                    client_port = value

        if string.find( client_port, "-" ):
            startport,endport = string.split( client_port, "-" )
            clientports = range( int(startport), int(endport) + 1 )
        else:
            clientports = [ int(client_port) ]
            
        proxy = Forwarder( self._clientaddr, clientports )
        print 'initialize a forwarder'
        print self._clientaddr

        msg.setheader( 'transport', 'RTP/AVP;unicast;client_port=' + proxy.getportrange() )

        debug( "  proxy requests of server:\n    " + msg.getheader('transport') )
        
        self.sendservermsg( msg )
        response = self.getservermsg()
        
        server_port = ''
        source = ''
        
        debug( "  server offers to proxy:\n    " + response.getheader('transport') )
        
        for bit in string.split( response.getheader('transport'), ";" ):
            bit = string.strip( bit )
            
            if string.find( bit, '=' ) > 0:
                name, value = string.split( bit, '=', 1 )
            
                if name == 'server_port':
                    server_port = value
                
                elif name == 'source':
                    source = value
        
        if string.find( server_port, "-" ):
            startport,endport = string.split( server_port, "-" )
            serverports = range( int(startport), int(endport) + 1 )
        else:
            serverports = [ int(server_port) ]
        
        
        if source <> '':
            addr = source
        else:
            addr = self._serveraddr
            
        proxy.setserver( addr, serverports )
        proxy.start()
        
        response.setheader( 'transport',
                            'RTP/AVP;unicast;client_port=%s;server_port=%s' % (client_port,
                                proxy.getportrange()) )

        debug( "  proxy offers to client:\n    " + response.getheader('transport') )
        
        self.sendclientmsg( response )


    def run( self ):
    
        try:
            print 'begin listening'
            while 1:
                msg = Message( self._clientconn, self.new_host )
                self.dispatch( msg )
        
        except Exception, e:
            debug( "taking down session" )
            print e
            self._clientconn.close()
            if self._serverconn:
                self._serverconn.close()



#------------------------------------------------------------------------

class Listener:


    def __init__( self, client_port, server_port ):
    
        self._client_sock = socket( AF_INET, SOCK_STREAM )
        self._client_sock.bind( ('',client_port) )
        self._server_sock = socket( AF_INET, SOCK_STREAM )
        self._server_sock.bind( ('',server_port) )
#        self._sock.setsockopt( IPPROTO_TCP, SO_REUSEADDR, 1 )
        self._client_sock.listen( 5 )
        self._server_sock.listen( 5 )
        self.server_conn = None
        self.server_addr = None
        
    def waitforserver( self ):
        
        self.server_conn, self.server_addr = self._server_sock.accept()
        debug( "accepted server connection from %s:%d" % self.server_addr )
        msg = Message( self.server_conn )
        print msg.getmessage()
        resp = "RTSP/1.0 200 OK\r\nCSeq: 1\r\n\r\n"
        self.server_conn.send( resp )

    def waitforclient( self ):
    
        conn, addr = self._client_sock.accept()
        print self.server_addr
        debug( "accepted connection from %s:%d" % addr )
        return Session( conn, addr[0], self.server_conn, self.server_addr )


    def stop( self ):
        self._server_sock.close()
        self._client_sock.close()



#------------------------------------------------------------------------

class Forwarder( Thread ):

    START_PORT = 10000
    _currentport = START_PORT
    

    def __init__( self, addr, ports ):
    
        Thread.__init__( self )
        self._clientaddr = gethostbyname( addr )
        self._clientports = ports
        self.buildports()
        self.setDaemon( 1 )
    
    
    def _allocateports( self, howmany ):
    
        start = Forwarder._currentport
        sofar = 0
        socks = []
        
        while sofar < howmany:
        
            sock = socket( AF_INET, SOCK_DGRAM )
            port = Forwarder._currentport
            Forwarder._currentport = Forwarder._currentport + 1
            
            try:
                sock.bind( ('',port) )
            except:
                sofar = 0
                start = self._currentport
                socks = []
                
            socks.append( (port,sock) )
            sofar = sofar + 1
            end = port
        
        debug( "  allocated a port range at %d-%d" % (start,end) )

        return socks


    def setserver( self, addr, ports ):
    
        self._serveraddr = gethostbyname( addr )
        self._serverports = ports

    
    def getportrange( self ):
    
        ports = map( lambda x: x[0], self._proxysocks )
        return makeportrange( ports )


    def doforwarding( self ):
    
        sockets = map( lambda x: x[1], self._proxysocks )
        count = 0
        size = 0
        then = time.time()
    
        while 1:
            readylist, _, _ = select( sockets, [], [] )
            
            for i in range(len(self._proxysocks)):
            
                port, sock = self._proxysocks[i]
                clientport = self._clientports[i]
                serverport = self._serverports[i]
                
                if sock in readylist:
                    (packet, addr) = sock.recvfrom( 2048 )
                    
#                    if addr == (self._serveraddr, serverport):
                    if addr[0] == self._serveraddr:
                        count = count + 1
                        size = size + len(packet)
                        sock.sendto( packet, (self._clientaddr, clientport) )
                        
                   
                        now = time.time()
                        elapsed = now - then
                        if elapsed > 30.0:
                            rate = (size * 8) / elapsed
                            debug( "forwarding rate approx %dbps on ports %s" % (rate,
                                        self.getportrange()) )
                            count = 0
                            size = 0
                            then = now
                            
                    elif addr == (self._clientaddr, clientport):
                        debug( "forwarding from client" )
                        sock.sendto( packet, (self._serveraddr, serverport) )
                    
                    elif addr[0] == self._clientaddr:
                        debug( "Change client port from %d to %d" % (clientport, addr[1]) )
                        self._clientports[i] = addr[1]                        
#                        sock.sendto( packet, (self._serveraddr, serverport) )
                        sock.sendto( packet, (self._clientaddr, addr[1]) )
                        
                    elif addr[1] == serverport:
                        debug( "server %s lied about its' address, it's really %s" % (
                            self._serveraddr, addr[0]) )
                        self._serveraddr = addr[0]
                        sock.sendto( packet, (self._clientaddr, clientport) )
                    
                    else:
                        debug( "forwarder received packet from unexpected source, %s:%d" % addr )
            


    def run( self ):
    
        debug( "  starting an RTP forwarder on ports " + self.getportrange() )
        debug( "    server %s:%s  <->  client %s:%s" % (
            self._serveraddr, makeportrange(self._serverports),
            self._clientaddr, makeportrange(self._clientports)))

        try:
            self.doforwarding()

        except Exception, e:
            debug( "stopping forwarder on ports " + self.getportrange() )
            print e
        
    
    def buildports( self ):
    
        num = len( self._clientports )
        self._proxysocks = self._allocateports( num )



#------------------------------------------------------------------------

def main( argv ):

    listener = Listener( 554, 7070 )
    
    debug( "waiting for a client" )
    
    try:
        while 1:
#            listener.waitforserver()
            listener.server_addr = ('211.136.165.57', 554);
            client = listener.waitforclient()
            client.start()

    finally:
        listener.stop()


if __name__ == "__main__":
    main( sys.argv )


