<h1 align="center">Pycro</h1>

<div align="center">
  
  <strong>A macro for the terminal game Py++</strong>
</div>


<div align="center">
  
![GitHub License](https://img.shields.io/github/license/rocklake/Pypp-Macro)
![GitHub forks](https://img.shields.io/github/forks/rocklake/Pypp-macro)
![GitHub Repo stars](https://img.shields.io/github/stars/rocklake/Pypp-macro)

</div>


## Requirements:
             
  Device the macro will be plugged into:
  
    Linux (Debian-based, preferably Raspbian)
    
    py-max installed in a folder named "py++" (case-sensitive!)
    
    tmux
  
  Device that will be plugged into the other device:
  
    Has to be a Raspberry Pi Pico 1
    
    Matching version of CircuitPython and Adafruit_HID lib
  

This project was inspired by an old version of Pico-Ducky.
## How to use: 
### switch file 
To switch the file make sure cap lock is enabled. This will stop the background from running. 
## All the variables: 
### start_delay  
Type Int 0 - ∞ 
the delay  before the program runs 
### Log_in 
Type bool 
The program log in for you so the username and password should be defined if login is true and they will be use for the program to log in 
### fan_max 
Type bool 
on most computers that are running Linux this will set the fan to its Max speed on the CPU 
### lowdown_level 
Type str “off”, “low”, “min”, “max” 
on summer lower power units like the raspberry pi 0 2W the commands happened too fast for it to registers to this should fix the problem 
### chip_chipper_repeat_all 
Type Int 0 - ∞ 
After the macros switches to chip chipper mode, this is how many cycles it would do. 
### chip_chipper_start_amount  
Type int 0 - ∞ 
This is how many enters it will do after buying the first chip. 
### chip_chipper_cash_repeat  
Type Int 0 - ∞ 
this is how Many enters it will do after buying the second chip and beyond 
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
Type Int 0 - ∞ 
this is how Many enters it will do after buying the second chip and beyond for qt submode 
### chosen_chip_of_buying 
Type str “b”, “r”, “bc” 
this is the Chip for the macro will buy 
### trivia_repeat 
Type Int 0 - ∞ 
attempted cases of trivia questions This also counts gui, so I believe divided by 4 to get true number. 
### the default configuration is: 
config start 
start_delay = 0 
 log_in = True 
 if log_in == True: 
username = "py"  
password = "hi"  
fan_max = True 
Options are "off", "low", "min", "max". Change to a higher setting if on a slower computer. 
slowdown_level = "off" 
chip chipper 
chip_chipper_repeat_all = 3 
chip_chipper_start_amount = 1020 
chip_chipper_cash_repeat = 100 
chip_chipper_repeat_amount = 3 
chip_chiper_multiplication = 50 
chip_chipper_start_multiplication_amount = 1 
quintillion_point_chance = 36 
chip_chipper_repeat_amount_qt = 49 
chosen_chip_of_buying = "r" 
trivia plus plus 
trivia_repeat = 6000 
config end 
## how much does it actually make: 
### For v2.1 
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
