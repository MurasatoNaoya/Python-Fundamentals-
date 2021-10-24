# Modules are other .py scripts that caled be called within your own .py script. 
# Packages are therefore a collection of modules.

# You can create another .py file that has one function, using 'import' you can retrieve that function as a module into your other .py script. 
# The .py file from which you imported the function, would be a MODULE. 

from module_example import my_func # Do note that you have to follow syntax for the module name. 
my_func()

# Having a single directory for a module is fine, but it is also possible to organise your own package with many directories and sub-directories. 
# You do this by creating a MainPackage folder, as well as a SubPackage folder within it. 
# Within both of these folders, you must put __init__, this demonstrates that MainPackage or SubPackage are not just a directories, but a packages.
# Actally allowing you to call several modules within each folder. 


# When you are importing a module from a package, or even a package within a package; you can do so like this - 
from MyMainPackage import main_script 
main_script.report_main() # Always remember that when you are calling a function from an imported module, you must reference the module first before using a function within it.

from MyMainPackage.Subpackage import sub_script # On a similar point, the same goes for files, you have to demonstrate if one file is a parent file or not. 
sub_script.sub_report()


# You can of course, just retrieve individual functions also - 
from MyMainPackage.main_script import report_main
report_main()