programmming_lang = ['Java', 'Python', 'Rust', 'C++', 'C#', 'C', 'Swift', 
                     'CSS', 'HTML', 'Clojure', 'JavaScript', 'PHP', 'Objective-C', 
                     'Fortran', 'ActionScript', 'Ada', 'Ruby', 'Go', 'TypeScript', 'R', 
                     'Groovy', 'Perl', 'Assembly language', 'Visual Basic', 'SQL', 'Object Pascal',
                     'MATLAB', 'Kotlin', 'Bash', 'Logo', 'PowerShell', 'Lisp', 'Dart']

numbers = list(range(100))

fx = lambda x,y: len(x[y]) # string length with choice index
f = lambda x: len(x) # string length
fi = lambda i: id(i) # id memory number
fs = lambda u: u.upper() # big letters
fo = lambda o: bin(o) # convert to binary

print("fx = ")
for i in range(len(programmming_lang)):
    print(i+1, programmming_lang[i], fx(programmming_lang, i))

print("f = ", list(map(f, programmming_lang)))    
print("fi = ", list(map(fi, programmming_lang)))    
print("fs = ", list(map(fs, programmming_lang)))    
print("fo = ", list(map(fo, numbers)))    

print("f (anomyous) = ", list(map(lambda x: len(x), programmming_lang)))
print("fi (anomyous) = ", list(map(lambda i: id(i), programmming_lang)))

