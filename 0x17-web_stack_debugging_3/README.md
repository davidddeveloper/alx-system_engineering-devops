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
