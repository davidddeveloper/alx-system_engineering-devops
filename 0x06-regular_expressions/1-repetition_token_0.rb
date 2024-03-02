#!/usr/bin/env ruby
puts ARGV[0].scan(/.{2}(t{2,5}([a-zA-z]*))/).join
