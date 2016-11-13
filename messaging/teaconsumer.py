#!/usr/bin/env python3
""""
File             : teaproducer.py
Author           : ian
Created          : 11-13-2016

Last Modified By : ian
Last Modified On : 11-13-2016
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

from kombu_brighter.kombu_gateway import BrightsideKombuConsumer, BrightsideKombuConnection, BrightsideKombuProducer

def run_client():
    # setup
    topic = "cup of tea"
    connection = BrightsideKombuConnection("amqp://guest:guest@localhost:5672//", "teasmaid.exchange")
    consumer = BrightsideKombuConsumer(connection, "tea_requests", topic)

    read_message = consumer.receive(3)
    print(read_message)


if __name__ == "__main__":
    run_client()
