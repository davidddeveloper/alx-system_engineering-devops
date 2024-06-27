# Web stack debugging #4

## Instroduction 
Ever wonder how google and facebook handle thousands incoming request and hundreds of which happen at the same time. Well in previous concept we look at employing one useful technology, that is a load balancer. A load balancer receives all the incoming request and distribute them to the servers.

Now I won't talk about loadbalancing and it mechanism as it won't be necessary in this debugging part. if you still want to look at the source code on how to setup loadbalancing, look at this [repo](https://github.com/davidddeveloper/alx-system_engineering-devops/tree/master/0x0F-load_balancer)

## Discussion
Just a quick review before we looked at why a web server might not handle requests effectively on high traffic, a web server is a software with an underlining hardware that listens to request on a specific port and respond by serving the request content. 

So if a web server is a software then it means it uses system resources - like the ram, memory etc and make sys call - like open, read, write etc.

One thing to note, is that in linux you can actually limit the resources a process or a user can utilize. So if a process - such as an nginx web server or a user does not have enough permission to use system resources it would actually not work as expected or may even break.

For example, if nginx is limited to open 15 number of files at a time, it might actually work well in low traffic but not so well in high traffic - many if not all, incoming request request, might not be processed. The same goes for a user, if the limit to the number of files he/she can open is too low, then he/she might not be able to open a file, create a file, change director etc. 

## Solution
### configure nginx to handle at high traffic
According to the context I already posed above, to configure nginx to process all incoming request at high traffic we need to consider increasing the system resource that nginx process can use. For this debugging project we only need to increase one system resource and that is the number of open files or socket that nginx can have at a time, but note that their are other optimization we can do, which I'll mention briefly.

`open ` 

      /etc/default/nginx

`add` 

      ULIMIT="-n 4096" # commet out any other ULIMIT directive

Othor things we can do. Note that you don't have to.
You can increase the number of worker process, increase the number of worker connections etc.

#### increase the number of worker processes
By default nginx have 4 worker process, you can increase it to 8 like so.
` open `
    
    vi /etc/nginx/nginx.conf

` increase worker processes `

    worker_processes 8; # replace with 8 or just auto

` increase worker connections `

    worker_connections 768; # replace 768 with 1000 or more

### configure os to allow users
Again a user may not able to open, read or write if the limit to system resources is low. You might think that just by doing chmod will permit a user to perform operation, no this it will not work if the user is limited as to the number of open files. Now here is the solution.

` open `

    /etc/security/limits.conf

` replace `

    <domain>        <type>  <item>  <value>
    dave            hard    nofile  4
    dave            soft    nofile  2

  with just noting ` or ` with a higher value

      <domain>        <type>  <item>  <value>
      dave            hard    nofile  100
      dave            soft    nofile  50

## Conclution
I was very impressed when I first learnt about ulimit. It is a very powerful tool. You can use it as 
a system administrator to set the limit a user to certain extent. Note also that you can use it on the command line like so:

      ulimit -n 100
