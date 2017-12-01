#!/usr/bin/perl -w

# This script runs independently of the current working directory.

$submissionRoot = "$ENV{HOME}/courses/csce355/fa13/project/submissions";

opendir DIR, $submissionRoot
    or die "Cannot open submission directory $submissionRoot ($!)\n";

@usernames = readdir DIR;

closedir DIR;

chdir $submissionRoot;

foreach $name (@usernames) {
    next
	unless -d "$submissionRoot/$name";

    $rc = system("zip -r $name $name");
    if ($rc >> 8) {
	print STDERR "zip for $name failed ($!)\n";
    }

    # Check if zip file exists
    if (-e "${name}.zip") {
	print STDERR "${name}.zip exists\n";
    }
    else {
	print STDERR "${name}.zip does not exist\n";
    }
}
