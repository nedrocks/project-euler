var n = 500001
var max = 0
var max_elem = 0

while (n < 1000000) {
      var count = 1
      var curr : BigInt = n
      while (curr != 1) {
            count += 1
            if (curr % 2 == 0) { curr /= 2 }
	    else { curr = curr * 3 + 1 }
      }
      if (count > max) {
          max = count
	  max_elem = n
      }
      n += 2
}

println("Max: " + max + ", max elem: " + max_elem)