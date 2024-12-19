.model small
.stack 100h
.data
msg db 3 
msg1 db ?
.code 

main proc  
    mov ax,@data
    mov ds,ax
    
    
    mov ah,2
    add msg,48
    mov dl,msg
    int 21h
  
    
    exit:
    mov ah,4ch
    int 21h
    main endp
end main