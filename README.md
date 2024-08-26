# ClickTest Information
this is just a test repository of me playing around with click to see how it works and what it could do

## Why Click
its a neat library that simplifies and modernizes the whole argument parsing and creation process. typically, creating arguments requires literally hundreds of lines with pointing to another function, it can be extremely hard to write and lacks the usage of decorators. Click fixes that.

## Commands
You can import commands / python files locally or via directory. ideally, importing it from a repository would be sexy but that would require `importlib` or `pip` to directly install it, not ideal and great compared to golang. however, the importing process is still simple that allows it to be very modular.

1. link that shit
`ln -s /Users/jremillard/workbench/Python/ClickTest/mycli.py /usr/local/bin/mycli`
2. what version you using
`mycli version`
3. figure it out, this is mostly display from click which is neat, helps documentation
```
mycli help                                                                                                                  Usage: mycli [OPTIONS] COMMAND [ARGS]...

  A CLI tool with multiple commands.

Options:
  --help  Show this message and exit.

Commands:
  delete-snapshot  Deletes an AWS snapshot given its snapshot ID.
  greet            Greet someone with a custom message.
  hello            Prints 'Hello, World!'.
  help             Show this message and exit.
  stop-instance    Shuts down an EC2 instance given its instance ID.
  version          Display the version of mycli.
```

## Exmaple outputs
```
╭─jremillard@MacBook-Pro-2 ~/workbench/Python/ClickTest ‹main*› 
╰─$ mycli hello                                                                                               
Hello, World!
╭─jremillard@MacBook-Pro-2 ~/workbench/Python/ClickTest ‹main*› 
╰─$ mycli greet --name jaryd --greeting ohshitwuddup
ohshitwuddup, jaryd!
```

## Disclaimers
I have no idea if these python scripts actually work and they are definitely not prod safe, I just slapped this repository together to showcase it can be modularized and import an in-house library of scripts.