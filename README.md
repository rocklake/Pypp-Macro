<h1 align="center">Pycro</h1>

<div align="center">
  
  <strong>A macro for the terminal game Py++</strong>
</div>


<div align="center">
  
![GitHub License](https://img.shields.io/github/license/rocklake/Pypp-Macro)
![GitHub forks](https://img.shields.io/github/forks/rocklake/Pypp-macro)
![GitHub Repo stars](https://img.shields.io/github/stars/rocklake/Pypp-macro)

</div>


# Requirements:
             
  Device the macro will be plugged into:
  
    Linux (Debian-based, preferably Raspbian)
    
    py-max installed in a folder named "py++" (case-sensitive!)
    
    tmux
  
  Device that will be plugged into the other device:
  
    Has to be a Raspberry Pi Pico 1
    
    Matching version of CircuitPython and Adafruit_HID lib
  

This project was inspired by an old version of Pico-Ducky.


### Update Mode 

To enter Update Mode, first, make sure caps lock is enabled on your keyboard. Then, plug in the macro device. This will stop the macro from starting, making it easy to update the code.py file.

# Info on all the variables: 

### start_delay  

Var Type: Int

Range: 0 - ∞ 

This variable controls the delay before the program starts.

### Log_in 

Var Type: bool 

Options: True, False

This controls if the program should auto-login as a part of the marco. (Note: The username and password should be defined if login is true. They will be used to log you in.

### fan_max 

Var Type: bool 

Options: True, False

On most computers that are running Linux, this will set the CPU fan speed to max speed.

### slowdown_level 

Var Type: str 

Options: “off”, “low”, “min”, “max” 

On some low power devices (for example the Raspberry Pi Zero 2W) the actions for the macro are sent too fast for it to register so this should fix the issue.

## Chip Chipper

### chip_chipper_repeat_all 

Var Type: Int 

Range: 0 - ∞ 

After the macro switches to Chip Chipper, this is how many cycles it will run. 

### chip_chipper_start_amount  

Var Type: int 0 - ∞ 

This is how many enters the macro will do after buying the first chip. 

### chip_chipper_cash_repeat  

Var Type: Int 

Range: 0 - ∞ 

this is how Many enters it will do after buying the second chipper and beyond 

### chip_chipper_repeat_amount 

Type Int 0 - ∞ 

after the macro switches to a chip chipper submode rebirth, this is how many of those cycles it will do. 

### chip_chiper_multiplication 

Type Int 0 - ∞ 
after buying and selling of any chips and chip chipper for previous buying amount would be multiplied by this number to get that new buying about. 

### chip_chipper_start_multiplication_amount 

Type Int 0 - ∞ 

at the beginning of submode this number will be multiplied with chip_chiper_multiplication to get the proper buying amount. 

### quintillion_point_chance 

Type Int 0 - ∞ 

at the beginning of every cycle a random NUMBER will be generated starting at 0 and ending at this number if is  Number is 1 it will start a sub mode of chip chipper called quintillion 

### chip_chipper_repeat_amount_qt 

Var Type: Int

Range: 0 - ∞ 

This controls how any enters the macro will do after buying the second chipper and beyond. !for qt submode only!

### chosen_chip_of_buying 

Var Type: str

Options: “b”, “r”, “bc”

This controls which chip for the macro will buy in the Chip Chipper mode.

## Trivia++

### trivia_repeat 

Type Int 0 - ∞ 

attempted cases of trivia questions This also counts gui, so I believe divided by 4 to get true number. 


## The default configuration is: 

start_delay = 0 

log_in = True 

username = "py"  

password = "hi"  

fan_max = True 

slowdown_level = "off" 

#### Chip Chipper

chip_chipper_repeat_all = 3 

chip_chipper_start_amount = 1020 

chip_chipper_cash_repeat = 100 

chip_chipper_repeat_amount = 3 

chip_chiper_multiplication = 50 

chip_chipper_start_multiplication_amount = 1 

quintillion_point_chance = 36 

chip_chipper_repeat_amount_qt = 49 

chosen_chip_of_buying = "r" 

#### Trivia++

trivia_repeat = 6000 

## How many points does it actually make?: 

### For v2.1:

triva coin in a hour 2,901.716 

rb_cc in a hour 46.213 

bot_points in a hour 711.479 

qt points an hour 2798351101696786e59 

all points in a hour is 384.5976 

vs 

### For v1.3: 

triva coin in a hour 3,312.373 

rb_cc in a hour 12.575 

bot_points in a hour 795.694 

all points in a hour is 338.282 
