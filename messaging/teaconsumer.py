#!/usr/bin/env python3
""""
File             : teaconsumer.py
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

from kombu_brighter.kombu_gateway import BrightsideKombuConsumer, BrightsideKombuConnection
from nutrimatic.nutrimatic_drinks_dispenser import TeaDispenser
from nutrimatic.tea_requests import BeverageType, TeaRequest
import json


def run_client():
    # setup
    topic = "cup of tea"
    connection = BrightsideKombuConnection("amqp://guest:guest@localhost:5672//", "teasmaid.exchange")
    consumer = BrightsideKombuConsumer(connection, "tea_requests", topic)

    read_message = consumer.receive(3)

    if read_message is not None:
        message_body = json.loads(read_message.body.value)
        beverage_str = message_body["_beverage_type"]
        beverage_type = BeverageType(beverage_str)
        has_milk = message_body["_has_milk"]
        no_of_sugars = message_body["_no_of_sugars"]
        tea_request = TeaRequest(beverage_type, has_milk, no_of_sugars)
        if BeverageType(tea_request.beverage_type) == BeverageType.tea:
            dispenser = TeaDispenser()
            dispenser.fill()
            dispenser.boil()
            dispenser.ready_cup()
            dispenser.pour_water()
            if tea_request.has_milk:
                dispenser.add_milk()
            if tea_request.no_of_sugars() > 0:
                dispenser.add_sugar(tea_request.no_of_sugars())


if __name__ == "__main__":
    run_client()
