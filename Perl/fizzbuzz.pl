for my $i (1..100) {
    my $output = "";
    if ($i % 3 == 0) {
        $output .= "fizz";
    }
    if ($i % 5 == 0) {
        $output .= "buzz";
    }
    if ($output eq "") {
        $output = "$i";
    }

    print "$output\n";
}