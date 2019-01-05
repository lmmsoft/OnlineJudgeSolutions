## Useful Links

- [Python performance tips](http://www.manongjc.com/article/35920.html)
- [How to read input in Python in Codeforces](https://algocoding.wordpress.com/2015/02/18/how-to-read-input-in-python-in-codeforces/)
- [Some Python solutions](https://github.com/deveshbajpai19/CodeForces)
- [codeforces-scraper](https://github.com/shashank-sharma/codeforces-scraper)

## Useful code

- Method 1a: Using a list comprehension
    ```python
    a, b, c, d = [int(x) for x in input().split()]
    print(a*b*c*d)
    ```
    
- Method 1b: Using the map function
    ```python
    a, b, c, d = map(int, input().split())
    print(a*b*c*d)
    ```

- A faster way is to use stdin and stdout:
- Method 2a: List comprehension with stdin and stdout
    ```python
    from sys import stdin, stdout
    a, b, c, d = [int(x) for x in stdin.readline().rstrip().split()]
    stdout.write( str(a*b*c*d) + "\n" )
    ```
- Method 2b: Map with stdin and stdout
    ```python
    from sys import stdin, stdout
    a, b, c, d = map( int, stdin.readline().rstrip().split() )
    stdout.write( str(a*b*c*d) + "\n" )
    ```
    Note that you have to convert the output a*b*c*d to a string when passing it to the function stdout.write(…).