# a puppet manifest that increases the ulimit of nginx

$file_path='/etc/default/nginx'
$content = "ULIMIT=\"-n 4096\""

exec {'comment_out_ulimit':
  command => 'sudo sed -i "s/^ULIMIT=\"-n 15\"/# &/" '${file_path}''
}

exec {'the_sky_is_the_limit':
  command => 'echo '${content}' | sudo tee -a '${file_path}'',
}
