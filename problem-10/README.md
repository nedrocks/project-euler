Sum of primes
=============

Primes are calculated iteratively using the sieve of eratosthenes which I can
never spell correctly (http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).
There is likely a far more efficient calculation but this is quick and dirty.
<br/><br/>
I like to consider how large the numbers are which we're calculating. An upper
limit is if we were to sum all digits <= 2e6 which would be (2e6 * (2e6 + 1))/2
= ~2e12 Keeping a running sum is reasonable using a long (unsigned int is not
large enough because log_2(2e12) = ~40 bits to represent). Of course, the sum
is far less than this upper bound.
<br/><br/>
After running sieve of eratosthenes across all numbers under 2e6, the sum is
142913828922. Calculating this takes awhile though:
<pre>
time PYTHONPATH=. python -m problem-10.prime_sum

real    0m13.111s
user    0m12.154s
sys 0m0.090s
</pre>