;mul->unsigned
;imul->signed/integer
;syntax mul/imuul source

.model small  
.stack 100h
.data
a db ? 
b db ?  
c db 'input first digit $'
d db 'input second digit $'
e db 'result $'

.code
main proc
  mov ax,@data
  mov ds,ax
  
  mov ah,9
  lea dx,c
  int 21h
  
  mov ah,1
  int 21h
  sub al,48  ; Convert ASCII to number
  mov a,al   ; Store the number in 'a' (byte)
  
  mov ah,9
  lea dx,d
  int 21h
  
  mov ah,1
  int 21h
  sub al,48  ; Convert ASCII to number
  mov b,al   ; Store the number in 'b' (byte)
  
  mov ah,9
  lea dx,e
  int 21h
  
  mov al,a   ; Load 'a' (byte) into AL
  mov bl,b   ; Load 'b' (byte) into BL
  mul bl     ; AL * BL = AX, result is in AX
  
  mov dl, al  ; Get the lower byte of the result
  add dl, 48  ; Convert to ASCII
  mov ah,2
  int 21h     ; Print the result
  
exit:
  mov ah,4ch
  int 21h
main endp

end main
