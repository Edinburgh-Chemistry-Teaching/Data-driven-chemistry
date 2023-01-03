import random

def get_molecule(verbose=True):

    #some settings for colourful outout
    class color:
       DCY = '\033[36m'
       MAG = '\033[35m'
       BOLD = '\033[1m'
       END = '\033[0m'
        
    #list of molecules
    molecule = ['Testosterone','BromoLSD','Cannabinol','Dexamethasone','Estradiol','Fluorescein','Lycopene','Melatonin','Quinine','Riboflavin','Strychnine']
    
    #shortened dictionary of webpages, as all start with http://www.chm.bris.ac.uk/motm/
    webshort = {'Riboflavin': '/vitaminB2/vitaminb2h.htm', 
    	'Quinine': '/quinine/quinineh.htm',
    	'Dexamethasone': '/dexamethasone/dexamethasoneh.htm',
    	'Lycopene': '/lycopene/lycopeneh.htm',
    	'Melatonin': '/DMT/dmth.htm',
    	'BromoLSD': '/DMT/dmth.htm',
    	'Testosterone': '/testosterone/testosteroneh.htm',
    	'Fluorescein': '/rose-bengal/rose-bengalh.htm',
    	'Cannabinol': '/cannabidiol/cannabidiolh.htm',
    	'Estradiol': '/estradiol/estradiolh.htm',
    	'Strychnine': '/strychnine/strychnineh.html'}
    
    #get a random molecule
    m = random.choice(molecule)
    
    #locate associated webpage
    w = f'http://www.chm.bris.ac.uk/motm{webshort[m]}'
    
    if verbose:
        #output to screen
        #print("\n") #empty line
        #print(color.DCY + '    - * - * - * - * - * - * - !  !  ! - * - * - * - * - * - * -'+ color.END)
        #print("\n") #empty line
        print(color.BOLD + color.DCY + 'Your molecule is', m,'!'+ color.END)
        print('The structure file for your molecule %s is named data/%s.mol'%(m, m))
        print('The MassSpec data file for your molecule %s is named data/MS_%s.txt'%(m, m))
        print(f'Interesting facts about %s are on {w}')#'http://www.chm.bris.ac.uk/motm%s'%(m,w))
        #print("\n")
        #print(color.DCY + '    - * - * - * - * - * - * - !  !  ! - * - * - * - * - * - * -'+ color.END)
        
    return m, w
