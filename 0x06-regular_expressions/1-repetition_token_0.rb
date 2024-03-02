#!/usr/bin/env ruby
puts ARGV[0].scan(/([a-zA-z][a-zA-z])(t{2,5})(.[^t])/).join
