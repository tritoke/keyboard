#![no_std]
#![no_main]

#[panic_handler]
fn panic(_info: &core::panic::PanicInfo) -> ! {
    exit()
}

fn exit() -> ! {
    loop {
        unsafe { core::arch::asm!("BKPT") };
    }
}

#[unsafe(no_mangle)]
fn _start() {
    exit()
}
