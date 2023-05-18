from Manager import PrinterManager
from Printer import  Printer
from InkjetPrinter import  InkjetPrinter
from LaserPrinter  import  LaserPrinter
from PhotoPrinter  import  PhotoPrinter 
from ThreeDPrinter  import ThreeDPrinter


manager = PrinterManager()

printers_with_type = manager.find_printer_with_type("laser")
print("Printers with type 'laser':")
for printer in printers_with_type:
    print(printer)

print("\n")

printers_with_more_paper_than = manager.find_printer_with_more_paper_than(100)
print("Printers with paper count greater than 100:")
for printer in printers_with_more_paper_than:
    print(printer)

print("\n")
