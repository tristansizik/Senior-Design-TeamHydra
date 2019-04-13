//////////////////////////////////////

============ TEAM HYDRA ==============

	Senior Design Project 
	        2019 

 Raspberry Pi Automated Data Solution

	    Tristan Sizik
           Alejandro Peraza
	    Andrew Freiha
	   Carlos Hernandez
	     Kris Whaley
	   Thomas Barbarito 

Supervisor:
	    Ying Khai Teh

//////////////////////////////////////

Description:
   Develop a System using the Raspberry Pi which gathers Data
   in order to address the excessive salinity problem of
   Imperial Valley, CA. 

References:
   Dragino/LoRa app
   

****For Running At Startup:
	sudo nano /etc/rc.local
	type before exit:
	sudo /home/pi/rpi-lora-tranceiver-mod/dragino_lora_app/dragino_lora_app (rec or sender) & 
	
                           ~~~~~rec or sender based off if client or server~~~~~
~~~~~ampersand (&) is IMPORTANT or else program's infinite while loop will obstruct rpi healthy boot~~~~~
