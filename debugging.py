def update(x, y):
  y = y * 10
  x = x + 3
  num = x + y
  return num


x = 20
y = 50
breakpoint()
out = update(x, y)

breakpoint()
"""
s(tep)–  The command, in this case, is reduced to s which executes the current line and stops in the next line of the current function or when a function is called.   
n(next) – Unlike the step command which stays and stops inside the current function this command executes called functions. 
The p expression –  Executes and prints the values of the expression in the current context.
c(continues)  – Executes code and only stops when a breakpoint is encountered.
"""

import logging

logging.basicConfig(filename='6-27-23_LOGS.log',
                    encoding='utf-8',
                    level=logging.DEBUG)
logging.debug("This message goes to the log file")
logging.info("This info goes to the log file")
logging.warning("This is a loud warning!")
logging.error("An error occurred!")

import logging
import mylib


def main():
  logging.basicConfig(filename='main_log.log', level=logging.INFO)


logging.info('Started')
mylib.do_something()
logging.info('Finished')

if __name__ == '__main__':
  main()
