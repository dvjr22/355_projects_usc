#!/usr/bin/perl -w

# Output to stdout a random DFA with specified parameters
#
# Command line args:
#   1.  number of states N (integer)
#   2.  expected number A of accepting states (integer) (each state is made
#               accepting with probability A/N, independently)
#   3.  alphabet (string)
#   4.  initial seed for srand (optional)

#sub main
{
    if (!@ARGV) {
	print STDERR "Arguments: no_states expected_no_final alphabet [seed]\n";
	exit(1);
    }
    $numStates = shift @ARGV;
    $expectedAcc = shift @ARGV;
    $alphabet = shift @ARGV;
    $alphaSize = length $alphabet;
    if (@ARGV) {
	print STDERR "Setting random seed to $ARGV[0]\n";
	srand($ARGV[0]);
    }

    print "Number of states: $numStates\n";
    print "Accepting states:";
    for ($i=0; $i<$numStates; $i++) {
	print " $i" if int(rand($numStates)) < $expectedAcc;
    }
    print "\nAlphabet: $alphabet\n";
    die "Empty alphabet\n"
	if $alphaSize == 0;

    for ($i=0; $i<$numStates; $i++) {
	$state = int(rand($numStates));
	print "$state";
	for ($j=1; $j<$alphaSize; $j++) {
	    $state = int(rand($numStates));
	    print " $state";
	}
	print "\n";
    }
}
