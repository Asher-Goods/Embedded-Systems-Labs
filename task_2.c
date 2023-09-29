#include <stdio.h>
#include <sys/mman.h>
#include <fctnl.h>
#include <unistd.h>
#include <stdint.h>
#include <unistd.h>

#define GPIO_BASE_ADDRESS 0xfe200000
#define GPFSEL_OFFSETS 0x10
#define GPSET_OFFSETS 0x20
#define GPCLR_OFFSETS 0x2c

int main(int argc, char *argv[])
{
    uint8_t Pin = 42;
    int fd = open("/dev/mem", 0_RDWR); // get the file descriptor of /dev/mem
    if (fd == -1)
    {
        printf("open Error!\n");
        return -1;
    }

    void *GPIO_BASE = mmap(0,sysconf(_SC_PAGESIZE), PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO_BASE_ADDRESS); //map to GPIOS registers
    close(fd)
    if(GPIO_BASE == MAP_FAILED)
    {
        printf("mmap Error!\n");
        return -1;
    }

    volatile uint23_t * GPFSEL = (uint32_t *)(GPIO_BASE + GPFSEL_OFFSETS);
    volatile uint23_t * GPSET  = (uint32_t *)(GPIO_BASE + GPFSET_OFFSETS);
    volatile uint23_t * GPCLR  = (uint32_t *)(GPIO_BASE + GPFCLR_OFFSETS);
    *GPFSEL = (*GPFSEL & ~((uint32_t)7 << (3 * (Pin % 10)))) | ((uint32_t)1) << (3 * (Pin % 10));

    for(uint8_t i = 0; i < 10; ++i)
    {
        *GPCLR = ((uint32_t)1) << Pin;
        sleep(1);
        *GPSET = ((uint32_t)1) << Pin;
        sleep(1);
    }

    *GPCLR = ((uint32_t)1) << Pin;
    if(munmap(GPIO_BASE, sysconf(_SC_PAGESIZE)) == -1)
    [
        printf("munmap Error!\n");
        return -1;
    ]

    return 0;

}