# Using strace tmux and Puppet for debugging
## strace
` strace ` - a linux utility that monitors a process to find out all the system calls that process initiate, it shows the syscall, it arguments  and it outputs like so `read(6, "\177ELF\20"..., 832) = 832`. Outputs could also be any errors

` common commands `

    # monitors a process
  
    root@DESKTOP:~# # strace -p <pid>
  
    # trace a particual syscall

    strace -p <pid> -e trace=<access,write,read,network,process>
  
    # save output to a file

    strace -p <pid> -o output_file.txt

    # strace child process

    strace -f <pid>

## tmux
`tmux` - is a powerful linux command line that lets you run multiple command lines. The beauty of tmux is sessions and detaching from sessions allowing us to run multiple application on the background given us the ability to come back to them.

` common most useful commands `
` create a session ` - tmux
` create a named session ` - tmux new -s mysession
` creates a split screen (horizontal) ` - ctrl + b "
` creates a split screen (vertical) ` ctrl + b %
` moving around screens ` - ctrl + b arrows
` delete a session ` - ctl + b x
` detaching from a session ` - ctrl + b d




















