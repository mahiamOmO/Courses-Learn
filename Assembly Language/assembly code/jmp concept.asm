.model small
.stack 100h
.data   
a db 'Jmp Concept $' 
b db 'Assembly Language '
c db 'Programming $'

main proc  
     
     mov ax,@data
     mov ds,ax
     
     mov ah,9
     lea dx,a
     int 21h
     
     mov ah,2
     mov bl,10 
     int 21h
     mov dl,13
     int 21h
     
     mov cx,26
     mov ah,2
     mov dl,'A'
     
     m:
     mov ah,9
     lea dx,b
     int 21h
     jmp n
     
     n:
     mov ah,9
     lea dx,c
     int 21h
     jmp exit
    
    exit:
    mov ah,4ch
    int 21h
    main endp
end main 