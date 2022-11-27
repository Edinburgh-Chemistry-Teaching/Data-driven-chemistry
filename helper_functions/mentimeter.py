""" 
Class to help display mentimeter votes and results within a Jupyter Notebook
"""

__author__ = 'James Cumby'
__email__ = 'james.cumby@ed.ac.uk'

__all__ = ['Mentimeter',]

from IPython.display import IFrame, HTML

class Mentimeter():
    """ Produce HTML code suitable from mentimeter links"""
    
    def __init__(self, vote=None, result=None):
        """ Set up vote and result (display) links. """
        self.vote = vote
        self.display = result
            
    def _vote_iframe(self):
        """ Generate IFrame HTML for voting page. """
        if self.vote is not None:
            if self.display is not None:
                width='30%'
            else:
                width='70%'
            return "<iframe src={} height=100% width={}></iframe>".format(self.vote, width)
        else:
            return ""
            
    def _display_iframe(self):
        """ Generate IFrame HTML for results page. """
        if self.display is not None:
            if self.vote is not None:
                width='69%'
            else:
                width='90%'
            return "<iframe src={} height=100% width={}></iframe>".format(self.display, width)
        else:
            return ""
        
    def _single_div(self):
        """ Combine voting and results iframes (as required) into single div """
        return "<div style='width:100%; height:40vh;'> {} </div>".format(self._vote_iframe() + self._display_iframe())
            
    def show(self):
        """ Return the ipython HTML object containing the iframes """
        return HTML(self._single_div())
        