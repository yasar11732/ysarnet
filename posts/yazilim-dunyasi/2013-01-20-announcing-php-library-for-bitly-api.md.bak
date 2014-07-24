<!--
.. date: 2013-01-20 20:52:43
.. slug: bitly-php-library
.. title: Announcing php library for bitly api
.. description: This library can be used to access bitly api using PHP. It tries to mimic offical Python library for bitly api.
-->

I am not sure if anyone else has done it before, but I wrote a php
library to bitly api. [Bitly Api Php github repo] is the place where you can get it. <!-- TEASER_END -->

**Basic usage:**

    :::php
    require("bitly_api.php");
    $bitly = new Bitly(array("login" => "yourlogin", "api_key" => "yourapikey"));
    # or to use oauth2 endpoints
    $bitly = new Bitly(array("access_token" => "youraccesstoken");
    $data = $bitly->shorten('http://www.google.com/');

Currently, it only supports curl to make http queries. I might add [php
http][] later on.

Please try, test, comment & contribute.

  [Bitly Api Php github repo]: https://github.com/yasar11732/bitly-api-php
    "Bitly Api Php"
  [php http]: http://php.net/manual/en/book.http.php