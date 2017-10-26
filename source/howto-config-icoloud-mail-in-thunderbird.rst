How to configure iCloud mail in Mozilla Thunderbird
***************************************************

:date: 2017-01-25
:slug: howto-config-icoloud-mail-in-thunderbird
:tags: mail, thunderbird
:category: software
:author: Dormouse Young
:summary: How to configure iCloud mail in Mozilla Thunderbird

Incoming::

    Protocol: IMAP
    Server: imap.mail.me.com
    Port: 993
    SSL: SSL/TLS
    Authentication: Normal password

Outgoing::

    Protocol: SMTP
    Server: smtp.mail.me.com
    Port: 587
    SSL: STARTTLS
    Authentication: Normal password

Username for both should just be your actual username "dormouse.young", not
your whole email address.
