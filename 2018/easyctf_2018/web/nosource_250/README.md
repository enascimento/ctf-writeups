# EasyCTF_2018: NoSource

**Category:** Web
**Points:** 250
**Description:**

>All you CTFers are sure getting on my nerves with your source-viewing and developer tools-ing! Alas, despite my best wishes, the experienced programmers on the wonderful website StackOverflow tell me that it's [impossible](https://stackoverflow.com/q/6597224/689161) to keep you from looking at the HTML. But a disable right click script certainly won't stop an experienced CTFer like you! So finding the flag in the source of this problem should be no trouble, [right](http://c1.easyctf.com:12486/)?

## Write-up
Essentially, the crux of this problem is that no developer's console could ever save you from the pain. To get around the problem of not having developer's console, I simply packet dumped my traffic and picked the packet containing the actual HTML page. What you end up getting is the source code!

    <!-- Stop looking at the source code -->
    <!doctype html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Stop looking at the source code</title>
    <script class="delete">
      var timeout = setTimeout(function () {
        location.replace('/soupd?2');
      }, 2000);
    </script>
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">
    <link href="/static/css/main.css" rel="stylesheet">
    </head>

    <body>
    <main role="main" class="container">
    <div class="starter-template">
      <h1>Stop looking at the source code</h1>
      <p class="lead">
        Welcome to the problem page! Please enter the flag below.
      </p>
      <form id="flag-form">
        <div class="form-group">
          <input type="text" class="form-control" id="flag" placeholder="easyctf{">
        </div>
        <button type="submit" class="btn btn-success btn-lg">Check</button>
      </form>
    </div>

    <script class="delete">
      // Ah, old friend, we meet again...
      function process(a, b) {
        'use strict';
        var len = Math.max(a.length, b.length);
        var out = [];
        for (var i = 0, ca, cb; i < len; i++) {
          ca = a.charCodeAt(i % a.length);
          cb = b.charCodeAt(i % b.length);
          out.push(ca ^ cb);
        }
        return String.fromCharCode.apply(null, out);
      }

      (function () {
        'use strict';

        function soupd() {
          document.documentElement.innerHTML = '';
          location.replace('/soupd?2');
          setInterval(function () {
            location.replace('/soupd?12');
          }, 100);
        }

        try {
          let badNodes = document.getElementsByClassName('delete');
          for (let i = 0; i < badNodes.length; i++) {
            badNodes[i].parentNode.removeChild(badNodes[i]);
          }
        } catch (e) {}

        try {
          window.history.pushState({}, 'Stop looking at the source', '/');
        } catch (e) {}

        try {
          var element = new Image('/static/img/soup.png');
          Object.defineProperty(element, 'id', { get: function () {
            soupd();
          }});
          eval("console.log('Stop looking at the source code%c', element);");
        } catch (e) {}

        var formEl = document.getElementById('flag-form');
        var inputEl = document.getElementById('flag');

        var func = "(function (e, v) { e.preventDefault() || " +
            "alert(inputEl.value === process(this.prototype.flag, " +
            "this.prototype.key) ? 'Your flag is correct!' : " +
            "'Incorrect, try again.'); })";
        var f = 'DQ4cJgsbCVofB18sNw4wRlhfCwAbXxpTC1wwKVlcGBIaUDAGJzowYDoqTiI=';
        var p = { prototype: { flag: atob(f), key: 'heheheh!' }};

        document.addEventListener('DOMContentLoaded', function () {
          formEl.addEventListener('submit', eval(func).bind(p));
          $('.delete').remove();
        });

      })();
    </script>
    </main>

    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="/static/js/jquery-3.2.1.slim.min.js"></script>
    <script src="/static/js/popper.min.js"></script>
    <script src="/static/js/bootstrap.min.js"></script>
    <script class="delete">clearTimeout(timeout);</script>

    </body>
    </html>

The parts we want to focus more on is this two,

    // Ah, old friend, we meet again...
      function process(a, b) {
        'use strict';
        var len = Math.max(a.length, b.length);
        var out = [];
        for (var i = 0, ca, cb; i < len; i++) {
          ca = a.charCodeAt(i % a.length);
          cb = b.charCodeAt(i % b.length);
          out.push(ca ^ cb);
        }
        return String.fromCharCode.apply(null, out);
      }

and

    var func = "(function (e, v) { e.preventDefault() || " +
            "alert(inputEl.value === process(this.prototype.flag, " +
            "this.prototype.key) ? 'Your flag is correct!' : " +
            "'Incorrect, try again.'); })";
        var f = 'DQ4cJgsbCVofB18sNw4wRlhfCwAbXxpTC1wwKVlcGBIaUDAGJzowYDoqTiI=';
        var p = { prototype: { flag: atob(f), key: 'heheheh!' }};

        document.addEventListener('DOMContentLoaded', function () {
          formEl.addEventListener('submit', eval(func).bind(p));
          $('.delete').remove();
        });

So it appears we have the same thing going on in Jr. however unlike this time, you can't just use Chrome's developer console to evaluate your script, what next? Well, I happen to have TamperMonkey installed so this script sufficed!

    // ==UserScript==
    // @name         New Userscript
    // @namespace    http://tampermonkey.net/
    // @version      0.1
    // @description  try to take over the world!
    // @author       You
    // @match        http://c1.easyctf.com:12486/*
    // @grant        none
    // ==/UserScript==

    (function() {
        'use strict';
        // Your code here...
        var f = 'DQ4cJgsbCVofB18sNw4wRlhfCwAbXxpTC1wwKVlcGBIaUDAGJzowYDoqTiI=';
        var p = { prototype: { flag: atob(f), key: 'heheheh!' }};
        alert(process(p.prototype.flag, p.prototype.key));
    })();

Therefore, the flag is `easyctf{wh0s_a_g00d_s0urc3_v13w3r?_YOU_ARE!}`.
