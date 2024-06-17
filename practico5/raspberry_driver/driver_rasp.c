#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/types.h>
#include <linux/fs.h>
#include <linux/device.h>
#include <linux/cdev.h>
#include <linux/gpio.h>
#include <linux/uaccess.h>

#define sensor_1 22
#define sensor_2 27

static dev_t first;
static struct cdev c_dev;
static struct class *cl;

static int sensor_select = 0;

static int my_open(struct inode *i, struct file *f)
{
    printk(KERN_INFO "Driver: open()\n");
    return 0;
}

static int my_close(struct inode *i, struct file *f)
{
    printk(KERN_INFO "Driver: close()\n");
    return 0;
}

static ssize_t my_read(struct file *f, char __user *buf, size_t len, loff_t *off)
{
    char sensor_value;
    int bytes_read = 0;

    if (*off > 0)
        return 0;

    printk(KERN_INFO "sensor_select: %d", sensor_select);

    if (sensor_select == 0)
    {
        sensor_value = '0' + gpio_get_value(sensor1);
    }
    else if (sensor_select == 1)
    {
        sensor_value = '0' + gpio_get_value(sensor_2);
    }
    else
    {
        return 0;
    }

    if (put_user(sensor_value, buf) != 0)
        return -EFAULT;

    *off += 1;
    bytes_read = 1;

    return bytes_read;
}

static ssize_t my_write(struct file *f, const char __user *buf, size_t len, loff_t *off)
{
    char pin_selection;
    int bytes_written = 0;

    if (len != 1)
        return -EINVAL;

    if (copy_from_user(&pin_selection, buf, 1) != 0)
        return -EFAULT;

    if (pin_selection == '22')
    {
        sensor_select = 0;
        printk(KERN_INFO "sensor_select: %d", sensor_select);
    }
    else if (pin_selection == '27')
    {
        sensor_select = 1;
        printk(KERN_INFO "sensor_select: %d", sensor_select);
    }
    else
    {
        return -EINVAL;
    }

    bytes_written = 1;

    return bytes_written;
}

static struct file_operations pugs_fops =
    {
        .owner = THIS_MODULE,
        .open = my_open,
        .release = my_close,
        .read = my_read,
        .write = my_write,
};

static int __init ofcd_init(void)
{

    printk(KERN_INFO "Initializing ofcd module\n");

    if (alloc_chrdev_region(&first, 0, 1, "driver_rasp") < 0)
    {
        return -1;
    }

    if ((cl = class_create(THIS_MODULE, "chardrv")) == NULL)
    {
        unregister_chrdev_region(first, 1);
        return -1;
    }

    if (device_create(cl, NULL, first, NULL, "input_device") == NULL)
    {
        class_destroy(cl);
        unregister_chrdev_region(first, 1);
        return -1;
    }

    cdev_init(&c_dev, &pugs_fops);

    if (cdev_add(&c_dev, first, 1) == -1)
    {
        device_destroy(cl, first);
        class_destroy(cl);
        unregister_chrdev_region(first, 1);
        return -1;
    }

    if (gpio_request(sensor1, "sensor1") < 0)
    {
        printk(KERN_ALERT "Error requesting GPIO pin for sensor 1\n");
        return -1;
    }

    if (gpio_request(sensor_2, "sensor2") < 0)
    {
        printk(KERN_ALERT "Error requesting GPIO pin for sensor 2\n");
        return -1;
    }

    gpio_direction_input(sensor1);
    gpio_direction_input(sensor_2);
    return 0;
}

static void __exit ofcd_exit(void)
{
    cdev_del(&c_dev);
    device_destroy(cl, first);
    class_destroy(cl);
    unregister_chrdev_region(first, 1);

    gpio_free(sensor1);
    gpio_free(sensor_2);

    printk(KERN_INFO "Exiting ofcd module\n");
}

module_init(ofcd_init);
module_exit(ofcd_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Facundo Dalla Fontana, Nicolas Gallardo, Federico Villar");
MODULE_DESCRIPTION("Driver para Raspberry Pi, 2 pines como entradas");