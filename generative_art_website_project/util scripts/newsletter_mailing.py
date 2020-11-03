from mailer import Mailer
from mailer import Message

message = Message(From="raunitd.it.17@nsit.net.in",
                  To="parullakhotia@gmail.com")
message.Subject = "An HTML Email"
message.Html = """<p>Hi!<br>
   How are you?<br>
   Here is the <a href="http://www.python.org">link</a> you wanted.</p>"""

sender = Mailer('smtp.example.com')
sender.send(message)
