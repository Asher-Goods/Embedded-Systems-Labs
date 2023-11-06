#include <stdio.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdint.h>
#include <unistd.h>

#define GPIO_BASE_ADDRESS 0xFE200000
#define GPFSEL_OFFSETS 0x0010
#define GPSET_OFFSETS 0x0020
#define GPCLR_OFFSETS 0x002c

int main(int argc, char *argv[])
{
    uint8_t Pin = 42;
    int fd = open("/dev/mem", O_RDWR); // get the file descriptor of /dev/mem
    if (fd == -1)
    {
        printf("open Error!\n");
        return -1;
    }

    void *GPIO_BASE = mmap(0,sysconf(_SC_PAGESIZE), PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO_BASE_ADDRESS); //map to GPIOS registers
    close(fd);
    if(GPIO_BASE == MAP_FAILED)
    {
        printf("mmap Error!\n");
        return -1;
    }

    volatile uint32_t * GPFSEL = (uint32_t *)(GPIO_BASE + GPFSEL_OFFSETS);
    volatile uint32_t * GPSET  = (uint32_t *)(GPIO_BASE + GPSET_OFFSETS);
    volatile uint32_t * GPCLR  = (uint32_t *)(GPIO_BASE + GPCLR_OFFSETS);
    *GPFSEL = (*GPFSEL & ~((uint32_t)7 << (3 * (Pin % 10)))) | ((uint32_t)1) << (3 * (Pin % 10));

    for(uint8_t i = 0; i < 10; ++i)
    {
        *GPCLR = ((uint32_t)1) << 10;
        sleep(1);
        *GPSET = ((uint32_t)1) << 10;
        sleep(1);
    }

    *GPCLR = ((uint32_t)1) << 10;
    if(munmap(GPIO_BASE, sysconf(_SC_PAGESIZE)) == -1)
    {
        printf("munmap Error!\n");
        return -1;
    }

    return 0;

}