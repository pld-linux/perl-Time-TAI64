#!/usr/bin/perl
# tai64nlocal + diff
# tool that prints differences from last entry
# Author: Elan Ruusamäe <glen@delfi.ee>
# Date: 2012-08-02

use strict;
use warnings;
use Time::TAI64 qw/:tai64n/;

my ($last, $tai, $log, $t, $diff);
while (my $line = <>) {
	($tai, $log) = split(' ', $line, 2);
	$t = tai64nunix($tai);
	$diff = $last ? $t - $last : 0;
	printf "%s [+%.4f] %s", tai64nlocal($tai), $diff, $log;
	$last = $t;
}
