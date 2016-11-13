#!/usr/bin/env python3
""""
File             : teaserver.py
Author           : ian
Created          : 07-05-2016

Last Modified By : ian
Last Modified On : 07-05-2016
***********************************************************************
The MIT License (MIT)
Copyright © 2015 Ian Cooper <ian_hammond_cooper@yahoo.co.uk>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
***********************************************************************
"""

import logging
from xmlrpc.server import SimpleXMLRPCServer
from core.nutrimatic_drinks_dispenser import TeaDispenser


def run_server():
    # set set up logging
    logging.basicConfig(level=logging.DEBUG)

    # create the rpc server
    server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True, allow_none=True)
    dispenser = TeaDispenser()

    server.register_function(dispenser.fill)
    server.register_function(dispenser.boil)
    server.register_function(dispenser.ready_cup)
    server.register_function(dispenser.pour_water)
    server.register_function(dispenser.add_milk)
    server.register_function(dispenser.add_sugar)
    server.register_function(dispenser.done)

    try:
        print("Listening for RPC requests")
        print("Use CTRL+C to exit")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting")


if __name__ == "__main__":
    run_server()


