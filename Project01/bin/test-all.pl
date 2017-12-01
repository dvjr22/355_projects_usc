#!/usr/bin/perl -w

# Script to test all CSCE 355 student projects
#
# Looks in each student's submission directory for a file 'subdir'.
# If found, appends onto the submission directory's pathname to find
# the directory with the submission code.
# Does a chdir to that directory and invokes project-test.pl on that
# directory.
# The default is the submission directory.

# Leaves a file all-comments.txt in the global submission root directory
# with contents of all the comment.txt and errlog.txt files created by
# project-test.pl

$bin_dir = "/acct/f1/fenner/public_html/csce355/prog-proj/bin";

if (!@ARGV) {
    print "Usage: test-all.pl global_submission_root_directory";
    exit(0);
}

$submission_root = $ARGV[0];
chdir $submission_root
    or die "Cannot chdir to directory '$submission_root' ($!)\n";

opendir DIR, "."
    or die "Cannot open directory '$submission_root' for reading ($!)\n";
@user_names = readdir DIR;
closedir DIR;

open COMMENTS, "> all-comments.txt"
    or die "Cannot open all-comments.txt for writing ($!)\n";

foreach $user_dir (sort @user_names) {
    next if $user_dir =~ /^\./o;
    next if !(-d $user_dir);

    print STDERR "Testing $user_dir\n";

    print COMMENTS "========================================================\n";
    print COMMENTS "COMMENTS FOR $user_dir:\n";

    # A file 'subdir' is placed (currently by hand) in the user's directory,
    # if necessary, indicating where the source files are.
    # Spaces in directory names cause problems, so change names to remove them.
    if (-r "$user_dir/subdir") {
	$user_subdir = `cat $user_dir/subdir`;
	chomp $user_subdir;
	$user_dir .= '/' . $user_subdir;
    }

    print COMMENTS "Running project-test.pl on '$user_dir' ... ";
    $rc = system("$bin_dir/project-test.pl", $user_dir);
    if ($rc >> 8) {
	print COMMENTS "TERMINATED ABNORMALLY\n\n";
    }
    else {
	print COMMENTS "OK\n\n";
    }

    print COMMENTS "Contents of comments.txt in $user_dir:\n\n";
    $cmts = `cat $user_dir/comments.txt`;
    print COMMENTS $cmts;
    print COMMENTS "========================================================\n";
    print COMMENTS "Contents of errlog.txt in $user_dir$:\n\n";
    $cmts = `cat $user_dir/errlog.txt`;
    print COMMENTS $cmts;
    print COMMENTS "========================================================\n";
}

close COMMENTS;
