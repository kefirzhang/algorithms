 #!/bin/bash
 #'\(\d{3}\) \d{3}-\d{4}' 或 xxx-xxx-xxxx
 grep -e ''

grep -E "^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$" file.txt