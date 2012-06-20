def from(n : BigInt) : Stream[BigInt] =
    Stream.cons(n, from(n + 1))

def sieve(s : Stream[BigInt]) : Stream[BigInt] =
    Stream.cons(s.head, sieve(s.tail filter { _ % s.head != 0 }))

def primes : Stream[BigInt] = sieve(from(2))

def isPrime(x : Int, primes : List[Int]) = True if primes.empty() else 

val primesLessThanSqrt = primes takeWhile(_ <= scala.math.sqrt(args(0).toInt))


println(primes takeWhile(_ <= args(0).toInt) reduceLeft(_+_))
