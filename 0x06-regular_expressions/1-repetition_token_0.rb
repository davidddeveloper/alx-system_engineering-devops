#!/usr/bin/env ruby
puts ARGV[0].scan(/[hb](.t{2,5}([a-zA-z]*))/).join
