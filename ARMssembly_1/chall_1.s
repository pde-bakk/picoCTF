	.arch armv8-a
	.file	"chall_1.c"
	.text
	.align	2
	.global	func
	.type	func, %function
func:
	sub	sp, sp, #32
	str	w0, [sp, 12] // store user_input at stack+12
	mov	w0, 68
	str	w0, [sp, 16] // store 68 at stack+16
	mov	w0, 2
	str	w0, [sp, 20] // store 2 at stack+20
	mov	w0, 3
	str	w0, [sp, 24] // // store 3 at stack+24
	ldr	w0, [sp, 20] // var w0 = 2
	ldr	w1, [sp, 16] // var w1 = 68
	lsl	w0, w1, w0	// logical left shift: w0 = w1 << w0 = 68 << 2 = 272
	str	w0, [sp, 28] // store 272 at stack=28
	ldr	w1, [sp, 28] // w1 = 272
	ldr	w0, [sp, 24] // w1 = 3
	sdiv	w0, w1, w0 // signed_divide: w0 = w1 / w0 = 90
	str	w0, [sp, 28] // store 90 at stack+28
	ldr	w1, [sp, 28] // w1 = 90
	ldr	w0, [sp, 12] // w0 = user_input
	sub	w0, w1, w0 // w0 = 90 - user_input
	str	w0, [sp, 28] // store (90 - user_input) at stack+28
	ldr	w0, [sp, 28]
	add	sp, sp, 32
	ret
	.size	func, .-func
	.section	.rodata
	.align	3
.LC0:
	.string	"You win!"
	.align	3
.LC1:
	.string	"You Lose :("
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	str	x1, [x29, 16]
	ldr	x0, [x29, 16]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi // call atoi on user input
	str	w0, [x29, 44] // store (int)argv1 at x29+44
	ldr	w0, [x29, 44]
	bl	func
	cmp	w0, 0
	bne	.L4 // if (func(w0) != 0) goto .LC4
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	puts
	b	.L6
.L4: // .L4 will call .LC1 which makes us lose :(
	adrp	x0, .LC1
	add	x0, x0, :lo12:.LC1
	bl	puts
.L6:
	nop
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
