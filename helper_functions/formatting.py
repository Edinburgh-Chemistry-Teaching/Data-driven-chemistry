"""
Functions to produce formatted string output in Jupyter notebooks
"""

__all__ = ['format_pseudocode',
		  ]
		  
__author__ = "James Cumby"
__email__ = "james.cumby@ed.ac.uk"		  



def format_pseudocode(steps, order):
    """ Return pseudocode steps with correct indentation. 
    
    Parameters
    ----------
    
    steps : dict
        Dictionary of pseudocode steps with integer keys
    order : list
        List of integers defining order of steps
    """
    
    indent = 0
    shift = -1
    output = ''
    
    # for step in order:
        # indent += shift
        # if (('IF' in steps[step]) or ('FOR' in steps[step])) and shift == 0:
            # indent -= 4    
        # if steps[step][-1] == '.':
            # count = 0
            # for character in steps[step][::-1]:
                # if character != '.':
                    # break
                # else:
                    # count += 1
            # indent -= 4*count
        # output += " "*indent + steps[step]+'\n'
        # shift = 0
        # if ('IF' in steps[step]) or ('FOR' in steps[step]):
            # shift = 4
        # if ('CONTINUE' in steps[step]):
            # shift = -8
            
    for step in order:
        output += " "*indent + steps[step]+'\n'
        if steps[step][-1] == ':':
            indent += 4
        elif steps[step][-1] == '.':
            count = 0
            for character in steps[step][::-1]:
                if character != '.':
                    break
                else:
                    count += 1
            indent -= 4*count
        if 'CONTINUE' in steps[step]:
            indent -= 8
            
    return output