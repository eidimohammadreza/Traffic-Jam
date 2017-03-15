

	######################################################
	#  Run file by make run		               	         #
	#  Clean objects and modules by make claen	         #
	######################################################

EXEDIR = .


run: 

	
# to install necessary libraries
	
#	sudo apt install python-numpy python-scipy python-matplotlib 
	
# to compile and run by python 
	
	python main.py 
	
clean:

	rm -f *.tmp
	rm -f *.pyc
	rm -f *.pyo

	
