; nasm https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1
global get_age

section .text
        phrase          dd      " years old",0
        buffer          times 11 db 0

; <--- unsigned int get_age(const char *inp) --->
get_age:
    xor eax,eax       ; EAX <- the result
    mov doubleword [buffer],edi
    mov doubleword [buffer],phrase
    ret
; ---------> endof get_age <---------
