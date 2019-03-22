The signal is not being caught inside the recursive function it just segfaults (when the signal handler is supposed to be called), I tested the signal handler with an inifite loop ( which I use segfaulted with kiss -s SEGV) and it caught the signal


The reason the signal is not caught is because the the interpreter segfaults and the the program in question
