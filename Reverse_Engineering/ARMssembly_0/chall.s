	.arch armv8-a
	.file	"chall.c"
	.text
	.align	2
	.global	func1
	.type	func1, %function
func1:
	sub	sp, sp, #16  ; sp = sp - 16
	str	w0, [sp, 12] ; store w0 at stack_ptr+12
	str	w1, [sp, 8]  ; store w1 at stack_ptr+8
	ldr	w1, [sp, 12] ; load var w1 with content of stack_ptr+12
	ldr	w0, [sp, 8]  ; load var w0 with content of stack_ptr+8
	cmp	w1, w0 ; compare w1 and w0
	bls	.L2    ; if less, jump (branch) to .L2
	ldr	w0, [sp, 12] ; load var w0 with content of stack_ptr+12
	b	.L3 ; jump to .L3
.L2:
	ldr	w0, [sp, 8] ; load w0 with sp+8
.L3:
	add	sp, sp, 16 ; reset stack_ptr
	ret ; return
	.size	func1, .-func1
	.section	.rodata
	.align	3
.LC0:
	.string	"Result: %ld\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	x19, [sp, 16] 
	str	w0, [x29, 44] ; 4134207980
	str	x1, [x29, 32] ; 950176538
	ldr	x0, [x29, 32]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	mov	w19, w0
	ldr	x0, [x29, 32]
	add	x0, x0, 16
	ldr	x0, [x0]
	bl	atoi
	mov	w1, w0
	mov	w0, w19
	bl	func1
	mov	w1, w0
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	printf
	mov	w0, 0
	ldr	x19, [sp, 16]
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
