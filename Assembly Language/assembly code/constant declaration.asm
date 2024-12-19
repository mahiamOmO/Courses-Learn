.model small
.stack 100h
.data
a equ '2'
b equ 'Computer Science & Engineering $'
c db b    
.code

main proc 
    
    mov dx,@data
    mov ds,ax
    
    mov ah,1
    int 21h
    mov bl,a
    
    
    mov ah,2
    mov dl,10
    int 21h
    mov dl,13
    int 21h
    
    
    mov ah,2
    mov dl,a
    int 21h   
    
    
    mov ah,2
    mov dl,10
    int 21h
    mov dl,13
    int 21h
    
    
    mov ah,9
    lea dx,c
    int 21h
   
    
    exit:
    mov ah,4ch
    int 21h
    main endp
end main  