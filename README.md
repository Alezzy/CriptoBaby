# Cripto baby steps

Hi, this is some of criptography related problems and their solutions.  
It covers some of the principles of RSA, El Gamal, number theory and abstract algebra in general.  
All these problems are from the class "Números Inteiros e Criptografia RSA" from UFRJ, the teacher was Luis Menasché.  
There are some mistakes on *3.2* and *12.2*.  
**Please do not copy this as your homework.**  

### Prerequisites

You need [python 2.7](https://www.python.org/downloads/) to run this.

### Testing

There is a bash script that tests the solutions, you should edit it with your information.  
In each directory there is a test case file called *exemplo.txt* and a expected output *saida.txt*.  

To run the tests you can just:
```
bash test.sh
```

## Problem set

| Problem | Description                                                                               |
| ------- | ----------------------------------------------------------------------------------------- |
| 1		  | Basic operations with python                                                              |
| 2.1	  | Naive division algorithm                                                                  |
| 2.2	  | Simple Euclidean algorithm                                                                |
| 3.1	  | Extended Euclidean algorithm                                                              |
| 3.2	  | Linear Diophantine equation solver for 2 variables                                        |
| 4.1	  | Naive Factorization algorithm                                                             |
| 4.2	  | Fermat Factorization algorithm                                                            |
| 5.1	  | Sieve of Eratosthenes                                                                     |
| 5.2	  | Highly composite numbers                                                                  |
| 6.1	  | Basic modular operations                                                                  |
| 6.2	  | Modular exponentiation                                                                    |
| 7.1	  | Modular multiplicative inverse                                                            |
| 7.2	  | Modular exponentiation of prime number through Fermat theorem                             |
| 8.1	  | Fermat theorem prime test                                                                 |
| 8.2	  | Korselt theorem to test Carmichael number                                                 |
| 8.3	  | Miller-Rabin                                                                              |
| 9.1	  | Chinese rest algorithm to solve linear modular systems                                    |
| 9.2	  | Chinese rest algorithm to simplify modular exponentiation                                 |
| 10.1	  | U(n) generator                                                                            |
| 10.2	  | Euler's totient function                                                                  |
| 10.3	  | Check if it is a subgroup of U(n)                                                         |
| 11	  | Generate the cyclic subgroups of U(n)                                                     |
| 12.1	  | Gauss algorithm to calculate a generator of a cyclic group of U(p)                        |
| 12.2	  | Lucas prime test                                                                          |
| 12.3	  | Pépin prime test of Fermat number                                                         |
| 13.1	  | Better Lucas prime test                                                                   |
| 13.2	  | Fermat method to find factors of Mersenne Numbers                                         |
| 14.1	  | "Break" RSA algorithm                                                                     |
| 14.2	  | Decript El Gamal messages                                                                 |
| 14.3	  | Baby-Step / Giant-Step Shanks algorithm to solve the discrete logarithm problem of a U(p) |

*n is a natural number*  
*p is a prime number*  

## Built With

* [Python 2.7.something](https://www.python.org/downloads/) - Just python

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

