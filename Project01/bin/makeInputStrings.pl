#!/usr/bin/perl

# Read in an alphabet from stdin and produce a random number of random
# strings over the alphabet.  Output is to stdout.

# optional command line arg sets the initial seed for srand

if (@ARGV) {
    print STDERR "Setting random seed to $ARGV[0]\n";
    srand($ARGV[0]);
}

<STDIN>;
<STDIN>;
$alphabet = <STDIN>;
chomp $alphabet;
$alphabet =~ s/Alphabet: //;

print STDERR "Alphabet: $alphabet\n";
$alphaLen = length($alphabet);
print STDERR "Alphabet length = $alphaLen\n";
$numStrs = int(rand(10)) + 1;
print STDERR "Generating $numStrs strings\n";
for ($i=0; $i<$numStrs; $i++) {
    $len = int(rand(1060));    # 1060 is about 200 x ln(200)
    for ($j=0; $j<$len; $j++) {
	$letter = substr $alphabet, int(rand($alphaLen)), 1;
	print $letter;
    }
    print "\n";
}
