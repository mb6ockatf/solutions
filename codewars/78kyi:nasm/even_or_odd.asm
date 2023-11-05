; nasm https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
global even_or_odd
section .text
        EVEN    dd      "Even",0
        ODD     dd      "Odd",0
; input: edi = number
; output: rax (a pointer to a statically allocated C-string, will not be freed
; by tests)
; callee saved registers: rbx, rsp, rbp, r12-r15
even_or_odd:
        mov eax,edi
        cdq
        mov ecx,2
        idiv ecx
        test edx,edx
        jz even

        mov rax,ODD
        ret

even:
        mov rax,EVEN
        ret