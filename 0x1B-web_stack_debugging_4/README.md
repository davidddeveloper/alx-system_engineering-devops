# Web stack debugging #4
Ever wonder how google and facebook handle thousands incoming request and hundreds of which happen at the same time. Well in previous concept we look at employing one useful technology, that is a load balancer. A load balance receives all the request and distribute them to the servers.

Now I won't talk about loadbalancing as it won't be necessary in this debugging part. if you still want to look at the source code on how to setup loadbalancing, look at this [repo](https://github.com/davidddeveloper/alx-system_engineering-devops/tree/master/0x0F-load_balancer)

Just a quick review before we looked at why a web server might not handle requests effectively on high traffic, a web server is a software with an underlining hardware that listens to request on a specific port and respond by serving the request content. 

So if a web server then it means it uses system resources - like the ram, memory etc and make sys call - like open, read, write etc.

One thing to note that in linux is that you can actuall limit the resources a process or user have utilize. So if a process - such as an nginx web server or a user does not have enough resources it actually not work as expected.
