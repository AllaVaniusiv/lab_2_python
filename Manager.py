from Printer import  Printer
from InkjetPrinter import  InkjetPrinter
from LaserPrinter  import  LaserPrinter
from PhotoPrinter  import  PhotoPrinter 
from ThreeDPrinter  import ThreeDPrinter

class PrinterManager:

	def __init__(self):
	    """
	    Initialize a PrinterManager object.

	    Initializes an empty list of printers.

	    """
	    self.printers = [
	    InkjetPrinter("Hp", "inkjet", False, True, 50, 100, "Type1", 100, "Type2", 50, "Type3", 75, "Type4", 80),
	    InkjetPrinter("Canon", "inkjet", False, True, 55, 100, "Type1", 70, "Type2", 50, "Type3", 105, "Type4", 90),
	    LaserPrinter("Hp", "laser", True, False, 40, 150, 200, 300),
	    LaserPrinter("Canon", "laser", True, True, 60, 100, 250, 350),
	    PhotoPrinter("Hp", "inkjet", True, True, 25, 130, 210, 320),
	    PhotoPrinter("Canon", "laser", True, True, 30, 85, 245, 330),
	    ThreeDPrinter("Hp", "inkjet", True, True, 45, 70, 220),
	    ThreeDPrinter("Canon", "inkjet", True, True, 65, 75, 250),
	]

	def add_printer(self, printer):
	    """
	    Add a printer to the manager.

	    Args:
		printer (Printer): The printer to be added.

	    """
	    self.printers.append(printer)

	def find_printer_with_type(self, type):
	    """
	    Find printers of a specific type.

	    Args:
		type (str): The type of printers to find.

	    Returns:
		   list: A list of printers matching the specified type.

	    """
	    filtered_printers = list(filter(lambda printer : printer.pr_type==type, self.printers))
	    return filtered_printers

	def find_printer_with_more_paper_than(self, paper_count):
	    """
	    Find printers with more paper than a given count.

	    Args:
		paper_count (int): The minimum paper count to filter printers.
 
	    Returns:
		   list: A list of printers with more paper than the specified count.

	    """
	    filtered_printers = list(filter(lambda printer : printer.paper_count>paper_count, self.printers))
	    return filtered_printers
