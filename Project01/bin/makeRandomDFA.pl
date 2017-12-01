#!/usr/bin/perl -w

# Output to stdout a random DFA with a random alphabet.
# Optional command line arg sets the initial seed for srand

#sub main
{
    if (@ARGV) {
	print STDERR "Setting random seed to $ARGV[0]\n";
	srand($ARGV[0]);
    }

    $numStates = int(rand(200)) + 1;
    print "Number of states: $numStates\n";
    print "Accepting states:";
    for ($i=0; $i<$numStates; $i++) {
	print " $i" if int(rand(2)) == 1;
    }
    print "\nAlphabet: ";
    $alphaSize = 0;
    for ($i=ord(' '); $i<=ord('~'); $i++) {
	if (int(rand(3)) >= 1) {
	    print(chr($i));
	    $alphaSize++;
	}
    }
    print "\n";
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
