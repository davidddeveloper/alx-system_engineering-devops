# a puppet manifest that create an index.html file for apche2 to run corectly
$content_val = '<!DOCTYPE html>
<head>
<title>Holberton &#8211; Just another WordPress site</title>
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
</head>
<body>
        <div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div>  </div>
                            <h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
        <p>Yet another bug by a Holberton student</p>
</body>'

exec {'stop_apache2':
  command => 'sudo service apache2 stop',
  path    => ['/bin', '/usr/bin'],
}

file {'/var/www/html/index.html':
  ensure  =>  file,
  content => $content_val
}

exec {'start_apache2':
  command => 'sudo service apache2 start',
  path    => ['/bin', '/usr/bin'],
}
